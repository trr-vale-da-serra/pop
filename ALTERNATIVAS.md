# Alternativas e histórico das decisões de TI

> **Data:** 29/10/2026 · **Responsável:** Lui Grosz (TI)
> Documento de consulta, **não vai para impressão**. Guarda as opções avaliadas, o motivo de cada escolha e o plano B de cada decisão.
> O que vale está no [POP-TI.md](POP-TI.md).

---

## 1. Computadores

### 1.1 Controle e acesso remoto

| Ferramenta | Situação | Por quê |
|---|---|---|
| **MeshCentral** | ✅ Escolhido (TI) | Painel web único para Windows e Linux: tela, terminal, arquivos, inventário básico, ações em massa. Grátis, servidor próprio |
| **MeshCentral pelo túnel da Cloudflare** | ✅ Escolhido (31/10/2026) | Nenhuma porta aberta no firewall (gerido pela empresa de TI), funciona com o IP público mudando (PPPoE) e chega nos PCs das outras bases. O agente só faz HTTPS de saída. Contra: depende da Cloudflare; se ela cair, o acesso remoto cai junto (a rede interna segue normal) |
| MeshCentral com a porta 443 aberta no firewall | ❌ Descartado (31/10/2026) | Servidor exposto direto na internet, precisa de DNS dinâmico e de mudança no firewall pela empresa de TI |
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
| **Sem backup dos PCs: arquivos só na nuvem da empresa** | ✅ Escolhido (29/10/2026) | O PC é refeito pelo pendrive e pelo Ansible em cerca de uma hora; só os arquivos importam. Contra: o que alguém salvar fora das pastas do servidor se perde com o PC, e programa instalado à mão fora da lista precisa ser reinstalado |
| UrBackup (arquivos todo dia e imagem do disco toda semana) | ❌ Descartado (era o escolhido até 29/10/2026) | As imagens dos PCs ocupariam boa parte dos 4 TB, para proteger o que o Ansible já refaz |
| **Espelho ZFS + snapshots (sanoid)** para os arquivos | ✅ Escolhido (29/10/2026) | Disco que morre não perde nada, e arquivo apagado ou estragado (inclusive por ransomware) volta do snapshot de uma hora, um dia ou um mês atrás |
| RAID da própria gaveta USB | ❌ Descartado | Se a gaveta queima, os discos só abrem em outra igual |
| mdadm (RAID do Linux) + ext4 | 🔁 Plano B | Se a gaveta USB derrubar discos do ZFS. Perde os snapshots e a conferência dos dados |
| **Disco 3 só para backup, sem criptografia** (dumps dos bancos e cópia da VM) | ✅ Escolhido (29/10/2026) | Arquivos comuns, que abrem sem programa nem senha. Fica desmontado fora da hora do backup. Contra: o disco roubado pode ser lido |
| Restic (criptografado) no disco 3 | ❌ Descartado | Criptografia sempre ligada, e sem a senha nada abre. O CheckVale continua com o restic dele para a nuvem (guia do servidor) |
| Cópia dos arquivos da nuvem da empresa no disco 3 | ❌ Não adotado agora (risco aceito, 29/10/2026) | Se a gaveta queimar ou os dois discos do espelho morrerem juntos, os arquivos se perdem: o disco 3 está na mesma gaveta. Reavaliar com um disco externo em rodízio fora da empresa |
| Cópia do servidor no Google Drive | ❌ Descartado | 15 GB é pouco, e regra: nada da empresa fora de equipamento da empresa |

### 1.5.1 Nuvem da empresa

| Opção | Situação | Por quê |
|---|---|---|
| **Samba (pastas de rede)** | ✅ Escolhido (29/10/2026) | Já vem no Windows e no Ubuntu, sem programa nos PCs e sem banco de dados para manter. Pasta pessoal com cota e pasta por departamento. "Versões anteriores" do Windows deixa a pessoa recuperar o arquivo sozinha. Contra: só funciona na rede da empresa (de fora, pela VPN) e sem cópia offline no PC |
| Nextcloud | ❌ Descartado (29/10/2026) | Mais do que o necessário (só armazenamento): servidor web, banco, cache e atualizações de uma versão maior por vez. Reavaliar se precisar de acesso pelo celular, de fora sem VPN, ou link para gente de fora |
| Seafile | ❌ Descartado | Mesma ideia do Nextcloud, com cliente próprio em cada PC |

### 1.6 Segurança e monitoramento

| Opção | Situação | Por quê |
|---|---|---|
| **Só Defender + ClamAV** | ✅ Escolhido (31/10/2026) | Antivírus em cada máquina, sem servidor para manter. Contra: cada alerta fica só no PC onde aconteceu; ninguém vê os de todas as máquinas juntos |
| Wazuh + Defender + ClamAV | ❌ Descartado (31/10/2026) | Painel central com todos os alertas, mas é um servidor pesado a mais, e o agente usa protocolo próprio (portas 1514/1515): os PCs das outras bases só chegariam nele por VPN entre as bases ou por um programa a mais em cada PC (WARP) |
| **Uptime Kuma** | ✅ Escolhido | Simples e leve, avisa por WhatsApp/Telegram/e-mail |
| Zabbix | ❌ Descartado | Pesado e complexo para o tamanho atual |
| **Vaultwarden** | ✅ Escolhido | Cofre compartilhado, usa os apps do Bitwarden |
| KeePassXC | ❌ Descartado | Arquivo local, ruim para compartilhar entre pessoas |
| **Sem criptografia de disco** (PCs e servidor) | ✅ Escolhido (16/10/2026) | PCs de mesa em escritório, com os arquivos no backup. Evita a senha do disco a cada reinício (que travaria a atualização mensal, POP-06) e o risco de perder os dados se a senha se perder. Contra: PC ou disco roubado, descartado ou mandado para conserto pode ser lido por quem pegar |
| LUKS (Linux) e BitLocker (Windows) com senha | ❌ Descartado | Alguém precisaria digitar a senha do disco a cada reinício |
| **Conta única dos funcionários (`usuario`), com administrador e sem senha** | ✅ Escolhido (23/10/2026) | Criada pelo pendrive de instalação, igual em todo PC: nada a fazer por pessoa na entrada e na saída. Contra: não dá para saber quem fez o quê no PC, e qualquer um no PC instala programas (inclusive vírus) e muda configurações; o POP-08 vira regra, não bloqueio |
| Uma conta por pessoa, sem administrador | ❌ Descartado (era o padrão até 22/10/2026) | Mais controle, mas uma conta para criar e apagar a cada entrada e saída |
| **Nenhum aviso na tela dos PCs** ("Não perturbe" travado no Linux; avisos desligados a cada entrada no Windows) | ✅ Escolhido (30/10/2026) | Some o aviso de atualização e de driver, que confundia o funcionário. A TI atualiza pelo POP-06. Contra: some também o aviso útil (pendrive conectado, download pronto, lembrete do calendário e, no Windows, bateria fraca do notebook). No Linux os avisos ficam no menu do relógio |
| Desligar só os avisos de atualização, driver e erro | ❌ Descartado (30/10/2026) | Mantinha os avisos úteis, mas a TI preferiu a tela sem nenhum aviso |
| Criptografia com desbloqueio pelo TPM | 🔁 Reavaliar se a empresa tiver notebooks | Liga sozinho e protege o disco tirado do PC. Não funciona em PC sem TPM |
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
| **Backup do WhatsApp no servidor** (backup local do aparelho + Syncthing) | ✅ Escolhido (29/10/2026) | Sem limite de 15 GB e sem depender do Google. Contra: o backup só chega quando o celular está na rede da empresa |
| Backup do WhatsApp no Google Drive | ❌ Descartado (era o escolhido até 29/10/2026) | Limite de 15 GB grátis e fora do equipamento da empresa |
| Backup do WhatsApp com vídeos | ❌ Descartado | Ocupa muito espaço sem necessidade |
| Backup do WhatsApp sem criptografia | ❌ Descartado | Preferida a criptografia, com a senha no Vaultwarden |
| **Google Drive + Documentos/Planilhas/Apresentações** para PDF e Office | ✅ Escolhido | Grátis, sem anúncios, usam o Gmail da empresa do aparelho |
| Microsoft 365 (um app só) | ❌ Descartado | Empurra login Microsoft, Copilot e assinatura |
| Collabora Office + MuPDF | ❌ Descartado | Interface mais simples, Collabora pesado em celular antigo |

**Plano B do bloqueio de apps:** se o Headwind Community não usar a Play Store gerenciada, os apps aprovados entram pela loja própria do Headwind (o funcionário continua sem instalar nada fora da lista).

---

## 3. Infraestrutura

| Opção | Situação | Por quê |
|---|---|---|
| **PC Ubuntu da empresa ligado 24h (VM para os sistemas, Docker)** | ✅ Escolhido | Equipamento da empresa, sem custo extra (guia do servidor) |
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
