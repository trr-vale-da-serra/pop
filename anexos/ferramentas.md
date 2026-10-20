# Anexo: Ferramentas atuais da TI

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** Lui Grosz (TI)
> Faz parte do [Plano de TI](../POP-TI.md).
> **Este é o único lugar que diz qual programa a TI usa em cada função.** Os POPs falam só da função (ex.: "cofre de senhas"), para não precisarem mudar quando uma ferramenta for trocada. Trocou a ferramenta: atualizar esta tabela e a data acima. Opções avaliadas e plano B de cada uma: [ALTERNATIVAS.md](../ALTERNATIVAS.md).

---

## 1. Ferramentas por função

| Função (nome usado nos POPs) | Ferramenta atual | Observação |
|---|---|---|
| Chamados, inventário e patrimônio | **GLPI + GLPI Agent** | Citado pelo nome nos POPs |
| Acesso remoto (TI) | **MeshCentral** | Único serviço exposto na internet (porta 443, HTTPS), com 2FA |
| Programa de suporte de fornecedor | **AnyDesk** | Só nos PCs que recebem suporte de fornecedor (POP-TI §3.2) |
| Configuração em massa | **Ansible** | Os "roteiros de configuração" dos POPs são os playbooks do Ansible |
| Painel de segurança | **Wazuh** | Recebe os alertas dos antivírus |
| Antivírus | **Microsoft Defender** (Windows) e **ClamAV** (Linux) | |
| Monitoramento | **Uptime Kuma** | Alertas no e-mail da TI |
| Backup dos PCs | **UrBackup** | |
| Backup do servidor | **Restic** | Para o disco USB externo |
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
| POP-05 | Antes do roteiro de configuração: ligar o WinRM (comando guardado com o playbook). Criptografia que o Windows liga sozinho: BitLocker / Criptografia do dispositivo, desligar |
| POP-06 | Playbooks de atualização: `apt` (Linux) e `win_updates` (Windows) |

## 4. Programas dos PCs Linux

Tudo o que o roteiro de configuração padrão (POP-04) instala em todo PC Linux. Programa fora desta lista só entra pelo POP-08. Mudou a lista: atualizar aqui e no roteiro (`ansible/roles/`).

### 4.1 Para o funcionário usar

| Programa | Para quê | Observação |
|---|---|---|
| **Firefox** | Navegador | Com o bloqueador de anúncios **uBlock Origin**, instalado à força: o funcionário não consegue remover |
| **LibreOffice** | Documentos, planilhas e apresentações. Abre arquivos do Word, Excel e PowerPoint | Em português, com corretor ortográfico |
| **Visualizador de documentos** (Evince) | Abrir PDF | |
| **Dash to Panel** e **ArcMenu** | Barra de tarefas embaixo e menu Iniciar, parecido com o Windows | Extensões do GNOME (§2) |

### 4.2 Da TI, rodando por trás

| Programa | Função (nome usado nos POPs) | Observação |
|---|---|---|
| **GLPI Agent** | Inventário | |
| Agente do **MeshCentral** | Acesso remoto | |
| Agente do **Wazuh** | Painel de segurança | Versão segurada, atualiza junto com o servidor |
| **ClamAV** | Antivírus | Varredura semanal da pasta `/home` |
| Cliente do **UrBackup** | Backup dos PCs | |
| **AnyDesk** | Programa de suporte de fornecedor | Só nos PCs que recebem suporte de fornecedor (POP-TI §3.2) |
| **unattended-upgrades** | Atualização de segurança diária | Sem reinício automático (o reinício fica para o POP-06) |
| **OpenSSH** | Acesso do roteiro de configuração em massa | Só a TI usa |
| Pacotes de idioma português, `curl`, `perl`, `net-tools` | Base do sistema | |
