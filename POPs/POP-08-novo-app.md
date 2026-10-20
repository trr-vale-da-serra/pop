# POP-08: Solicitação de app novo (celular ou computador)

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Só entram nos equipamentos da empresa programas e apps **conferidos pela TI**. O funcionário não instala nada por conta própria (não tem permissão de administrador no PC, e o celular só aceita apps da lista aprovada).

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **Funcionário** | Abre o chamado no GLPI dizendo qual app e para quê |
| **TI** | Avalia, aprova ou recusa, instala e registra. **A decisão é só da TI** |

## 3. Passo a passo

1. **Funcionário** abre um chamado no GLPI: nome do app, em qual equipamento e para que vai usar no trabalho.
2. **TI** avalia:
   - Vem da loja oficial (Play Store, loja oficial do Linux, site oficial do fabricante)?
   - É gratuito ou a empresa já tem licença?
   - Que permissões pede (contatos, arquivos, câmera) e se fazem sentido para o uso?
   - Tem histórico de problema de segurança?
   - Já existe app aprovado que faz a mesma coisa?
3. **TI** responde no chamado: **aprovado** ou **recusado**, com o motivo, em até **3 dias úteis**.
4. Se aprovado:
   - **Celular:** incluir na lista de apps aprovados do MDM. Vale para todos os aparelhos daquele grupo.
   - **PC:** instalar pelo acesso remoto ou pela ferramenta de configuração em massa.
5. App pago: só depois que a compra for autorizada por quem paga.

## 4. App da própria empresa (APK no celular)

App feito pela empresa ou por fornecedor contratado, que não está na Play Store. É a **única exceção** ao bloqueio de APK do POP-TI §4.2: o funcionário continua sem poder instalar APK; quem instala é o MDM.

1. **Responsável pelo app** (setor ou fornecedor) entrega o APK no chamado do GLPI, com o número da versão e o que mudou.
2. **TI** confere:
   - O APK está **assinado com a chave da empresa**, a mesma das versões anteriores. A chave é da empresa e fica no cofre de senhas. Fornecedor que desenvolve o app usa essa chave ou entrega o código para a TI gerar o APK.
   - As permissões que o app pede fazem sentido para o uso (mesmos critérios do passo 2 da seção 3).
3. **TI** guarda o APK no servidor, na pasta `apps-empresa/<app>/<versão>/`, que entra no backup do servidor.
4. **TI** instala pelo MDM num **celular de teste** e confere que o app abre e faz o que deve.
5. **TI** libera pelo MDM para o grupo de aparelhos. A versão anterior fica guardada para voltar se der problema.

**Nunca:** mandar APK por WhatsApp, e-mail ou link para o funcionário instalar, nem liberar "fontes desconhecidas" no aparelho.

## 5. Lista de apps aprovados

Os **apps padrão** de todo celular estão no POP-TI §4.2 e não precisam de solicitação. Os programas de todo PC Linux estão no [anexo de ferramentas](../anexos/ferramentas.md) §4. A lista completa dos celulares fica no MDM. Na revisão semestral de acessos (POP-11), a TI remove o que ninguém usa mais.

## 6. Registro

Chamado no GLPI com a decisão e o motivo. App da empresa: também a versão liberada e a data.
