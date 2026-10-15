# Anexo: Padrão de e-mail corporativo

> **Versão:** 0.1 (rascunho) · **Data:** 15/10/2026
> Usado pelos POP-01 (entrada), POP-11 (funcionário ativo) e POP-02 (saída).

## 1. Onde ficam as contas

O e-mail é o **da hospedagem do domínio** de cada empresa (painel tipo cPanel do provedor). Cada empresa do grupo tem o **seu próprio domínio**.

| Empresa do grupo | Domínio | Painel da hospedagem | Logo para a assinatura (URL) |
|---|---|---|---|
| _a preencher_ | `@_____.com.br` | _a preencher_ | _a preencher_ |
| _a preencher_ | `@_____.com.br` | _a preencher_ | _a preencher_ |
| _a preencher_ | `@_____.com.br` | _a preencher_ | _a preencher_ |

> Os dados de acesso aos painéis **não** entram neste arquivo. Ficam no cofre de senhas da TI.

## 2. Padrão de endereço

### Pessoas

`nome.sobrenome@<domínio-da-empresa>`

- Tudo minúsculo, sem acento, sem cedilha: `João Conceição` → `joao.conceicao@`.
- Nome composto: usar o primeiro nome e o **último** sobrenome: `Maria Clara de Souza Lima` → `maria.lima@`.
- Homônimo (endereço já existe ou existiu): acrescentar número: `joao.silva2@`. Nunca reaproveitar o endereço de quem saiu.
- Sem apelido, sem número de telefone, sem cargo no endereço da pessoa.

### Setores (aliases)

Endereços de setor **não** são de uma pessoa. Eles encaminham para quem atende o setor:

| Endereço | Uso |
|---|---|
| `financeiro@` | Contas a pagar/receber, cobrança |
| `vendas@` | Pedidos e comercial |
| `rh@` | RH/DP |
| `ti@` | Chamados de TI |
| `contato@` | Formulário do site, contato geral |

Lista completa e quem recebe cada alias: manter no Formulário B de cada pessoa e revisar no POP-11 §4.

## 3. Assinatura padrão

### Conteúdo (nesta ordem)

1. **Nome** (como a pessoa é chamada no trabalho: `João Silva`)
2. **Cargo** · **Empresa**
3. **Telefone/WhatsApp** corporativo
4. **Logo** da empresa

Nada além disso: sem frase motivacional, sem imagem de fundo, sem cores fora do padrão, sem foto.

### Regras

- Gerar sempre a partir do modelo [assinatura-modelo.html](assinatura-modelo.html). Não montar à mão.
- Logo **por link** (URL da imagem hospedada no site da empresa), não colado como imagem: imagem colada vira anexo em muitos programas.
- Telefone no formato `(DD) 9XXXX-XXXX`.
- Mudou de cargo ou de empresa: atualizar a assinatura no mesmo dia (POP-11 §3).

### Como gerar

1. Abrir uma cópia de `assinatura-modelo.html` no editor de texto.
2. Trocar os campos entre `{{ }}`: `{{NOME}}`, `{{CARGO}}`, `{{EMPRESA}}`, `{{TELEFONE}}`, `{{TELEFONE_LINK}}` (só números com DDI, ex.: `5532999998888`), `{{LOGO_URL}}`, `{{COR_EMPRESA}}`.
3. Abrir o arquivo no navegador e conferir.

### Como instalar

| Programa | Caminho |
|---|---|
| **Outlook clássico** (Windows) | Abrir o HTML no navegador → selecionar tudo (Ctrl+A) → copiar → Outlook: *Arquivo → Opções → Email → Assinaturas → Novo* → colar → definir como padrão para mensagens novas **e** respostas |
| **Novo Outlook / Outlook Web** | *Configurações → Contas → Assinaturas* → colar → definir como padrão |
| **Webmail Roundcube** (comum em cPanel) | *Configurações → Identidades* → escolher a identidade → ligar o editor HTML → colar → Salvar |
| **Celular** (Gmail/Outlook app) | Assinatura simples só em texto: `Nome · Cargo · Empresa · Telefone` |

Depois de instalar: mandar um e-mail de teste para um endereço externo e conferir se o logo aparece.
