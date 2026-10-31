# Anexo: Ferramentas atuais da TI

> **Versão:** 1.3 · **Data:** 29/10/2026 · **Responsável:** Lui Grosz (TI)
> Faz parte do [Plano de TI](../POP-TI.md).
> **Este é o único lugar que diz qual programa a TI usa em cada função.** Os POPs falam só da função (ex.: "cofre de senhas"), para não precisarem mudar quando uma ferramenta for trocada. Trocou a ferramenta: atualizar esta tabela e a data acima. Opções avaliadas e plano B de cada uma: [ALTERNATIVAS.md](../ALTERNATIVAS.md).

---

## 1. Ferramentas por função

| Função (nome usado nos POPs) | Ferramenta atual | Observação |
|---|---|---|
| Chamados, inventário e patrimônio | **GLPI + GLPI Agent** | Citado pelo nome nos POPs |
| Acesso remoto (TI) | **MeshCentral** | Único serviço exposto na internet (HTTPS, com 2FA), pelo túnel da Cloudflare: nenhuma porta aberta no firewall |
| Programa de suporte de fornecedor | **AnyDesk** | Em todo PC Windows; no Linux, só nos PCs que recebem suporte de fornecedor (POP-TI §3.2) |
| Configuração em massa | **Ansible** | Os "roteiros de configuração" dos POPs são os playbooks do Ansible |
| Antivírus | **Microsoft Defender** (Windows) e **ClamAV** (Linux) | |
| Monitoramento | **Uptime Kuma** | Alertas no e-mail da TI |
| Nuvem da empresa | **Samba** (pastas de rede) | No servidor: pasta pessoal por funcionário, com cota, e pasta por departamento. "Versões anteriores" do Windows mostra os snapshots |
| Discos do servidor | **ZFS** (espelho) + **sanoid** (snapshots) | Gaveta USB-C com 3 discos de 4 TB: 2 em espelho, 1 só para backup |
| Backup do servidor | **Scripts próprios** (`pg_dump` / `sqlite3` e cópia da VM) | Para o disco de backup, sem criptografia. Playbook `ansible/playbooks/servidor.yml` |
| Backup do WhatsApp | **Syncthing** (no celular e no servidor) | Envia o backup local do WhatsApp para o servidor |
| Cofre de senhas | **Vaultwarden** | |
| Firewall | **OPNsense** | Também faz a troca automática para o link reserva |
| VPN | **WireGuard** (no firewall) | |
| Link reserva | **Starlink** | Sem IP fixo |
| MDM dos celulares | **Headwind MDM Community** (Android Enterprise) | Aparelho zerado, provisionado por QR code. Também hospeda e instala os APKs da própria empresa (POP-08 §4) |
| Serviços do servidor | **Docker** (contêineres) | |
| Hospedagem de e-mail | **Ittek** | As três empresas |

## 2. Linux padrão

| Item | Atual |
|---|---|
| Distribuição | **Ubuntu 26.04 LTS** (Desktop), baixado de `ubuntu.com` |
| Ambiente gráfico | GNOME com as extensões **Dash to Panel** (barra de tarefas embaixo) e **ArcMenu** (menu Iniciar) |
| Atualização de segurança diária | `unattended-upgrades` |
| Loja de programas | `apt` / loja do Ubuntu |

## 3. Detalhes técnicos usados nos POPs

| POP | Detalhe |
|---|---|
| POP-04 | Antes do roteiro de configuração: `sudo apt install openssh-server`. No instalador: "apagar o disco", sem criptografia. Ou o pendrive de instalação automática (`ansible/PRIMEIRO-PC.md`) |
| POP-05 | Pendrive com `autounattend.xml` (`ansible/autounattend/`): instala sem conta Microsoft, cria a conta da TI, liga o WinRM (acesso do Ansible) e impede o BitLocker / Criptografia do dispositivo. Sem o pendrive: ligar o WinRM à mão e desligar a criptografia |
| POP-05 | Configuração em massa: `ansible/playbooks/windows-padrao.yml` (ou `ansible/pc-novo.sh`) |
| POP-06 | Playbooks de atualização: `apt` (Linux) e `win_updates` (Windows) |

## 4. Programas dos PCs Linux

Tudo o que o roteiro de configuração padrão (POP-04) instala em todo PC Linux. Programa fora desta lista só entra pelo POP-08. Mudou a lista: atualizar aqui e no roteiro (`ansible/roles/`).

### 4.1 Para o funcionário usar

| Programa | Para quê | Observação |
|---|---|---|
| **Firefox** | Navegador | Com o bloqueador de anúncios **uBlock Origin** e a extensão do **Bitwarden**, instalados à força: o funcionário não consegue remover |
| **Bitwarden** | Cofre de senhas (app) | Entra no Vaultwarden da empresa: no primeiro acesso, trocar o servidor para o endereço do Vaultwarden |
| **LibreOffice** | Documentos, planilhas e apresentações. Abre arquivos do Word, Excel e PowerPoint | Em português, com corretor ortográfico |
| **Visualizador de documentos** (Evince) | Abrir PDF | |
| **Dash to Panel** e **ArcMenu** | Barra de tarefas embaixo e menu Iniciar, parecido com o Windows | Extensões do GNOME (§2) |

### 4.2 Da TI, rodando por trás

| Programa | Função (nome usado nos POPs) | Observação |
|---|---|---|
| **GLPI Agent** | Inventário | |
| Agente do **MeshCentral** | Acesso remoto | |
| **ClamAV** | Antivírus | Varredura semanal da pasta `/home` |
| **AnyDesk** | Programa de suporte de fornecedor | Só nos PCs que recebem suporte de fornecedor (POP-TI §3.2) |
| **unattended-upgrades** | Atualização de segurança diária | Sem reinício automático (o reinício fica para o POP-06) |
| **OpenSSH** | Acesso do roteiro de configuração em massa | Só a TI usa |
| Pacotes de idioma português, `curl`, `perl`, `net-tools` | Base do sistema | |

## 5. Programas dos PCs Windows

Tudo o que o roteiro de configuração padrão (POP-05) instala em todo PC Windows. Programa fora desta lista só entra pelo POP-08. Mudou a lista: atualizar aqui e no roteiro (`windows_choco` em `ansible/inventario/group_vars/windows/main.yml`).

### 5.1 Para o funcionário usar

| Programa | Para quê | Observação |
|---|---|---|
| **Firefox** | Navegador | Com o **uBlock Origin** e a extensão do **Bitwarden**, instalados à força |
| **Bitwarden** | Cofre de senhas (app) | Entra no Vaultwarden da empresa: no primeiro acesso, trocar o servidor para o endereço do Vaultwarden |
| **Edge** | Navegador (vem com o Windows) e abrir PDF | Com o **uBlock Origin Lite**, instalado à força. No Chrome, se alguém instalar, também |
| **LibreOffice** | Documentos, planilhas e apresentações | |

### 5.2 Da TI, rodando por trás

| Programa | Função (nome usado nos POPs) | Observação |
|---|---|---|
| **Microsoft Defender** | Antivírus | Vem com o Windows; o roteiro confere que está ligado |
| **Chocolatey** | Instala e atualiza os programas | Só a TI usa |
| **GLPI Agent** e agente do **MeshCentral** | Inventário e acesso remoto | Só depois que o servidor de cada um estiver no ar |
| **AnyDesk** | Programa de suporte de fornecedor | Em todo PC Windows (POP-TI §3.2) |
| **WinRM** | Acesso do roteiro de configuração em massa | Ligado pelo pendrive; só aceita da mesma rede |
