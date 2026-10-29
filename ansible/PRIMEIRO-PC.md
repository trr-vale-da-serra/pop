# Primeiro PC Linux: passo a passo

> **Data:** 17/10/2026 · **Responsável:** TI: Lui Grosz
> Roteiro único para preparar o servidor Ansible, o pendrive e instalar o primeiro PC (POP-TI §9, passo 5). Detalhes de cada parte no [README](README.md).

## 1. O que precisa

- [ ] ISO do **Ubuntu 26.04 LTS Desktop**, baixada de `ubuntu.com`
- [ ] **Pendrive de 16 GB ou mais** (vai ser apagado)
- [ ] **Rufus**, baixado de `rufus.ie` (versão portátil)
- [ ] **PC de teste** que pode ter o disco apagado (não o PC de trabalho de alguém)
- [ ] **Senha da conta da TI** nos PCs. Vai para o Vaultwarden; se ele ainda não estiver no ar, guardar em lugar seguro e passar para lá depois

## 2. Conferir a ISO

No PowerShell:

```powershell
Get-FileHash "$env:USERPROFILE\Downloads\ubuntu-26.04*-desktop-amd64.iso" -Algorithm SHA256
```

Comparar com o valor da ISO em `releases.ubuntu.com/26.04/SHA256SUMS`. Tem que ser **igual**. Se não for, baixar de novo.

## 3. Instalar o WSL (onde o Ansible roda)

No PowerShell **como administrador**:

```powershell
wsl --install -d Ubuntu
```

Reiniciar o PC. Na volta, o Ubuntu abre e pede um usuário e uma senha **do WSL** (separados de tudo, guardar no Vaultwarden).

## 4. Ansible e chave SSH (dentro do Ubuntu do WSL)

```bash
sudo apt update && sudo apt install -y ansible sshpass git
```

```bash
git clone -b ansible/linux-padrao https://github.com/trr-vale-da-serra/pop.git ~/repos/pop
```

```bash
cd ~/repos/pop/ansible && ansible-galaxy collection install -r requirements.yml
```

```bash
ssh-keygen -t ed25519 -C ansible-ti
```

No `ssh-keygen`, apertar Enter nas perguntas. Depois que a branch `ansible/linux-padrao` entrar na `main`, clonar sem o `-b ansible/linux-padrao`.

## 5. Gravar o pendrive

1. Abrir o Rufus, escolher o pendrive e a ISO.
2. Clicar em **Iniciar**. Quando perguntar, escolher **modo ISO** (não o modo DD).
3. Esperar terminar.

## 6. Colocar o `autoinstall.yaml` no pendrive

No **PC principal**, dentro do Ubuntu do WSL, com o pendrive conectado (trocar `D:` pela letra que o Windows deu a ele):

```bash
sudo mkdir -p /mnt/d && sudo mount -t drvfs D: /mnt/d
```

```bash
cd ~/repos/pop && git pull && python3 ansible/autoinstall/gerar.py /mnt/d
```

Ele pergunta:

| Pergunta | Resposta |
|---|---|
| Chave SSH pública | Enter (usa a chave do item 4) |
| Usuário da conta da TI | `ti` (Enter) |
| Senha da conta da TI | A senha do item 1 |
| Usuário da conta dos funcionários | `usuario` (Enter). Fica com administrador e sem senha |
| Wi-Fi da empresa, nome da rede | O nome da rede (no Vaultwarden). Vazio = sem Wi-Fi |
| Senha do Wi-Fi | A senha da rede (no Vaultwarden) |

```bash
sudo umount /mnt/d
```

O pendrive está pronto e serve para todos os PCs. Ele tem a senha da TI (em hash) e a **senha do Wi-Fi**: **guardar com a TI**. Os PCs conectam no Wi-Fi sozinhos e o funcionário não vê a senha.

## 7. Instalar o PC de teste

1. Ligar o PC pelo pendrive (tecla de boot: F12, F11, F8 ou Esc, depende da marca).
2. O instalador acha o `autoinstall.yaml` e **pede confirmação para apagar o disco**. Confirmar.
3. Esperar terminar. O PC reinicia sozinho.
4. Pegar o IP do PC: no terminal do próprio PC, `ifconfig` (ou `hostname -I`), ou na lista de DHCP do roteador/OPNsense (nome `pc-novo-XXXX`).

## 8. Rodar o Ansible

1. **No PC:** abrir o terminal (`Ctrl+Alt+T`) e ver o IP:
   ```bash
   hostname -I
   ```
2. **No Ubuntu do WSL**, com o nome definitivo do PC (`<EMPRESA>-PC-<patrimônio>`) e o IP do passo 1:
   ```bash
   cd ~/repos/pop && git pull && ansible/pc-novo.sh TRR-PC-0012 10.10.10.101
   ```
   Pede a senha da conta da TI (`BECOME password`). O script põe o PC no inventário e roda o playbook, que troca o nome do PC, cria a conta dos funcionários (`usuario`) e configura tudo. No final o PC **reinicia sozinho** (o login automático e a barra nova só valem depois disso).
   Enquanto os servidores do MeshCentral, GLPI e Wazuh não estiverem no ar, o playbook pula esses agentes e avisa no final. Isso é esperado.

## 9. Ajustar a aparência

1. No PC de teste, entrar com a conta da TI e deixar a barra e o menu do jeito que todos os PCs devem ficar (posição, tamanho, apps fixados, papel de parede).
2. No PC, exportar:
   ```bash
   dconf dump /org/gnome/shell/extensions/ > aparencia.txt
   ```
3. Passar o `aparencia.txt` para a TI incluir no Ansible (role `desktop`) e rodar o playbook de novo para conferir.

## 10. Conferir

Marcar a lista "Conferir no primeiro PC" do [README](README.md). Tudo certo: os outros PCs seguem o mesmo roteiro a partir do item 7 (resumo em "PC novo" no README).
