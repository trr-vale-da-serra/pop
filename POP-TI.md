# Plano de TI: Gestão de Computadores e Celulares

> **Versão:** 1.4 · **Data:** 29/10/2026 · **Responsável:** Lui Grosz (TI)
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
| **Antivírus** | Em cada máquina, com os alertas na própria máquina |
| **Monitoramento** | Avisa quando o link, o servidor ou um serviço cai |
| **Nuvem da empresa** | Pasta pessoal de cada funcionário e pasta de cada departamento, no servidor. É o único lugar dos arquivos de trabalho |
| **Backup do servidor** | Espelho de discos com snapshots, e cópia dos bancos e da VM dos sistemas para um disco só de backup |
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
- **Usuários:** todo PC tem a mesma **conta dos funcionários** (`usuario`), **com permissão de administrador** e **sem senha**. Não há uma conta por pessoa. A instalação padrão já cria essa conta (POP-04/05). A tela de login não aceita colar senha, então senha em todos os PCs não é prático.
  - **Exceção:** no PC do **gestor de cada departamento**, o gestor pode pôr senha na conta dos funcionários daquele PC, **escolhida por ele**. Essa senha não vai para o cofre. Se ele esquecer, a TI troca pela conta administradora da TI.
  - A TI tem uma conta administradora separada, **com senha**, guardada no cofre de senhas.
  - **Contra (aceito):** não dá para saber quem fez o quê no PC, e qualquer pessoa no PC consegue instalar programas e mudar configurações. Instalar programa continua dependendo da TI (POP-08), mas como regra, não como bloqueio.
- **Terminal:** o funcionário **nunca** precisa abrir o terminal. Tudo o que ele faz no PC é pelas telas gráficas. Comandos ficam só com a TI.

### 3.2 Acesso remoto

**TI:** sempre pela **ferramenta de acesso remoto**, com 2FA ligado para todos os usuários do painel.

**Fornecedores (programa de suporte de fornecedor):**

1. Só quando **a empresa chamou o fornecedor**. Nunca para quem ligou oferecendo suporte.
2. Sempre **assistido**: alguém no PC aceita a conexão e acompanha. **Nunca** configurar senha de acesso autônomo.
3. Cada acesso é registrado num **chamado do GLPI**: fornecedor, data, motivo e quem acompanhou.
4. O programa de suporte de fornecedor fica instalado em **todo PC Windows**. No Linux, só nos PCs que recebem suporte de fornecedor.

### 3.3 Segurança

- **Antivírus:** em todo PC, Windows e Linux. Vírus encontrado é incidente: tratar no mesmo dia (POP-09).
- **Criptografia de disco:** **não é usada**, nem nos PCs nem no servidor. Se o Windows ligar a criptografia sozinho na instalação, desligar (POP-05).
- **Senhas:** **todas** as senhas ficam no cofre de senhas, inclusive as pessoais de cada funcionário (e-mail, Sistema VS, Petroshow, Infinitum, Orion), numa pasta por funcionário. Só a TI acessa o cofre, com 2FA. A TI gera senhas fortes e entrega pessoalmente. O funcionário **não troca** senha sozinho: pede à TI, que troca e atualiza o cofre. O usuário do PC não tem senha (§3.1). A senha que o gestor escolhe para o próprio PC é a única que não vai para o cofre.
- **Monitoramento:** vigia o link principal, o link reserva, o servidor e cada serviço. Os alertas vão para o e-mail da TI.

### 3.4 Atualizações

- **Linux:** atualizações de segurança automáticas todos os dias.
- **Mensal (Windows e Linux):** na **2ª quarta-feira de cada mês, depois do expediente**, a ferramenta de configuração em massa força as atualizações pendentes nos PCs ligados e reinicia o que precisar. PC desligado ou fora da empresa é atualizado quando voltar à rede: ninguém precisa deixar o PC ligado. Detalhes no POP-06.

### 3.5 Backup

Os **PCs não têm backup**. Os arquivos de trabalho ficam só na **nuvem da empresa** (pasta pessoal e pasta do departamento). PC com defeito é reinstalado (POP-04/05) e as pastas são ligadas de novo. **Arquivo salvo fora da nuvem da empresa não tem backup**: a regra é explicada na entrada (POP-01).

| O quê | Como | Frequência | Guarda |
|---|---|---|---|
| Arquivos da empresa (nuvem da empresa) | Espelho de discos com snapshots | A cada hora, dia e mês | 24 horas, 30 dias, 6 meses |
| Bancos dos sistemas | Cópia para o disco de backup | Toda noite | 30 dias |
| VM dos sistemas | Cópia para o disco de backup | Toda semana | 2 cópias |
| WhatsApp dos celulares | Backup local do aparelho, copiado para o servidor (§4.3) | Todo dia | Último backup + snapshots |
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
| **Syncthing** | Envia o backup do WhatsApp para o servidor (§4.3). Só a TI mexe |

Os apps do Google usam o Gmail da empresa do aparelho (§4.1). Qualquer outro app segue o POP-08.

### 4.3 Backup do WhatsApp

O WhatsApp é a principal ferramenta de trabalho, então as conversas precisam de backup. O backup fica **no servidor da empresa**, não no Google Drive:

1. WhatsApp → Configurações → Conversas → Backup → Fazer backup no Google Drive: **Nunca**. O WhatsApp continua fazendo sozinho, toda madrugada, o **backup local** no próprio celular.
2. Configurações → Armazenamento e dados → download automático de **vídeos desligado** (Wi-Fi e dados móveis).
3. Ligar o **backup com criptografia de ponta a ponta**. A senha vai para o cofre de senhas, no item do aparelho. **Sem essa senha ninguém restaura o backup.**
4. O MDM instala o **Syncthing**. A TI liga nele a pasta do WhatsApp do aparelho (`Android/media/com.whatsapp.w4b/WhatsApp`) **só para enviar**, sem a pasta de vídeos, para o servidor, que guarda em `/dados/whatsapp/<aparelho>`. O envio acontece sozinho quando o celular está na rede da empresa.
5. Todo mês a TI confere que a cópia de cada aparelho no servidor é de ontem ou hoje (POP-07).

**Restaurar** (aparelho novo, mesmo número): **antes de abrir o WhatsApp**, copiar a pasta do servidor para `Android/media/com.whatsapp.w4b/WhatsApp` no aparelho novo. Depois entrar com o número e escolher restaurar o backup (pede a senha do cofre). O backup só restaura em aparelho com o **mesmo número**.

---

## 5. Infraestrutura

### 5.1 Internet

| Link | Uso | IP |
|---|---|---|
| **Link empresarial** | Principal | IPv4 fixo |
| **Link reserva** | Backup | Sem IP fixo |

O **firewall** troca para o link reserva automaticamente quando o link principal cai e volta sozinho quando ele normaliza.

### 5.2 Servidor

- Roda num **PC Ubuntu da empresa**, dentro da empresa, ligado 24h. Os sistemas da empresa ficam numa máquina virtual, e os serviços da TI em **contêineres**.
- Discos: uma **gaveta USB-C com 3 discos de 4 TB**. Dois formam um **espelho** (se um disco morre, nada se perde), com a nuvem da empresa, o WhatsApp e as pastas do servidor, e snapshots a cada hora. O terceiro é **só para backup** (bancos toda noite, VM toda semana), sem criptografia, e fica desmontado fora da hora do backup.
- Reinícios e manutenção **só fora do horário de trabalho**: se esse PC para, param juntos o acesso remoto, o MDM, o GLPI, o cofre de senhas e o backup.
- O PC também é usado no dia a dia, então: 2FA em todos os painéis e atualizações em dia.

### 5.3 O que fica exposto na internet

- **Só o acesso remoto** (HTTPS), com 2FA, pelo **túnel da Cloudflare**: nenhuma porta aberta no firewall. Funciona também para as outras bases e notebooks fora da empresa.
- Todo o resto (GLPI, cofre de senhas, MDM, backup, monitoramento) fica **só na rede interna**. De fora, acessar pela **VPN** do firewall.
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
| [POP-11](POPs/POP-11-funcionario-ativo.md) | Funcionário ativo (revisão de acessos e troca de equipamento) |

**Anexos:** [ferramentas atuais](anexos/ferramentas.md) · [padrão de e-mail e assinatura](anexos/padrao-email.md) · [formulários A a D](anexos/formularios.md)

---

## 9. Ordem de implantação

1. Preparar o servidor: contêineres, gaveta de discos (espelho e disco de backup), nuvem da empresa e backup dos celulares.
2. Firewall: troca automática para o link reserva e VPN.
3. Cofre de senhas (precisa existir antes de criar as outras senhas).
4. Acesso remoto, GLPI e monitoramento.
5. Primeiro PC Linux pelo POP-04: conferir a ferramenta de acesso remoto e o programa de suporte de fornecedor no Linux padrão. Depois, os demais PCs.
6. MDM e o primeiro celular: conferir todas as políticas do §4.2. Depois, os demais celulares.
