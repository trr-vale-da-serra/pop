# Ansible: configuração dos PCs

Configuração em massa dos PCs (POP-TI §2). Aqui ficam os playbooks citados no POP-04 e no POP-06.

**Primeira vez?** Seguir o [passo a passo do primeiro PC](PRIMEIRO-PC.md).

| Playbook | POP | O que faz |
|---|---|---|
| `playbooks/linux-padrao.yml` | POP-04 §4.2 | Deixa um PC Ubuntu 26.04 no padrão da empresa |
| `playbooks/linux-atualizacao.yml` | POP-06 §3.2 | Atualização mensal (`apt` e `snap`) e reinício se precisar |
| `playbooks/servidor.yml` | POP-TI §5.2, POP-07 | Discos do servidor, nuvem da empresa e backup (ver "Servidor" abaixo) |
| `playbooks/windows-padrao.yml` | POP-05 §4.2 | Deixa um PC Windows 11 no padrão da empresa |
| `playbooks/windows-atualizacao.yml` | POP-06 §3.2 | Atualização mensal (Windows Update e programas) com reinício |

## O que o `linux-padrao.yml` faz

| Role | O quê |
|---|---|
| `base` | Confere o nome `<EMPRESA>-PC-<patrimônio>`, sistema com o disco inteiro, fuso horário, chave SSH da TI, atualizações e `unattended-upgrades` (diário, sem reinício automático) |
| `funcionarios` | Conta dos funcionários (`usuario`, com administrador, sem senha e login automático, POP-TI §3.1). O pendrive já cria; o playbook cria nos PCs instalados antes ou à mão |
| `desktop` | Dash to Panel e ArcMenu (baixados do `extensions.gnome.org`, na versão do GNOME do PC, porque o Ubuntu 26.04 não tem pacote) ligados para todos os usuários (dconf), dock do Ubuntu desligado. **Nenhum aviso na tela** do funcionário ("Não perturbe" travado; ficam no menu do relógio), sem avisos de atualização, firmware/driver e erro, snaps atualizam à noite |
| `apps` | LibreOffice em português, leitor de PDF, Bitwarden (cofre de senhas) e Firefox com o bloqueador de anúncios uBlock Origin e a extensão do Bitwarden (instalados à força, o usuário não remove). Lista em `roles/apps/defaults/main.yml` (programa novo: POP-08) |
| `clamav` | ClamAV com alertas no syslog (para o Wazuh) e varredura semanal da `/home` |
| `agentes` | MeshCentral, GLPI Agent, Wazuh e AnyDesk (só com `anydesk: true` no host) |

## O que o `windows-padrao.yml` faz

| Role | O quê |
|---|---|
| `windows_base` | Confere o nome `<EMPRESA>-PC-<patrimônio>`, fuso de Brasília, **nenhum aviso na tela** (desliga de novo a cada entrada no Windows), Windows Update sem reinício no horário de trabalho (7h às 19h) nem com alguém usando o PC, atualizações do Windows e confere que o **Microsoft Defender** está ligado |
| `windows_funcionarios` | Conta dos funcionários (`usuario`, com administrador e sem senha, POP-TI §3.1). O pendrive já cria; o playbook confere e cria nos PCs instalados à mão |
| `windows_apps` | Firefox, LibreOffice e Bitwarden pelo **Chocolatey** (lista em `windows_choco`, `inventario/group_vars/windows/main.yml`). uBlock Origin e Bitwarden à força no Firefox e **uBlock Origin Lite** à força no Edge e no Chrome (os dois não aceitam mais o uBlock Origin completo). PDF: o Edge abre |
| `windows_agentes` | MeshCentral, GLPI Agent, Wazuh e AnyDesk (só com `anydesk: true` no host) |

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

## Servidor (POP-TI §5.2)

O servidor é o PC Ubuntu ligado 24h descrito no guia do servidor (host + VM `prod` com os sistemas). Os discos ficam numa **gaveta USB-C com 3 discos de 4 TB**:

| Disco | Uso | Onde |
|---|---|---|
| 1 e 2 | **Espelho ZFS** (4 TB úteis): se um disco morre, nada se perde. Snapshots automáticos a cada hora (24), dia (30) e mês (6) | `/dados` |
| 3 | **Só backup**, sem criptografia: dump de cada banco toda noite (30 dias) e cópia da VM `prod` todo domingo (2 cópias). Fica desmontado fora do backup | `/backup` |

| Role | O quê |
|---|---|
| `servidor_discos` | Confere os 3 discos, tira a economia de energia do USB, liga o aviso de saúde dos discos (smartd, no syslog), cria o espelho e as pastas (`usuarios`, `departamentos`, `whatsapp`, `emails-ex-funcionarios`, `apps-empresa`), os snapshots (sanoid) e formata o disco 3 |
| `arquivos` | **Nuvem da empresa** (Samba): uma conta e uma pasta pessoal por funcionário, com cota, e uma pasta por departamento. "Versões anteriores" do Windows mostra os snapshots |
| `whatsapp` | **Syncthing**: recebe a pasta do WhatsApp de cada celular em `/dados/whatsapp/<aparelho>`. Painel em `http://<IP>:47921` |
| `ferramentas_ti` | **Vaultwarden** (cofre de senhas) e **GLPI** (chamados e inventário) em contêineres, dados em `/srv`, com HTTPS pelo Caddy na 443, só para a rede interna. Ver "Ferramentas da TI" abaixo |
| `servidor_backup` | `ti-backup-bancos` (todo dia às 02:00) e `ti-backup-vm` (domingo à 01:30, desliga a VM por alguns minutos). Avisa o monitoramento (Uptime Kuma, monitor "Push") quando termina bem |

**Primeira vez:**

1. Gaveta no modo **JBOD** (discos separados), nunca no RAID da própria gaveta. Ligar no servidor e anotar os IDs:
   ```bash
   ls -l /dev/disk/by-id/ | grep -v part
   ```
   Cada disco precisa ter um ID (número de série) diferente.
2. No PC da TI: pôr o servidor no inventário (grupo `servidor`, modelo em `inventario/hosts.yml.exemplo`) e preencher `inventario/group_vars/servidor/main.yml`: IDs dos discos, `nuvem_endereco`, `departamentos` e `usuarios_samba`.
3. Senhas das pastas (uma por funcionário, geradas no cofre):
   ```bash
   cp inventario/group_vars/servidor/vault.yml.exemplo inventario/group_vars/servidor/vault.yml
   ```
   ```bash
   ansible-vault encrypt inventario/group_vars/servidor/vault.yml
   ```
4. Rodar com `preparar_discos=true`. **Apaga os 3 discos** (só na primeira vez; sem a opção, o playbook para e avisa em vez de apagar):
   ```bash
   ansible-playbook playbooks/servidor.yml -K --ask-vault-pass -e preparar_discos=true
   ```
5. O playbook mostra a chave SSH do root do servidor. Colocar no `~/.ssh/authorized_keys` da conta `ti` da VM `prod` (no grupo `docker`), para o backup pedir o dump dos bancos de lá.
6. Abrir `http://<IP>:47921` (Syncthing) e **definir usuário e senha do painel** antes de tudo.
7. Testar o backup na hora e conferir o resultado:
   ```bash
   sudo systemctl start ti-backup-bancos && journalctl -t ti-backup -n 20
   ```
8. No Uptime Kuma: criar um monitor "Push" com intervalo de 25 horas e pôr a URL em `backup_push_url`.

**Funcionário novo ou que saiu:** acrescentar (ou marcar `ativo: false`) em `usuarios_samba`, a senha em `senhas_samba` no vault, e rodar o playbook sem o `preparar_discos`. Trocar senha: mudar no vault e rodar de novo. Sistema novo com banco: acrescentar um item em `backup_bancos`.

**Ligar a pasta no PC** (POP-04/05, conferência), com a conta da pessoa:
- Windows: Explorador de Arquivos → *Este Computador* → *Mapear unidade de rede*, `\<IP>\<nome.sobrenome>`, marcar *Reconectar ao entrar* e *Usar credenciais diferentes*, e salvar a senha. Repetir para a pasta do departamento.
- Ubuntu: *Arquivos* → *Outros locais* → `smb://<IP>/<nome.sobrenome>`, usuário e senha da pessoa, *Lembrar para sempre*. Depois *Adicionar aos favoritos* (barra lateral). Repetir para a pasta do departamento.

**Disco com defeito:** `zpool status dados` mostra qual. Trocar o disco na gaveta e rodar `sudo zpool replace dados <ID antigo> <ID novo>`. O espelho se refaz sozinho, e o servidor continua no ar durante a troca.

### O servidor é também o PC da TI

O servidor (TRR-PC-0003) é a estação de trabalho da TI e o lugar de onde o Ansible roda. No inventário ele fica nos grupos `linux` e `servidor`, com `pc_da_ti: true` e `ansible_connection: local` (modelo em `inventario/hosts.yml.exemplo`). Com o `pc_da_ti`, o `linux-padrao.yml`:
- **mantém a conta `usuario` e tudo o que tem nela**, mas ela passa a pedir senha para entrar e para o `sudo`, e sem login automático. Antes, criar a senha: `sudo passwd usuario` (o playbook para e avisa se ela não tiver senha);
- deixa os avisos na tela (a TI precisa deles);
- reinicia sozinho às 04:00 quando uma atualização de segurança pede.

Ansible no próprio servidor (sem WSL):
```bash
sudo apt install -y ansible sshpass git python3-winrm
```

### Ferramentas da TI (Vaultwarden e GLPI)

Rodam no servidor em contêineres (`/srv/ferramentas-ti`), com os dados em `/srv/vaultwarden` e `/srv/glpi`. Entram pela rede interna em `https://cofre.<domínio>` e `https://glpi.<domínio>`. O certificado é do Let's Encrypt, validado pelo DNS da Cloudflare: nenhum PC ou celular precisa instalar certificado, e os nomes apontam para o IP interno do servidor (de fora não abrem).

**Primeira vez:**

1. **Token da Cloudflare** (o domínio da empresa precisa estar na Cloudflare): *My Profile → API Tokens → Create Token → Edit zone DNS*, só no domínio da empresa. Guardar no Vaultwarden.
2. Em `inventario/group_vars/servidor/main.yml`: `ti_dominio` e `nuvem_endereco` (IP do servidor, **fixo no firewall**: os nomes apontam para ele).
3. No `vault.yml` do servidor: `cloudflare_token` e `glpi_banco_senha` (`openssl rand -hex 24`).
4. **Trazer o Vaultwarden antigo** (WSL do PC antigo, pasta `~/vaultwarden`), antes do primeiro `servidor.yml`:
   - No PC antigo (WSL), parar e copiar os dados para o pendrive (`D:`):
     ```bash
     cd ~/vaultwarden && docker compose down && sudo mkdir -p /mnt/d && sudo mount -t drvfs D: /mnt/d && sudo tar czf /mnt/d/vaultwarden-data.tgz -C ~/vaultwarden data && sudo umount /mnt/d
     ```
   - No servidor:
     ```bash
     sudo mkdir -p /srv/vaultwarden && sudo tar xzf /media/$USER/PENDRIVE/vaultwarden-data.tgz -C /srv/vaultwarden
     ```
   - **Apagar o `vaultwarden-data.tgz` do pendrive** (é o cofre inteiro). A pasta antiga fica parada no PC antigo até tudo ser conferido.
5. Rodar:
   ```bash
   ansible-playbook playbooks/servidor.yml -K --ask-vault-pass
   ```
6. **Vaultwarden:** em cada app e extensão do Bitwarden, sair da conta e trocar o servidor para `https://cofre.<domínio>` (só o campo "Server URL"). As senhas são as mesmas. O certificado antigo (`vaultwarden-ca.crt`) não é mais usado e pode sair dos aparelhos.
7. **GLPI:** abrir `https://glpi.<domínio>`, entrar com `glpi` / `glpi` e **trocar na hora as senhas das quatro contas padrão** (`glpi`, `tech`, `normal`, `post-only`), ou desativar as que não forem usadas. Em *Configurar → Geral*, "URL da aplicação" = `https://glpi.<domínio>`. Depois, preencher `glpi_url` em `group_vars/all/main.yml` para os PCs ganharem o GLPI Agent.

**Backup:** o `ti-backup-bancos` leva toda noite o banco do Vaultwarden (SQLite), o do GLPI (MariaDB) e as pastas dos dois (`backup_pastas`): as chaves do Vaultwarden e a `glpicrypt.key` do GLPI, sem as quais o banco sozinho não basta. **Falta a cópia criptografada do Vaultwarden fora da máquina** (guia do servidor, infra §4).

**Versão nova:** trocar a imagem em `roles/ferramentas_ti/defaults/main.yml` e rodar o `servidor.yml`. Antes, conferir que o backup da noite terminou bem.

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
- [ ] Nome da conta da TI (`ansible_user`, hoje `ti`).
- [ ] O instalador Desktop do 26.04 lê o `autoinstall.yaml` do pendrive gravado pelo Rufus, instala o SSH e aplica o nome `pc-novo-XXXX`.
- [ ] O uBlock Origin e o Bitwarden aparecem sozinhos no Firefox (snap) e não dá para remover. Se não aparecer, conferir em `about:policies`.
- [ ] Windows: o `autounattend.xml` pula tudo menos a escolha do disco, a conta da TI entra, o WinRM responde (`Test-WSMan <IP>` de outro Windows) e a criptografia fica desligada (`manage-bde -status`).
- [ ] Windows: o `windows-padrao.yml` roda até o fim. Conferir: `usuario` é administrador, Firefox e LibreOffice em português, uBlock no Firefox (`about:policies`) e uBlock Origin Lite no Edge (`edge://policy`), PC reinicia com o nome novo.
- [ ] Windows Home: conferir se o Windows Update respeita o "sem reinício com alguém usando o PC" (é política, e o Home pode ignorar).
- [ ] Acesso remoto do MeshCentral no Wayland (ALTERNATIVAS §1.2).
- [ ] Servidor: "Versões anteriores" do Windows mostra os snapshots numa pasta do servidor (configuração `shadow:` do `smb.conf`).
