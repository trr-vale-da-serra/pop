# Plano de TI: Gestão de Computadores e Celulares

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** Lui Grosz (TI)
> Empresas: Postos Vale da Serra, Sertão Petróleo e TRR Vale da Serra.
> **Regra geral:** todas as ferramentas são **gratuitas** (licença grátis ou open source, sem mensalidade).
> **Regra de equipamento:** nenhum serviço ou dado da empresa roda em equipamento que não seja da empresa.

---

## 1. Objetivo

Padronizar como a TI controla, protege e dá suporte aos equipamentos da empresa:

- **Computadores:** Linux (padrão) e Windows (só onde algum programa exige).
- **Celulares** corporativos Android.

---

## 2. Ferramentas adotadas

| Área | Ferramenta | Para quê |
|---|---|---|
| Acesso remoto e controle | **MeshCentral** | Tela, terminal e arquivos de qualquer PC, Windows ou Linux, pelo navegador |
| Suporte de fornecedor | **AnyDesk** | Só para fornecedores externos, com regras (§3.2) |
| Configuração em massa | **Ansible** | Instala programas e aplica configurações em vários PCs de uma vez |
| Inventário, chamados e patrimônio | **GLPI + GLPI Agent** | Inventário automático, chamados de TI e quem está com cada equipamento |
| Segurança | **Wazuh** | Painel central de alertas de segurança de todas as máquinas |
| Antivírus | **Microsoft Defender** (Windows) e **ClamAV** (Linux) | Antivírus em cada máquina, com alertas enviados ao Wazuh |
| Monitoramento | **Uptime Kuma** | Avisa quando o link, o servidor ou um serviço cai |
| Backup de PCs | **UrBackup** | Backup central de todos os PCs no servidor |
| Backup do servidor | **Restic** | Cópia do próprio servidor para um disco USB externo |
| Senhas | **Vaultwarden** | Cofre com **todas** as senhas: da empresa e de cada funcionário |
| Criptografia de disco | **BitLocker** (Windows Pro) e **LUKS** (Linux) | Protege os dados se o PC for roubado |
| Firewall e internet | **OPNsense** | Firewall, VPN WireGuard e troca automática para a Starlink |
| Celulares | **Headwind MDM Community** (Android Enterprise) | Políticas, bloqueio de apps, bloqueio e limpeza remotos |

Não há domínio (Active Directory). As configurações dos PCs são aplicadas pelo Ansible.

---

## 3. Computadores

### 3.1 Sistema padrão

- **Linux (padrão):** **Ubuntu 26.04 LTS** com GNOME, com as extensões **Dash to Panel** (barra de tarefas embaixo) e **ArcMenu** (menu Iniciar), para a tela ficar parecida com o Windows. Instalação no POP-04.
- **Windows:** fica só nos PCs que usam programas que não rodam no Linux (ex.: alguns sistemas de banco ou fornecedores). Instalação no POP-05.
- **Nome dos computadores:** `<EMPRESA>-PC-<patrimônio>`, com `POSTOS`, `SERTAO` ou `TRR` no lugar de `<EMPRESA>` (ex.: `TRR-PC-0012`).
- **Usuários:** cada pessoa tem um usuário **sem permissão de administrador**. A TI tem uma conta administradora separada, com a senha no Vaultwarden.

### 3.2 Acesso remoto

**TI:** sempre pelo **MeshCentral**, com 2FA ligado para todos os usuários do painel.

**Fornecedores (AnyDesk):**

1. Só quando **a empresa chamou o fornecedor**. Nunca para quem ligou oferecendo suporte.
2. Sempre **assistido**: alguém no PC aceita a conexão e acompanha. **Nunca** configurar senha de acesso autônomo.
3. Cada acesso é registrado num **chamado do GLPI**: fornecedor, data, motivo e quem acompanhou.
4. O AnyDesk fica instalado só nos PCs que recebem suporte de fornecedor.

### 3.3 Segurança

- **Antivírus:** Defender no Windows e ClamAV no Linux, os dois enviando alertas ao Wazuh.
- **Wazuh:** a TI olha o painel **toda semana** e trata os alertas críticos no mesmo dia (POP-09).
- **Criptografia de disco:**
  - Linux: **LUKS**, ligado na instalação.
  - Windows Pro: **BitLocker**, com a chave de recuperação no Vaultwarden.
  - Windows Home: usar a **Criptografia do dispositivo** se o PC tiver. Se não tiver, o PC fica na lista para migrar para Linux ou atualizar para Pro.
- **Senhas:** **todas** as senhas ficam no Vaultwarden, inclusive as pessoais de cada funcionário (e-mail, Sistema VS, ERP, Petroshow, Sigest, Infinitum, Orion, PC), numa pasta por funcionário. Só a TI acessa o cofre, com 2FA. A TI gera senhas fortes e entrega pessoalmente. O funcionário **não troca** senha sozinho: pede à TI, que troca e atualiza o cofre.
- **Monitoramento:** o Uptime Kuma vigia o link principal, a Starlink, o servidor e cada serviço. Os alertas vão para o WhatsApp da TI.

### 3.4 Atualizações

- **Linux:** atualizações de segurança automáticas todos os dias (`unattended-upgrades`).
- **Mensal (Windows e Linux):** na **2ª quarta-feira de cada mês, à noite**, o Ansible força as atualizações pendentes e reinicia o que precisar. Detalhes no POP-06.

### 3.5 Backup

| O quê | Como | Frequência | Guarda |
|---|---|---|---|
| Arquivos dos PCs | UrBackup | Toda noite | 30 dias |
| Imagem completa do disco dos PCs | UrBackup | Toda semana | 4 imagens |
| Servidor inteiro (serviços, cofre, backups) | Restic para disco USB externo | Toda noite | 30 dias |
| WhatsApp dos celulares | Google Drive do Gmail do aparelho (§4.3) | Todo dia | Último backup |
| Caixa de e-mail de quem saiu | Download por IMAP para o servidor (POP-02) | Na saída | **Permanente** |

**Teste de restauração todo mês** (POP-07). Backup que nunca foi testado não conta como backup.

---

## 4. Celulares (Android)

### 4.1 Conta Google

- A TI cria **um Gmail por celular**: `celularNN.<empresa>@gmail.com` (ex.: `celular01.trrvaledaserra@gmail.com`). A senha e o 2FA ficam no **Vaultwarden**.
- A conta fica com o **aparelho**, não com a pessoa. O funcionário **nunca** entra com o Gmail pessoal no aparelho da empresa.
- Assim a proteção contra restauração de fábrica (FRP) fica sempre com a empresa: depois de um reset ou wipe, a TI desbloqueia o aparelho com essa conta.
- **E-mail de recuperação:** `lui@trrvaledaserra.com.br` (responsável de TI).
- **Telefone de recuperação:** celular corporativo do responsável de TI (Lui Grosz). Nunca número pessoal, nunca o chip do próprio aparelho.
- Se o responsável de TI mudar, trocar o e-mail e o telefone de recuperação de todas as contas (POP-02).
- O Google limita quantas contas um mesmo número pode verificar. Se travar, verificar a conta na criação com o chip do próprio aparelho e manter o número da TI só como recuperação.

### 4.2 Políticas do Headwind MDM

Todo celular corporativo é registrado no Headwind MDM (aparelho zerado, provisionado por QR code) e recebe:

| Política | Regra |
|---|---|
| Bloqueio de apps | Só apps da lista aprovada pela TI (POP-08) |
| Apps de fora da loja (APK) | Bloqueados |
| Senha | PIN de no mínimo 6 dígitos, bloqueio de tela automático em 2 minutos |
| Restauração de fábrica pelo usuário | Bloqueada |
| Depuração USB e Opções do desenvolvedor | Bloqueadas |
| Bloqueio remoto | Ativo |
| Limpeza remota (wipe) | Ativa |
| Wi-Fi da empresa | Enviado automaticamente (o funcionário não sabe a senha) |
| Atualização do sistema | Automática, em janela noturna |
| Localização | **Desativada.** A empresa não registra nem consulta a localização dos aparelhos |

Só aparelhos da empresa. **Celular pessoal não é gerenciado** e não recebe dados da empresa.

**Apps padrão** (instalados em todo celular corporativo pelo Headwind MDM):

| App | Para quê |
|---|---|
| **WhatsApp Business** | Atendimento e comunicação de trabalho |
| **YouTube** | Vídeos de treinamento e de fornecedores (versão grátis, com anúncios) |
| **Google Drive** | Abrir **PDF**, sem anúncios |
| **Google Planilhas** | Abrir **Excel** (.xlsx), sem anúncios |
| **Google Documentos** | Abrir **Word** (.docx), sem anúncios |
| **Google Apresentações** | Abrir **PowerPoint** (.pptx), sem anúncios |

Os apps do Google usam o Gmail da empresa do aparelho (§4.1). Qualquer outro app segue o POP-08.

### 4.3 Backup do WhatsApp

O WhatsApp é a principal ferramenta de trabalho, então as conversas precisam de backup:

1. WhatsApp → Configurações → Conversas → Backup → conta: o **Gmail da empresa do aparelho**.
2. Frequência: **diária**. **Sem vídeos** no backup.
3. Configurações → Armazenamento e dados → download automático de **vídeos desligado** (Wi-Fi e dados móveis).
4. Ligar o **backup com criptografia de ponta a ponta**. A senha vai para o Vaultwarden, no item do aparelho. **Sem essa senha ninguém restaura o backup.**
5. Todo mês a TI confere a data e o tamanho do último backup (POP-07). Se passar de **12 GB** (o limite grátis é 15 GB), limpar arquivos grandes antigos em "Gerenciar armazenamento".

O backup só restaura em aparelho com o **mesmo número**. Quando o aparelho troca de mãos, o histórico continua no Gmail da empresa.

---

## 5. Infraestrutura

### 5.1 Internet

| Link | Uso | IP |
|---|---|---|
| **Link empresarial** | Principal | IPv4 fixo |
| **Starlink** | Backup | Sem IP fixo |

O **OPNsense** troca para a Starlink automaticamente quando o link principal cai e volta sozinho quando ele normaliza (POP-10).

### 5.2 Servidor

- Roda no **PC de trabalho do Lui Grosz**, dentro da empresa, ligado 24h, com todos os serviços em **contêineres Docker**.
- Reinícios e manutenção **só fora do horário de trabalho**: se esse PC para, param juntos MeshCentral, Headwind, GLPI, Wazuh, Vaultwarden e backup.
- O PC também é usado no dia a dia, então: 2FA em todos os painéis, disco criptografado e atualizações em dia.
- O servidor é copiado toda noite para um **disco USB externo** da empresa (Restic).

### 5.3 O que fica exposto na internet

- **Só o MeshCentral** (porta 443, HTTPS), com 2FA.
- Todo o resto (GLPI, Wazuh, Vaultwarden, Headwind, UrBackup, Uptime Kuma) fica **só na rede interna**. De fora, acessar pela **VPN WireGuard** do OPNsense.
- Durante uma queda do link principal, a rede interna funciona normalmente pela Starlink, mas **o acesso de fora fica indisponível** até o link voltar. Isso é aceito.

---

## 6. E-mail

| Empresa | Domínio | Hospedagem |
|---|---|---|
| Postos Vale da Serra | `@postosvaledaserra.com.br` | Ittek |
| Sertão Petróleo | `@sertaopetroleo.com.br` | Ittek |
| TRR Vale da Serra | `@trrvaledaserra.com.br` | Ittek |

Padrão de endereço `nome.sobrenome@`, assinatura em imagem padronizada feita pelo RH e foto do funcionário: ver [anexo: padrão de e-mail](anexos/padrao-email.md).

---

## 7. Responsáveis

| Papel | Pessoa |
|---|---|
| TI (todos os POPs) | Lui Grosz |
| RH (POP-01, POP-02 e POP-11) | Camila Faverao |
| Direção (incidentes com dados pessoais, POP-09) | Artur |

---

## 8. POPs

| # | POP |
|---|---|
| [POP-01](POPs/POP-01-entrada.md) | Entrada de funcionário |
| [POP-02](POPs/POP-02-saida.md) | Saída de funcionário |
| [POP-03](POPs/POP-03-celular-perdido.md) | Celular perdido ou roubado |
| [POP-04](POPs/POP-04-instalacao-linux.md) | Instalação padrão de computador Linux |
| [POP-05](POPs/POP-05-instalacao-windows.md) | Instalação padrão de computador Windows |
| [POP-06](POPs/POP-06-atualizacoes.md) | Atualizações mensais |
| [POP-07](POPs/POP-07-backup.md) | Backup e teste de restauração |
| [POP-08](POPs/POP-08-novo-app.md) | Solicitação de app novo |
| [POP-09](POPs/POP-09-incidente.md) | Incidente de segurança |
| [POP-10](POPs/POP-10-queda-link.md) | Queda do link principal |
| [POP-11](POPs/POP-11-funcionario-ativo.md) | Funcionário ativo (mudanças, revisão de acessos, troca de equipamento, afastamento) |

**Anexos:** [padrão de e-mail e assinatura](anexos/padrao-email.md) · [formulários A a D](anexos/formularios.md)

---

## 9. Ordem de implantação

1. Preparar o servidor no PC do Lui Grosz: Docker e disco USB para o Restic.
2. OPNsense: firewall, failover para a Starlink e VPN WireGuard.
3. Vaultwarden (o cofre precisa existir antes de criar as outras senhas).
4. MeshCentral, GLPI, Wazuh, UrBackup e Uptime Kuma.
5. Primeiro PC Linux pelo POP-04: conferir o acesso remoto do MeshCentral e do AnyDesk no Ubuntu 26.04. Depois, os demais PCs.
6. Headwind MDM e o primeiro celular: conferir todas as políticas do §4.2. Depois, os demais celulares.
