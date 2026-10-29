# Ansible: configuração dos PCs

Configuração em massa dos PCs (POP-TI §2). Aqui ficam os playbooks citados no POP-04 e no POP-06.

**Primeira vez?** Seguir o [passo a passo do primeiro PC](PRIMEIRO-PC.md).

| Playbook | POP | O que faz |
|---|---|---|
| `playbooks/linux-padrao.yml` | POP-04 §4.2 | Deixa um PC Ubuntu 26.04 no padrão da empresa |
| `playbooks/linux-atualizacao.yml` | POP-06 §3.2 | Atualização mensal (`apt` e `snap`) e reinício se precisar |
| `playbooks/windows-padrao.yml` | POP-05 §4.2 | Deixa um PC Windows 11 no padrão da empresa |
| `playbooks/windows-atualizacao.yml` | POP-06 §3.2 | Atualização mensal (Windows Update e programas) com reinício |

## O que o `linux-padrao.yml` faz

| Role | O quê |
|---|---|
| `base` | Confere o nome `<EMPRESA>-PC-<patrimônio>`, sistema com o disco inteiro, fuso horário, chave SSH da TI, atualizações e `unattended-upgrades` (diário, sem reinício automático) |
| `funcionarios` | Conta dos funcionários (`usuario`, com administrador, sem senha e login automático, POP-TI §3.1). O pendrive já cria; o playbook cria nos PCs instalados antes ou à mão |
| `desktop` | Dash to Panel e ArcMenu (baixados do `extensions.gnome.org`, na versão do GNOME do PC, porque o Ubuntu 26.04 não tem pacote) ligados para todos os usuários (dconf), dock do Ubuntu desligado |
| `apps` | LibreOffice em português, leitor de PDF e Firefox com o bloqueador de anúncios uBlock Origin (instalado à força, o usuário não remove). Lista em `roles/apps/defaults/main.yml` (programa novo: POP-08) |
| `clamav` | ClamAV com alertas no syslog (para o Wazuh) e varredura semanal da `/home` |
| `agentes` | MeshCentral, GLPI Agent, Wazuh, UrBackup e AnyDesk (só com `anydesk: true` no host) |

## O que o `windows-padrao.yml` faz

| Role | O quê |
|---|---|
| `windows_base` | Confere o nome `<EMPRESA>-PC-<patrimônio>`, fuso de Brasília, Windows Update sem reinício no horário de trabalho (7h às 19h) nem com alguém usando o PC, atualizações do Windows e confere que o **Microsoft Defender** está ligado |
| `windows_funcionarios` | Conta dos funcionários (`usuario`, com administrador e sem senha, POP-TI §3.1). O pendrive já cria; o playbook confere e cria nos PCs instalados à mão |
| `windows_apps` | Firefox e LibreOffice pelo **Chocolatey** (lista em `windows_choco`, `inventario/group_vars/windows/main.yml`). uBlock Origin à força no Firefox e **uBlock Origin Lite** à força no Edge e no Chrome (os dois não aceitam mais o uBlock Origin completo). PDF: o Edge abre |
| `windows_agentes` | MeshCentral, GLPI Agent, Wazuh, UrBackup e AnyDesk (só com `anydesk: true` no host) |

No fim, reinicia o PC se precisar (atualização ou nome novo).

Cada agente **só é instalado depois que o servidor dele estiver configurado** em `inventario/group_vars/all/main.yml` (no Windows, também a versão do GLPI Agent e do Wazuh, em `group_vars/windows`). Enquanto o campo estiver vazio, o playbook pula o agente e avisa no final.

## Onde roda

O Ansible não roda direto no Windows. No servidor (PC do Lui Grosz, POP-TI §5.2) ele roda no **WSL2 com Ubuntu**, que o Docker Desktop já usa.

```bash
wsl --install -d Ubuntu
```

Dentro do Ubuntu do WSL:

```bash
sudo apt install -y ansible sshpass git python3-winrm
git clone https://github.com/trr-vale-da-serra/pop.git ~/repos/pop
cd ~/repos/pop/ansible
ansible-galaxy collection install -r requirements.yml
ssh-keygen -t ed25519 -C ansible-ti
```

`python3-winrm` é o acesso aos PCs Windows. Clonar **dentro do WSL** (`~/repos`), não usar `/mnt/c/...`: lá a pasta é aberta para todos e o Ansible ignora o `ansible.cfg` por segurança.

## Pendrive de instalação automática (POP-04 §4.1)

Um pendrive só serve para todos os PCs. Ele instala o Ubuntu já com idioma, teclado ABNT2, fuso, conta da TI, a **conta dos funcionários** (`usuario`, com administrador, sem senha e com login automático, POP-TI §3.1), SSH e a chave do Ansible. Quem está no PC só confirma que pode apagar o disco.

**Preparar o pendrive (uma vez, e de novo quando trocar a senha da TI):**

1. Baixar a ISO do **Ubuntu 26.04 LTS Desktop** em `ubuntu.com`.
2. Gravar com o **Rufus** no **modo ISO** (não o modo DD). Assim o pendrive continua gravável.
3. Gerar o `autoinstall.yaml` na raiz do pendrive (ex.: pendrive na letra `E:`):
   ```bash
   python autoinstall/gerar.py E:\
   ```
   Ele pede a chave SSH pública do Ansible (copiar do WSL: `~/.ssh/id_ed25519.pub`), a senha da conta da TI, o nome da conta dos funcionários (Enter = `usuario`) e, se quiser, o nome e a senha do Wi-Fi da empresa (tudo no Vaultwarden). Com o Wi-Fi, o PC já conecta sozinho depois da instalação. A instalação também coloca o `net-tools` (`ifconfig`).

O `autoinstall.yaml` do pendrive tem a senha da TI (em hash) e a do Wi-Fi: guardar o pendrive com a TI.

**Em cada PC:**

1. Iniciar pelo pendrive. O instalador acha o `autoinstall.yaml` e **pede confirmação antes de apagar o disco**.
2. Esperar terminar e reiniciar.
3. O PC sobe com o nome `pc-novo-<4 últimos dígitos do MAC>`. Pegar o IP na lista de DHCP do OPNsense.

## Pendrive de instalação automática do Windows (POP-05 §4.1)

Mesma ideia do pendrive do Linux, com o arquivo `autounattend.xml`. Ele instala o Windows 11 em português, teclado ABNT2, fuso de Brasília, **sem conta Microsoft** e sem as telas do primeiro uso. Também cria a conta local da TI e a **conta dos funcionários** (`usuario`, com administrador e sem senha, POP-TI §3.1), impede a criptografia de disco e liga o WinRM, que é o acesso do Ansible.

**Preparar o pendrive (uma vez):**

1. Criar o pendrive com a **Ferramenta de Criação de Mídia** da Microsoft (`microsoft.com/software-download/windows11`), em português. Se usar o Rufus, **desmarcar todas as opções** da janela "Windows User Experience": ele cria um arquivo próprio que conflita com o nosso.
2. Gerar o `autounattend.xml` na raiz do pendrive. No WSL do PC principal:
   ```bash
   sudo mkdir -p /mnt/d && sudo mount -t drvfs D: /mnt/d
   ```
   ```bash
   cd ~/repos/pop && git pull && python3 ansible/autounattend/gerar.py /mnt/d
   ```
   ```bash
   sudo umount /mnt/d
   ```
   Ele pede a edição (**home** ou **pro**, a mesma que o PC já tinha, para a licença ativar sozinha), a senha da conta da TI e o nome da conta dos funcionários (Enter = `usuario`).

O `autounattend.xml` tem a senha da TI só codificada (qualquer um decodifica): guardar o pendrive com a TI.

**Em cada PC:**

1. Iniciar pelo pendrive.
2. **Única tela:** a escolha do disco. Apagar as partições do disco do PC e escolher o espaço livre. Fica manual de propósito, para nunca apagar o disco errado.
3. Esperar. O Windows instala, entra uma vez sozinho na conta da TI, configura e reinicia.
4. O PC sobe com o nome `PC-NOVO-<4 últimos dígitos do MAC>`. Pegar o IP com `ipconfig` ou na lista de DHCP do firewall.

## PC novo (POP-04 §4.2)

Linux ou Windows, o mesmo comando. Depois que o PC terminou a instalação pelo pendrive e reiniciou:

1. **No PC:** ver o IP. No Linux, abrir o terminal (`Ctrl+Alt+T`) e rodar `hostname -I`. No Windows, abrir o Prompt de Comando e rodar `ipconfig` (linha "Endereço IPv4").
2. **No Ubuntu do WSL** (PC da TI), com o nome definitivo (`<EMPRESA>-PC-<patrimônio>`) e o IP do passo 1:
   ```bash
   cd ~/repos/pop && git pull && ansible/pc-novo.sh TRR-PC-0003 10.10.10.123
   ```
   Pede a senha da conta da TI (no Linux aparece `BECOME password`, no Windows `SSH password`). O PC reinicia sozinho no final.

O `pc-novo.sh`:
- descobre se o PC é Linux (responde no SSH) ou Windows (responde no WinRM);
- no Linux, aceita a chave SSH do PC (e troca a antiga, se o PC foi reinstalado);
- põe o PC no grupo certo do inventário `inventario/hosts.yml`, ou atualiza o IP se ele já estava lá;
- roda o `linux-padrao.yml` ou o `windows-padrao.yml` só nele: troca o nome do PC para o definitivo, configura tudo e **reinicia se precisar**.

Com alguém usando o PC, acrescentar `-e reiniciar=false` no fim do comando e reiniciar depois. Linux instalado à mão (sem o pendrive): instalar o SSH nele (`sudo apt install openssh-server`) e acrescentar `-k` (pede a senha SSH). Windows instalado à mão: ligar o WinRM (comandos 2 a 5 do `autounattend.modelo.xml`, no PowerShell como administrador).

O IP **não precisa ser fixo**: só serve para achar o PC enquanto ele ainda tem o nome `pc-novo-XXXX`. Se mudar, rodar o `pc-novo.sh` de novo com o IP novo. Depois que o firewall registrar os nomes no DNS (pfSense: *Services → DNS Resolver → Register DHCP leases*), dá para apagar as linhas `ansible_host` e o Ansible acha os PCs pelo nome.

O inventário (`inventario/hosts.yml`) fica **só no PC da TI**, fora do git: o repositório é público e o arquivo tem os IPs da rede. Modelo em `inventario/hosts.yml.exemplo`.

## Atualização mensal (POP-06)

```bash
ansible-playbook playbooks/linux-atualizacao.yml -K
```

```bash
ansible-playbook playbooks/windows-atualizacao.yml -k
```

Atualiza de 5 em 5 PCs e reinicia só os que precisam. PC desligado ou fora da empresa aparece como `UNREACHABLE` e os outros seguem normalmente. Quando ele voltar à rede (POP-06 §3.3), rodar só nele com `--limit <nome-do-pc>`. O agente Wazuh fica **segurado** (`hold`) para não ficar mais novo que o servidor: atualizar junto com o servidor Wazuh.

## Senhas

O ID do grupo do MeshCentral fica criptografado com `ansible-vault`:

```bash
cp inventario/group_vars/all/vault.yml.exemplo inventario/group_vars/all/vault.yml
ansible-vault encrypt inventario/group_vars/all/vault.yml
```

A senha do vault vai para o Vaultwarden. `vault.yml` só entra no git criptografado. Ao rodar, acrescentar `--ask-vault-pass`.

## Conferir no primeiro PC (POP-TI §9, passo 5)

- [ ] Dash to Panel e ArcMenu funcionam no GNOME 50 do Ubuntu 26.04 (vêm do `extensions.gnome.org`).
- [ ] O pacote `glpi-agent` do Ubuntu conversa com a versão do servidor GLPI. Se não, trocar pelo instalador oficial.
- [ ] Respostas do instalador do UrBackup (`urbackup_respostas`).
- [ ] Nome da conta da TI (`ansible_user`, hoje `ti`).
- [ ] O instalador Desktop do 26.04 lê o `autoinstall.yaml` do pendrive gravado pelo Rufus, instala o SSH e aplica o nome `pc-novo-XXXX`.
- [ ] O uBlock Origin aparece sozinho no Firefox (snap) e não dá para remover. Se não aparecer, conferir em `about:policies`.
- [ ] Windows: o `autounattend.xml` pula tudo menos a escolha do disco, a conta da TI entra, o WinRM responde (`Test-WSMan <IP>` de outro Windows) e a criptografia fica desligada (`manage-bde -status`).
- [ ] Windows: o `windows-padrao.yml` roda até o fim. Conferir: `usuario` é administrador, Firefox e LibreOffice em português, uBlock no Firefox (`about:policies`) e uBlock Origin Lite no Edge (`edge://policy`), PC reinicia com o nome novo.
- [ ] Windows Home: conferir se o Windows Update respeita o "sem reinício com alguém usando o PC" (é política, e o Home pode ignorar).
- [ ] Acesso remoto do MeshCentral no Wayland (ALTERNATIVAS §1.2).
