# Ansible: configuração dos PCs

Configuração em massa dos PCs (POP-TI §2). Aqui ficam os playbooks citados no POP-04 e no POP-06.

**Primeira vez?** Seguir o [passo a passo do primeiro PC](PRIMEIRO-PC.md).

| Playbook | POP | O que faz |
|---|---|---|
| `playbooks/linux-padrao.yml` | POP-04 §4.2 | Deixa um PC Ubuntu 26.04 no padrão da empresa |
| `playbooks/linux-atualizacao.yml` | POP-06 §3.2 | Atualização mensal (`apt` e `snap`) e reinício se precisar |

O playbook do Windows (POP-05) ainda não existe.

## O que o `linux-padrao.yml` faz

| Role | O quê |
|---|---|
| `base` | Confere o nome `<EMPRESA>-PC-<patrimônio>`, fuso horário, chave SSH da TI, atualizações e `unattended-upgrades` (diário, sem reinício automático) |
| `desktop` | Dash to Panel e ArcMenu ligados para todos os usuários (dconf), dock do Ubuntu desligado |
| `apps` | LibreOffice em português, leitor de PDF e Firefox com o bloqueador de anúncios uBlock Origin (instalado à força, o usuário não remove). Lista em `roles/apps/defaults/main.yml` (programa novo: POP-08) |
| `clamav` | ClamAV com alertas no syslog (para o Wazuh) e varredura semanal da `/home` |
| `agentes` | MeshCentral, GLPI Agent, Wazuh, UrBackup e AnyDesk (só com `anydesk: true` no host) |

Cada agente **só é instalado depois que o servidor dele estiver configurado** em `inventario/group_vars/linux/main.yml`. Enquanto o campo estiver vazio, o playbook pula o agente e avisa no final.

## Onde roda

O Ansible não roda direto no Windows. No servidor (PC do Lui Grosz, POP-TI §5.2) ele roda no **WSL2 com Ubuntu**, que o Docker Desktop já usa.

```bash
wsl --install -d Ubuntu
```

Dentro do Ubuntu do WSL:

```bash
sudo apt install -y ansible sshpass git
git clone https://github.com/vsautonomus/pop.git ~/repos/pop
cd ~/repos/pop/ansible
ansible-galaxy collection install -r requirements.yml
ssh-keygen -t ed25519 -C ansible-ti
```

Clonar **dentro do WSL** (`~/repos`), não usar `/mnt/c/...`: lá a pasta é aberta para todos e o Ansible ignora o `ansible.cfg` por segurança.

## Pendrive de instalação automática (POP-04 §4.1)

Um pendrive só serve para todos os PCs. Ele instala o Ubuntu já com idioma, teclado ABNT2, fuso, conta da TI, SSH e a chave do Ansible. Quem está no PC só confirma que pode apagar o disco.

**Preparar o pendrive (uma vez, e de novo quando trocar a senha da TI):**

1. Baixar a ISO do **Ubuntu 26.04 LTS Desktop** em `ubuntu.com`.
2. Gravar com o **Rufus** no **modo ISO** (não o modo DD). Assim o pendrive continua gravável.
3. Gerar o `autoinstall.yaml` na raiz do pendrive (ex.: pendrive na letra `E:`):
   ```bash
   python autoinstall/gerar.py E:\
   ```
   Ele pede a chave SSH pública do Ansible (copiar do WSL: `~/.ssh/id_ed25519.pub`), a senha da conta da TI e, se quiser, o nome e a senha do Wi-Fi da empresa (tudo no Vaultwarden). Com o Wi-Fi, o PC já conecta sozinho depois da instalação. A instalação também coloca o `net-tools` (`ifconfig`).

O `autoinstall.yaml` do pendrive tem a senha da TI (em hash) e a do Wi-Fi: guardar o pendrive com a TI.

**Em cada PC:**

1. Iniciar pelo pendrive. O instalador acha o `autoinstall.yaml` e **pede confirmação antes de apagar o disco**.
2. Esperar terminar e reiniciar.
3. O PC sobe com o nome `pc-novo-<4 últimos dígitos do MAC>`. Pegar o IP na lista de DHCP do OPNsense.

## PC novo (POP-04 §4.2)

1. Em `inventario/hosts.yml`, dentro de `linux`, incluir o PC com o nome definitivo e o IP:
   ```yaml
   TRR-PC-0012:
     ansible_host: 192.168.1.112
   ```
2. Rodar (pede a senha do `sudo` da TI e a do vault):
   ```bash
   ansible-playbook playbooks/linux-padrao.yml -l TRR-PC-0012 -K --ask-vault-pass
   ```
   Se o PC foi instalado à mão (sem o pendrive), instalar o SSH nele (`sudo apt install openssh-server`) e acrescentar `-k` na primeira vez.
3. O playbook troca o nome do PC para o definitivo.

## Atualização mensal (POP-06)

```bash
ansible-playbook playbooks/linux-atualizacao.yml -K
```

Atualiza de 5 em 5 PCs e reinicia só os que precisam. PC desligado ou fora da empresa aparece como `UNREACHABLE` e os outros seguem normalmente. Quando ele voltar à rede (POP-06 §3.3), rodar só nele com `--limit <nome-do-pc>`. O agente Wazuh fica **segurado** (`hold`) para não ficar mais novo que o servidor: atualizar junto com o servidor Wazuh.

## Senhas

O ID do grupo do MeshCentral fica criptografado com `ansible-vault`:

```bash
cp inventario/group_vars/linux/vault.yml.exemplo inventario/group_vars/linux/vault.yml
ansible-vault encrypt inventario/group_vars/linux/vault.yml
```

A senha do vault vai para o Vaultwarden. `vault.yml` só entra no git criptografado. Ao rodar, acrescentar `--ask-vault-pass`.

## Conferir no primeiro PC (POP-TI §9, passo 5)

- [ ] Dash to Panel e ArcMenu funcionam no GNOME do Ubuntu 26.04 (pacotes do repositório `universe`).
- [ ] O pacote `glpi-agent` do Ubuntu conversa com a versão do servidor GLPI. Se não, trocar pelo instalador oficial.
- [ ] Respostas do instalador do UrBackup (`urbackup_respostas`).
- [ ] Nome da conta da TI (`ansible_user`, hoje `ti`).
- [ ] O instalador Desktop do 26.04 lê o `autoinstall.yaml` do pendrive gravado pelo Rufus, instala o SSH e aplica o nome `pc-novo-XXXX`.
- [ ] O uBlock Origin aparece sozinho no Firefox (snap) e não dá para remover. Se não aparecer, conferir em `about:policies`.
- [ ] Acesso remoto do MeshCentral no Wayland (ALTERNATIVAS §1.2).
