# Anexo: Ferramentas atuais da TI

> **Versão:** 1.1 · **Data:** 17/10/2026 · **Responsável:** Lui Grosz (TI)
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
| Monitoramento | **Uptime Kuma** | Alertas no WhatsApp da TI |
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
