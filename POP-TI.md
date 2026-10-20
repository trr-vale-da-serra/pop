# Plano de TI: Gestão de Computadores e Celulares

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** Lui Grosz (TI)
> Empresas: Postos Vale da Serra, Sertão Petróleo e TRR Vale da Serra.
> **Regra geral:** todas as ferramentas são **gratuitas** (licença grátis ou open source, sem mensalidade).
> **Regra de equipamento:** nenhum serviço ou dado da empresa roda em equipamento que não seja da empresa.

---

## 1. Objetivo

Padronizar como a TI controla, protege e dá suporte aos equipamentos da empresa:

- **Computadores:** Linux (padrão) e Windows (só onde algum programa exige).
- **Celulares** corporativos Android.

---

## 2. Ferramentas

Os POPs falam da **função** de cada ferramenta (ex.: "cofre de senhas", "acesso remoto"), não do programa, porque os programas mudam. **Qual programa faz cada função está em um só lugar: [anexo: ferramentas atuais](anexos/ferramentas.md).** A exceção é o **GLPI**, citado pelo nome.

| Função | Para quê |
|---|---|
| **Chamados, inventário e patrimônio (GLPI)** | Inventário automático, chamados de TI e quem está com cada equipamento |
| **Acesso remoto** | Tela, terminal e arquivos de qualquer PC, Windows ou Linux, pelo navegador |
| **Programa de suporte de fornecedor** | Só para fornecedores externos, com regras (§3.2) |
| **Configuração em massa** | Instala programas e aplica configurações em vários PCs de uma vez, por roteiros de configuração |
| **Painel de segurança** | Painel central de alertas de segurança de todas as máquinas |
| **Antivírus** | Em cada máquina, com alertas enviados ao painel de segurança |
| **Monitoramento** | Avisa quando o link, o servidor ou um serviço cai |
| **Backup dos PCs** | Backup central de todos os PCs no servidor |
| **Backup do servidor** | Cópia do próprio servidor para um disco USB externo |
| **Cofre de senhas** | Guarda **todas** as senhas: da empresa e de cada funcionário |
| **Firewall** | Firewall, VPN e troca automática para o link reserva |
| **MDM dos celulares** | Políticas, bloqueio de apps, bloqueio e limpeza remotos |

Não há domínio (Active Directory). As configurações dos PCs são aplicadas pela ferramenta de configuração em massa.

---

## 3. Computadores

### 3.1 Sistema padrão

- **Linux (padrão):** a distribuição e a versão padrão estão no [anexo de ferramentas](anexos/ferramentas.md) §2, com a tela ajustada para ficar parecida com o Windows (barra de tarefas embaixo e menu Iniciar). Instalação no POP-04.
- **Windows:** fica só nos PCs que usam programas que não rodam no Linux (ex.: alguns sistemas de banco ou fornecedores). Instalação no POP-05.
- **Nome dos computadores:** `<EMPRESA>-PC-<patrimônio>`, com `POSTOS`, `SERTAO` ou `TRR` no lugar de `<EMPRESA>` (ex.: `TRR-PC-0012`).
- **Usuários:** cada pessoa tem um usuário **sem permissão de administrador** e **sem senha**. A tela de login não aceita colar senha, então senha em todos os PCs não é prático.
  - **Exceção:** no PC do **gestor de cada departamento**, o gestor pode ter senha, **escolhida por ele**. Essa senha não vai para o cofre. Se ele esquecer, a TI troca pela conta administradora.
  - A TI tem uma conta administradora separada, **com senha**, guardada no cofre de senhas.
- **Terminal:** o funcionário **nunca** precisa abrir o terminal. Tudo o que ele faz no PC é pelas telas gráficas. Comandos ficam só com a TI.

### 3.2 Acesso remoto

**TI:** sempre pela **ferramenta de acesso remoto**, com 2FA ligado para todos os usuários do painel.

**Fornecedores (programa de suporte de fornecedor):**

1. Só quando **a empresa chamou o fornecedor**. Nunca para quem ligou oferecendo suporte.
2. Sempre **assistido**: alguém no PC aceita a conexão e acompanha. **Nunca** configurar senha de acesso autônomo.
3. Cada acesso é registrado num **chamado do GLPI**: fornecedor, data, motivo e quem acompanhou.
4. O programa de suporte de fornecedor fica instalado só nos PCs que recebem suporte de fornecedor.

### 3.3 Segurança

- **Antivírus:** em todo PC, Windows e Linux, enviando alertas ao painel de segurança.
- **Painel de segurança:** a TI olha o painel **toda semana** e trata os alertas críticos no mesmo dia (POP-09).
- **Criptografia de disco:** **não é usada**, nem nos PCs nem no servidor. Se o Windows ligar a criptografia sozinho na instalação, desligar (POP-05).
- **Senhas:** **todas** as senhas ficam no cofre de senhas, inclusive as pessoais de cada funcionário (e-mail, Sistema VS, Petroshow, Infinitum, Orion), numa pasta por funcionário. Só a TI acessa o cofre, com 2FA. A TI gera senhas fortes e entrega pessoalmente. O funcionário **não troca** senha sozinho: pede à TI, que troca e atualiza o cofre. O usuário do PC não tem senha (§3.1). A senha que o gestor escolhe para o próprio PC é a única que não vai para o cofre.
- **Monitoramento:** vigia o link principal, o link reserva, o servidor e cada serviço. Os alertas vão para o e-mail da TI.

### 3.4 Atualizações

- **Linux:** atualizações de segurança automáticas todos os dias.
- **Mensal (Windows e Linux):** na **2ª quarta-feira de cada mês, depois do expediente**, a ferramenta de configuração em massa força as atualizações pendentes nos PCs ligados e reinicia o que precisar. PC desligado ou fora da empresa é atualizado quando voltar à rede: ninguém precisa deixar o PC ligado. Detalhes no POP-06.

### 3.5 Backup

| O quê | Como | Frequência | Guarda |
|---|---|---|---|
| Arquivos dos PCs | Backup dos PCs | Toda noite | 30 dias |
| Imagem completa do disco dos PCs | Backup dos PCs | Toda semana | 4 imagens |
| Servidor inteiro (serviços, cofre, backups) | Backup do servidor, para disco USB externo | Toda noite | 30 dias |
| WhatsApp dos celulares | Google Drive do Gmail do aparelho (§4.3) | Todo dia | Último backup |
| Caixa de e-mail de quem saiu | Download por IMAP para o servidor (POP-02) | Na saída | **Permanente** |

**Teste de restauração todo mês** (POP-07). Backup que nunca foi testado não conta como backup.

---

## 4. Celulares (Android)

### 4.1 Conta Google

- A TI cria **um Gmail por celular**: `celularNN.<empresa>@gmail.com` (ex.: `celular01.trrvaledaserra@gmail.com`). A senha e o 2FA ficam no **cofre de senhas**.
- A conta fica com o **aparelho**, não com a pessoa. O funcionário **nunca** entra com o Gmail pessoal no aparelho da empresa.
- Assim a proteção contra restauração de fábrica (FRP) fica sempre com a empresa: depois de um reset ou wipe, a TI desbloqueia o aparelho com essa conta.
- **E-mail de recuperação:** `lui.grosz@trrvaledaserra.com.br` (responsável de TI).
- **Telefone de recuperação:** celular corporativo do responsável de TI (Lui Grosz). Nunca número pessoal, nunca o chip do próprio aparelho.
- Se o responsável de TI mudar, trocar o e-mail e o telefone de recuperação de todas as contas (POP-02).
- O Google limita quantas contas um mesmo número pode verificar. Se travar, verificar a conta na criação com o chip do próprio aparelho e manter o número da TI só como recuperação.

### 4.2 Políticas do MDM

Todo celular corporativo é registrado no MDM (aparelho zerado) e recebe:

| Política | Regra |
|---|---|
| Bloqueio de apps | Só apps da lista aprovada pela TI (POP-08) |
| Apps de fora da loja (APK) | Bloqueados para o usuário. **Exceção:** apps da própria empresa, instalados só pelo MDM (POP-08 §4) |
| Senha | PIN de no mínimo 6 dígitos, bloqueio de tela automático em 2 minutos |
| Restauração de fábrica pelo usuário | Bloqueada |
| Depuração USB e Opções do desenvolvedor | Bloqueadas |
| Bloqueio remoto | Ativo |
| Limpeza remota (wipe) | Ativa |
| Wi-Fi da empresa | Enviado automaticamente (o funcionário não sabe a senha) |
| Atualização do sistema | Automática, em janela noturna |
| Localização | **Desativada.** A empresa não registra nem consulta a localização dos aparelhos |

Só aparelhos da empresa. **Celular pessoal não é gerenciado** e não recebe dados da empresa.

**Apps padrão** (instalados em todo celular corporativo pelo MDM):

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
4. Ligar o **backup com criptografia de ponta a ponta**. A senha vai para o cofre de senhas, no item do aparelho. **Sem essa senha ninguém restaura o backup.**
5. Todo mês a TI confere a data e o tamanho do último backup (POP-07). Se passar de **12 GB** (o limite grátis é 15 GB), limpar arquivos grandes antigos em "Gerenciar armazenamento".

O backup só restaura em aparelho com o **mesmo número**. Quando o aparelho troca de mãos, o histórico continua no Gmail da empresa.

---

## 5. Infraestrutura

### 5.1 Internet

| Link | Uso | IP |
|---|---|---|
| **Link empresarial** | Principal | IPv4 fixo |
| **Link reserva** | Backup | Sem IP fixo |

O **firewall** troca para o link reserva automaticamente quando o link principal cai e volta sozinho quando ele normaliza (POP-10).

### 5.2 Servidor

- Roda no **PC de trabalho do Lui Grosz**, dentro da empresa, ligado 24h, com todos os serviços em **contêineres**.
- Reinícios e manutenção **só fora do horário de trabalho**: se esse PC para, param juntos o acesso remoto, o MDM, o GLPI, o painel de segurança, o cofre de senhas e o backup.
- O PC também é usado no dia a dia, então: 2FA em todos os painéis e atualizações em dia.
- O servidor é copiado toda noite para um **disco USB externo** da empresa (backup do servidor).

### 5.3 O que fica exposto na internet

- **Só o acesso remoto** (HTTPS), com 2FA.
- Todo o resto (GLPI, painel de segurança, cofre de senhas, MDM, backup, monitoramento) fica **só na rede interna**. De fora, acessar pela **VPN** do firewall.
- Durante uma queda do link principal, a rede interna funciona normalmente pelo link reserva, mas **o acesso de fora fica indisponível** até o link voltar. Isso é aceito.

---

## 6. E-mail

| Empresa | Domínio |
|---|---|
| Postos Vale da Serra | `@postosvaledaserra.com.br` |
| Sertão Petróleo | `@sertaopetroleo.com.br` |
| TRR Vale da Serra | `@trrvaledaserra.com.br` |

As três ficam na mesma hospedagem (ver [anexo de ferramentas](anexos/ferramentas.md)).

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
| [POP-11](POPs/POP-11-funcionario-ativo.md) | Funcionário ativo (revisão de acessos e troca de equipamento) |

**Anexos:** [ferramentas atuais](anexos/ferramentas.md) · [padrão de e-mail e assinatura](anexos/padrao-email.md) · [formulários A a D](anexos/formularios.md)

---

## 9. Ordem de implantação

1. Preparar o servidor no PC do Lui Grosz: contêineres e disco USB para o backup do servidor.
2. Firewall: troca automática para o link reserva e VPN.
3. Cofre de senhas (precisa existir antes de criar as outras senhas).
4. Acesso remoto, GLPI, painel de segurança, backup dos PCs e monitoramento.
5. Primeiro PC Linux pelo POP-04: conferir a ferramenta de acesso remoto e o programa de suporte de fornecedor no Linux padrão. Depois, os demais PCs.
6. MDM e o primeiro celular: conferir todas as políticas do §4.2. Depois, os demais celulares.
