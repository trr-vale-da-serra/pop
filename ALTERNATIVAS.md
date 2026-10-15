# Alternativas e histórico das decisões de TI

> **Data:** 15/10/2026 · **Responsável:** Lui Grosz (TI)
> Documento de consulta, **não vai para impressão**. Guarda as opções avaliadas, o motivo de cada escolha e o plano B de cada decisão.
> O que vale está no [POP-TI.md](POP-TI.md).

---

## 1. Computadores

### 1.1 Controle e acesso remoto

| Ferramenta | Situação | Por quê |
|---|---|---|
| **MeshCentral** | ✅ Escolhido (TI) | Painel web único para Windows e Linux: tela, terminal, arquivos, inventário básico, ações em massa. Grátis, servidor próprio |
| **AnyDesk** | ✅ Permitido só para fornecedores | Muitos fornecedores só trabalham com AnyDesk. Uso assistido, nunca acesso autônomo (ver POP-TI §3.2) |
| **RustDesk** (servidor próprio) | 🔁 Plano B | Desde agosto/2026 tem acesso autônomo no Wayland (versão preview, Ubuntu/Debian). Entra se o MeshCentral não funcionar no Ubuntu 26.04 |
| **Tactical RMM** | ❌ Descartado | Agente Linux e alguns recursos ficam restritos a patrocinadores |
| **Só MeshCentral, sem AnyDesk** | ❌ Descartado | Fornecedores que só usam AnyDesk ficariam sem atender |

### 1.2 Desktop Linux (Wayland × Xorg)

| Opção | Situação | Por quê |
|---|---|---|
| **Ubuntu 26.04 LTS + GNOME (Wayland)** | ✅ Escolhido | Mais moderno, atualizações até 2031, mais seguro (um programa não lê a tela nem o teclado de outro) |
| **Ubuntu 26.04 + Xfce (Xorg)** | 🔁 Plano B | Se o acesso remoto falhar no Wayland. Xfce ainda roda em Xorg: AnyDesk e MeshCentral funcionam 100%. Já tem barra e menu parecidos com o Windows |
| **Ubuntu 24.04 + GNOME no Xorg** | ❌ Descartado | Funciona hoje, mas o suporte acaba em 2029 e obrigaria outra migração |
| **Linux Mint** | ❌ Descartado | Preferência por Ubuntu puro |

**Por que o Wayland importa:** no Ubuntu 26.04 o GNOME só roda em Wayland (a opção "Ubuntu no Xorg" foi removida no 25.10). No Wayland, programas de acesso remoto precisam de permissão para ver a tela. Em agosto/2026 o AnyDesk ainda exigia Xorg para acesso autônomo no Linux. Não foi encontrada informação confiável sobre o MeshCentral no Wayland.

**Teste que decide entre o escolhido e o plano B** (1 PC com Ubuntu 26.04 + GNOME):

1. MeshCentral: abrir a tela remota com e sem alguém no PC, e depois de reiniciar.
2. AnyDesk: fornecedor conecta com alguém aceitando na tela.
3. Se o item 1 falhar: testar o RustDesk. Se ele também falhar, trocar o padrão para Xfce.

Fontes: [Ubuntu 25.10 drops GNOME on Xorg](https://discourse.ubuntu.com/t/ubuntu-25-10-drops-support-for-gnome-on-xorg/62538) · [Ubuntu 26.04 LTS: novidades](https://linuxiac.com/ubuntu-26-04-lts-resolute-raccoon-released/) · [RustDesk no Wayland](https://alternativeto.net/news/2026/8/rustdesk-brings-true-unattended-remote-access-to-wayland-including-multi-monitor-setups/) · [AnyDesk e Wayland](https://pinggy.io/blog/remote_desktop_into_wayland_without_a_vps/)

### 1.3 Domínio

| Opção | Situação | Por quê |
|---|---|---|
| **Sem domínio: MeshCentral + Ansible** | ✅ Escolhido | Mais simples para o tamanho atual |
| **Samba AD** | 🔁 Reavaliar em abril/2027 | Login único e políticas (GPO) para Windows e Linux, mas é mais um servidor crítico |

### 1.4 Inventário e chamados

| Opção | Situação | Por quê |
|---|---|---|
| **GLPI + GLPI Agent** | ✅ Escolhido | Inventário automático, chamados e controle de patrimônio num lugar só |
| **Snipe-IT** | ❌ Descartado | Só controla patrimônio. Seria mais um sistema para manter |

### 1.5 Backup

| Opção | Situação | Por quê |
|---|---|---|
| **UrBackup + Restic (disco USB externo)** | ✅ Escolhido | Backup central dos PCs e cópia do próprio servidor para fora dele |
| **Veeam Agent Free** | ❌ Descartado | Sem painel central na versão grátis |
| **Só Restic** | ❌ Descartado | Linha de comando em cada máquina, mais trabalho |
| Cópia do servidor no Google Drive | ❌ Descartado | 15 GB é pouco para imagens de disco |

### 1.6 Segurança e monitoramento

| Opção | Situação | Por quê |
|---|---|---|
| **Wazuh + Defender + ClamAV** | ✅ Escolhido | Antivírus em cada máquina e um painel central com todos os alertas |
| Só Defender + ClamAV | ❌ Descartado | Ninguém veria os alertas de todas as máquinas juntos |
| **Uptime Kuma** | ✅ Escolhido | Simples e leve, avisa por WhatsApp/Telegram/e-mail |
| Zabbix | ❌ Descartado | Pesado e complexo para o tamanho atual |
| **Vaultwarden** | ✅ Escolhido | Cofre compartilhado, usa os apps do Bitwarden |
| KeePassXC | ❌ Descartado | Arquivo local, ruim para compartilhar entre pessoas |
| **TI guarda todas as senhas, inclusive as pessoais** | ✅ Escolhido | A TI consegue entrar em qualquer conta (suporte, saída, incidente). Contra: perde-se a prova de quem fez o quê, porque a TI também sabe a senha |
| Só o funcionário sabe a senha (senha provisória trocada no 1º acesso) | ❌ Descartado | |
| Cofre pessoal de cada funcionário no Vaultwarden | ❌ Descartado | |

---

## 2. Celulares

| Opção | Situação | Por quê |
|---|---|---|
| **Headwind MDM Community** | ✅ Escolhido | Open source, roda no servidor interno, não depende do Google Workspace |
| Google Android Management (Workspace) | ❌ Descartado | O básico grátis exige Workspace, e os recursos avançados são pagos |
| **Gmail da empresa por aparelho** | ✅ Escolhido | A proteção de restauração de fábrica (FRP) fica sempre com a empresa |
| Sem conta Google | ❌ Descartado | Sem Play Store, e o WhatsApp precisaria de APK manual |
| Conta do Google Play gerenciado | ❌ Descartado | Depende do Headwind Community suportar, o que não foi confirmado |
| Gmail pessoal do funcionário | ❌ Descartado | O aparelho fica travado pelo FRP quando a pessoa sai |
| Localização do aparelho | ❌ Descartado | A empresa não quer registrar localização |
| Celular pessoal (BYOD) com perfil de trabalho | ❌ Descartado | Dados da empresa só em equipamento da empresa |
| Modo quiosque (um app só) | ❌ Não adotado agora | Não há aparelho de função única hoje |
| Bloquear transferência de arquivos por USB | ❌ Não adotado agora | A depuração USB já fica bloqueada |
| Backup do WhatsApp com vídeos | ❌ Descartado | Aparelhos com muito uso passariam dos 15 GB grátis |
| Backup do WhatsApp sem criptografia | ❌ Descartado | Preferida a criptografia, com a senha no Vaultwarden |
| **Google Drive + Documentos/Planilhas/Apresentações** para PDF e Office | ✅ Escolhido | Grátis, sem anúncios, usam o Gmail da empresa do aparelho |
| Microsoft 365 (um app só) | ❌ Descartado | Empurra login Microsoft, Copilot e assinatura |
| Collabora Office + MuPDF | ❌ Descartado | Interface mais simples, Collabora pesado em celular antigo |

**Plano B do bloqueio de apps:** se o Headwind Community não usar a Play Store gerenciada, os apps aprovados entram pela loja própria do Headwind (o funcionário continua sem instalar nada fora da lista).

---

## 3. Infraestrutura

| Opção | Situação | Por quê |
|---|---|---|
| **PC de trabalho do Lui Grosz (Docker)** | ✅ Escolhido | Equipamento da empresa, sem custo extra |
| PC antigo dedicado | 🔁 Futuro | Migrar quando houver máquina sobrando. Com Docker, é copiar os volumes |
| VM grátis em nuvem (Oracle Always Free) | ❌ Descartado | Regra: nenhum serviço da empresa fora de equipamento da empresa |
| PC pessoal | ❌ Descartado | Mesma regra |
| **OPNsense junto com o servidor** | ✅ Escolhido | Failover para a Starlink e VPN desde o início |
| Cloudflare Tunnel na queda do link principal | ❌ Descartado | Aceita a indisponibilidade do acesso externo durante a queda |

---

## 4. Pessoas, e-mail e processos

| Opção | Situação | Por quê |
|---|---|---|
| **`nome.sobrenome@`** | ✅ Escolhido | Padrão mais comum no mercado |
| `nsobrenome@` (inicial + sobrenome) | ❌ Descartado | Mais difícil de adivinhar o endereço |
| `nome@` | ❌ Descartado | Esgota rápido com nomes repetidos |
| **Responsáveis: TI em todos, RH junto nos de pessoas** | ✅ Escolhido | |
| Revisão do jurídico nos formulários | ❌ Não necessária | Só o Formulário E (localização) pedia revisão, e ele foi removido |
| **App novo aprovado só pela TI** | ✅ Escolhido | Mais rápido |
| Gestor + TI, ou gestor + TI + direção | ❌ Descartado | |
| **B.O. só em caso de roubo** | ✅ Escolhido | Perda simples: só bloqueio e wipe |
| **Atualização mensal na 2ª quarta-feira à noite** | ✅ Escolhido | Dia seguinte ao Patch Tuesday da Microsoft |
