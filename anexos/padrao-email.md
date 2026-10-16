# Anexo: Padrão de e-mail corporativo

> **Versão:** 1.1 · **Data:** 16/10/2026
> Usado pelos POP-01 (entrada), POP-11 (funcionário ativo) e POP-02 (saída).

## 1. Onde ficam as contas

O e-mail é o **da hospedagem do domínio** de cada empresa (painel tipo cPanel do provedor). Cada empresa do grupo tem o **seu próprio domínio**.

| Empresa do grupo | Domínio | Hospedagem |
|---|---|---|
| Postos Vale da Serra | `@postosvaledaserra.com.br` | Ittek |
| Sertão Petróleo | `@sertaopetroleo.com.br` | Ittek |
| TRR Vale da Serra | `@trrvaledaserra.com.br` | Ittek |

> Os dados de acesso aos painéis **não** entram neste arquivo. Ficam no cofre de senhas da TI.

## 2. Padrão de endereço

`nome.sobrenome@<domínio-da-empresa>`

- Tudo minúsculo, sem acento, sem cedilha: `João Conceição` → `joao.conceicao@`.
- Nome composto: usar o primeiro nome e o **último** sobrenome: `Maria Clara de Souza Lima` → `maria.lima@`.
- Homônimo (endereço já existe ou existiu): acrescentar número: `joao.silva2@`. Nunca reaproveitar o endereço de quem saiu.
- Sem apelido, sem número de telefone, sem cargo no endereço da pessoa.

## 3. Assinatura padrão (imagem de rodapé)

A assinatura de e-mail é **uma imagem feita pelo RH**. A foto do funcionário, o conteúdo, o layout e a autorização de uso da foto são **assunto só do RH**.

### O que a TI recebe do RH

- A imagem de rodapé em **PNG**, com **600 px de largura**, nome `rodape-nome.sobrenome.png`.
- A foto já editada, para a foto de perfil do e-mail (se o programa permitir).
- Mudou de cargo, de telefone ou de empresa: o RH refaz a imagem e a TI troca no mesmo dia (POP-11 §3).
- Na saída (POP-02), a TI tira a imagem e a foto do e-mail.

### Como instalar (TI)

| Programa | Caminho |
|---|---|
| **Outlook clássico** (Windows) | *Arquivo → Opções → Email → Assinaturas → Novo* → botão de inserir imagem → escolher o PNG → definir como padrão para mensagens novas **e** respostas |
| **Novo Outlook / Outlook Web** | *Configurações → Contas → Assinaturas* → inserir imagem → definir como padrão |
| **Webmail Roundcube** (comum em cPanel) | *Configurações → Identidades* → escolher a identidade → ligar o editor HTML → inserir imagem → Salvar |
| **Celular** (Gmail/Outlook app) | Assinatura simples só em texto: `Nome · Cargo · Empresa · Telefone` |

Depois de instalar: mandar um e-mail de teste para um endereço externo e conferir como a assinatura aparece.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
