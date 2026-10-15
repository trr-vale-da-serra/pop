# Plano de POP de TI: Gestão de Computadores e Celulares

> **Versão:** 0.1 (rascunho) · **Data:** 15/10/2026 · **Responsável:** _a definir_
> **Regra geral:** todas as ferramentas precisam ser **gratuitas** (licença grátis ou open source, sem mensalidade).

---

## 1. Objetivo

Padronizar como a TI controla, protege e dá suporte aos equipamentos da empresa:

- **Computadores** em ambiente misto: Windows e Linux, porque parte das máquinas está migrando para Linux.
- **Celulares** corporativos Android.

## 2. Status das decisões

| Área | Item | Status |
|---|---|---|
| Celulares | Bloqueio de apps | ✅ Decidido |
| Celulares | Android Enterprise (versão gratuita) | ✅ Decidido |
| Celulares | Bloqueio remoto do aparelho | ✅ Decidido |
| Celulares | Bloqueio de depuração USB (anti-debug) | ✅ Decidido |
| Computadores | Ferramenta de controle remoto/gestão Windows + Linux | 🟡 Em avaliação |
| Computadores | Inventário, atualizações, backup, segurança | 🟡 Em avaliação |

---

## 3. Computadores (Windows + Linux)

### 3.1 Ferramenta principal de controle: propostas

| Ferramenta | O que faz | Windows | Linux | Custo | Observação |
|---|---|---|---|---|---|
| **MeshCentral** ⭐ | Acesso remoto (tela, terminal, arquivos), inventário básico, agrupamento de máquinas, ações em massa | ✅ | ✅ | Grátis (open source, servidor próprio) | **Recomendação principal.** Um painel web só para tudo, leve, roda em qualquer PC velho ou VM |
| **RustDesk** (servidor próprio) | Acesso remoto tipo "AnyDesk/TeamViewer" | ✅ | ✅ | Grátis no plano open source | Bom para suporte pontual, mas gerencia menos que o MeshCentral |
| **Tactical RMM** | RMM completo (scripts, alertas, patches) | ✅ | ⚠️ | Open source | O agente Linux e alguns recursos ficam restritos a patrocinadores. **Conferir antes de adotar** |

**Sugestão:** usar o **MeshCentral** para controle e suporte e o **Ansible** (3.2) para configurar várias máquinas de uma vez.

### 3.2 Configuração em massa e padronização

| Ferramenta | Uso | Custo |
|---|---|---|
| **Ansible** | Instala programas, aplica configurações e cria usuários em várias máquinas ao mesmo tempo. Linux via SSH, Windows via WinRM. Não precisa instalar agente | Grátis |
| **Samba AD** | Servidor de domínio gratuito (substitui o Windows Server). Login único e políticas (GPO) para Windows, e Linux entrando no domínio via SSSD | Grátis |

### 3.3 Inventário e chamados (helpdesk)

| Ferramenta | Uso | Custo |
|---|---|---|
| **GLPI + GLPI Agent** | Inventário automático (hardware, software, licenças) e sistema de chamados. Windows e Linux | Grátis (open source) |
| **Snipe-IT** | Controle de patrimônio: quem está com qual equipamento, termo de responsabilidade | Grátis (servidor próprio) |

### 3.4 Segurança e monitoramento

| Ferramenta | Uso | Custo |
|---|---|---|
| **Wazuh** | Monitoramento central de segurança (SIEM/XDR), **não é antivírus**: junta os alertas de todas as máquinas, detecta vulnerabilidades, alterações em arquivos e logins suspeitos, e recebe os alertas do Defender e do ClamAV. Windows e Linux | Grátis (open source) |
| **Microsoft Defender** | Antivírus que já vem no Windows | Grátis (incluso) |
| **ClamAV** | Antivírus para Linux | Grátis |
| **Zabbix** ou **Uptime Kuma** | Avisa quando máquina, internet (Starlink) ou serviço cai | Grátis |
| **BitLocker / LUKS** | Criptografia de disco (BitLocker no Windows Pro, LUKS no Linux) | Grátis (incluso) |
| **OPNsense** | Firewall/roteador com filtro de sites, VPN e **failover entre o link principal e a Starlink** (ver 5.4) | Grátis |

### 3.5 Backup

| Ferramenta | Uso | Custo |
|---|---|---|
| **UrBackup** | Backup centralizado de arquivos e imagem de disco. Windows e Linux | Grátis (open source) |
| **Veeam Agent (edição Free)** | Backup de máquina individual. Windows e Linux | Grátis |
| **Restic** | Backup por linha de comando, criptografado | Grátis |

### 3.6 Senhas

| Ferramenta | Uso | Custo |
|---|---|---|
| **Vaultwarden** | Cofre de senhas da empresa, compatível com os apps do Bitwarden | Grátis (servidor próprio) |

### 3.7 Atualizações (patches)

- **Linux:** `unattended-upgrades` (Ubuntu/Mint) para atualizações automáticas de segurança, mais Ansible para forçar atualizações.
- **Windows:** política local/GPO (via Samba AD) para o Windows Update, mais Ansible (módulo `win_updates`) para forçar atualizações.
- Sugestão de distro para a migração: **Ubuntu LTS** ou **Linux Mint** (estáveis e com suporte longo).

---

## 4. Celulares (Android)

### 4.1 Já decidido

- **Android Enterprise (versão gratuita):** base do gerenciamento.
- **Bloqueio de apps:** só apps aprovados (via Play Store gerenciada).
- **Bloqueio remoto:** travar o aparelho em caso de perda ou roubo.
- **Anti-depuração USB:** desativar Opções do desenvolvedor e Depuração USB.

### 4.2 Ideias complementares (todas gratuitas, quase todas são só políticas do próprio Android Enterprise)

| Ideia | Por quê |
|---|---|
| Exigir senha/PIN forte e bloqueio de tela automático | Proteção básica se o aparelho for perdido |
| Bloquear instalação de fontes desconhecidas (APK) | Evita app pirata ou malware |
| Bloquear restauração de fábrica pelo usuário | Impede que o funcionário "limpe" o aparelho e saia do controle |
| Limpeza remota (wipe) | Complemento do bloqueio remoto em caso de roubo |
| Wi-Fi corporativo enviado automaticamente | O funcionário não precisa saber a senha da rede |
| Bloquear transferência de arquivos via USB | Complementa a anti-depuração e evita vazamento de dados |
| Política de atualização do sistema (automática ou em janela de horário) | Mantém os aparelhos seguros |
| Modo quiosque (app único) para aparelhos de função específica | Ideal para coletor, vendas ou ponto |
| Perfil de trabalho (BYOD) para celular pessoal | Separa os dados da empresa sem invadir a privacidade |
| Localização do aparelho | Achar aparelho perdido (**avisar o funcionário por escrito**, ver LGPD) |
| **Headwind MDM (Community)** como alternativa | MDM open source e gratuito, caso o Android Enterprise grátis fique limitado |

---

## 5. Infraestrutura necessária (atenção)

As ferramentas são grátis, mas várias precisam de **um servidor** para rodar:

### 5.1 Internet

| Link | Uso | IP |
|---|---|---|
| **Link empresarial** | Principal | **IPv4 fixo** |
| **Starlink** | Backup (contingência) | Sem IP fixo (provável CGNAT) |

### 5.2 Servidor

- **Recomendado:** um PC antigo da empresa com **Ubuntu Server**, ligado 24h, **dentro da empresa** (custo: só energia). Como o link principal tem IP fixo, o servidor pode ser acessado de fora.
- **Alternativa:** VM gratuita em nuvem (ex.: **Oracle Cloud "Always Free"**). Conferir as condições atuais antes de usar.

### 5.3 Cuidados ao expor o servidor pelo IP fixo

- Expor para a internet **somente o MeshCentral** (porta 443/HTTPS), com **autenticação de dois fatores (2FA)** ligada.
- GLPI, Wazuh, Vaultwarden e os demais painéis ficam **só na rede interna**. De fora, acessar via **VPN** (WireGuard no OPNsense, grátis).
- **⚠️ Durante uma queda do link principal:** a internet cai para a Starlink, que não tem IP fixo. Os PCs **dentro da empresa** continuam funcionando normalmente, mas o **acesso de fora** ao servidor fica indisponível até o link principal voltar. É aceitável para backup. Se precisar de acesso externo mesmo nessa situação, usar **Cloudflare Tunnel** (grátis) como caminho alternativo.

### 5.4 Failover automático (link principal → Starlink)

O **OPNsense** (ver 3.4) faz **failover gratuito** entre os dois links: se o link principal cair, a rede passa para a Starlink automaticamente e volta quando o principal normaliza. Esse é um bom motivo para adiantar a implantação do firewall.

---

## 6. POPs a escrever (próximos passos)

| # | POP | Prioridade |
|---|---|---|
| POP-01 | Entrada de funcionário (criar usuário, entregar PC/celular, termo de responsabilidade) | Alta |
| POP-02 | Saída de funcionário (bloquear acessos, recolher e limpar equipamentos) | Alta |
| POP-03 | Celular perdido/roubado (bloqueio → localização → wipe → B.O.) | Alta |
| POP-04 | Instalação padrão de computador Linux (imagem padrão + agentes MeshCentral/GLPI/Wazuh) | Alta |
| POP-05 | Instalação padrão de computador Windows | Média |
| POP-06 | Atualizações mensais (Windows e Linux) | Média |
| POP-07 | Backup e teste de restauração (mensal) | Alta |
| POP-08 | Solicitação de novo app no celular/PC (aprovação) | Média |
| POP-09 | Incidente de segurança (vírus, vazamento, acesso indevido) | Média |
| POP-10 | Queda do link principal (failover para Starlink e retorno) | Média |

---

## 7. Pendências / decisões em aberto

- [ ] Validar o MeshCentral como ferramenta principal de controle (teste com 2 PCs: 1 Windows e 1 Linux)
- [ ] Separar o PC que será o servidor interno (Ubuntu Server)
- [ ] Decidir quando implantar o OPNsense (failover link principal → Starlink)
- [ ] Definir a distro Linux padrão
- [ ] Decidir se haverá domínio (Samba AD) ou só gestão via MeshCentral/Ansible
- [ ] Confirmar os limites da versão gratuita do Android Enterprise escolhida
- [ ] Definir o responsável por cada POP
