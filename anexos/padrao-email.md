# Anexo: Padrão de e-mail corporativo

> **Versão:** 1.0 · **Data:** 15/10/2026
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

A assinatura de e-mail é **uma imagem padronizada**, feita pelo **RH** para cada funcionário a partir do modelo de rodapé da empresa.

### Conteúdo da imagem

1. **Foto** do funcionário, editada pelo RH (seção 4)
2. **Nome** (como a pessoa é chamada no trabalho: `João Silva`)
3. **Cargo** · **Empresa**
4. **Telefone** do celular corporativo, no formato `(DD) 9XXXX-XXXX`

Mesmo layout, fontes e cores para todos da mesma empresa. Nada além disso: sem frase motivacional, sem informação fora do modelo.

<div style="border: 1px dashed #999; padding: 14px; margin: 8px 0; color: #444; font-size: 9.5pt;"><b>[ foto ]</b> &nbsp; <b>João Silva</b> · Analista Financeiro · TRR Vale da Serra · (32) 99999-0000 &nbsp; <i>(exemplo de disposição; o visual final é o modelo do RH)</i></div>

### Regras

- Sempre a partir do **modelo de rodapé da empresa**. Não montar à mão.
- Arquivo **PNG**, com **600 px de largura**, nome `rodape-nome.sobrenome.png`. O RH guarda o arquivo na pasta do funcionário e envia para a TI.
- Mudou de cargo, de telefone ou de empresa: o RH refaz a imagem e a TI troca no mesmo dia (POP-11 §3).

### Como instalar (TI)

| Programa | Caminho |
|---|---|
| **Outlook clássico** (Windows) | *Arquivo → Opções → Email → Assinaturas → Novo* → botão de inserir imagem → escolher o PNG → definir como padrão para mensagens novas **e** respostas |
| **Novo Outlook / Outlook Web** | *Configurações → Contas → Assinaturas* → inserir imagem → definir como padrão |
| **Webmail Roundcube** (comum em cPanel) | *Configurações → Identidades* → escolher a identidade → ligar o editor HTML → inserir imagem → Salvar |
| **Celular** (Gmail/Outlook app) | Assinatura simples só em texto: `Nome · Cargo · Empresa · Telefone` |

Depois de instalar: mandar um e-mail de teste para um endereço externo e conferir como a assinatura aparece.

## 4. Foto do funcionário

A mesma foto vale para a **imagem de rodapé** e para a **foto de perfil** do e-mail.

1. **Quando:** na admissão (POP-01), antes do primeiro dia.
2. **Como tirar:** de frente, do peito para cima, fundo liso e claro, boa luz, sem óculos escuros nem boné. Pode ser com o celular da empresa.
3. **RH edita:** recorta no formato padrão, ajusta luz e fundo e monta a imagem de rodapé.
4. **RH envia para a TI:** a foto editada e o PNG do rodapé.
5. **Autorização:** o funcionário autoriza o uso da foto ao assinar o Formulário C. Na saída (POP-02), a foto sai do e-mail e da assinatura e não é mais usada.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
