# POP-01: Entrada de funcionário

> **Versão:** 1.1 · **Data:** 16/10/2026 · **Responsáveis:** TI: Lui Grosz · RH: Camila Faverao
> Faz parte do [Plano de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Garantir que todo funcionário novo comece a trabalhar no primeiro dia com **só os acessos e equipamentos que a função precisa**, todos registrados e com termo assinado.

Funcionários dos **postos** (frentista, caixa, chefe de pista, lubrificador) **não fazem parte** deste POP.

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **RH/DP** | Dispara o POP: abre o chamado **Solicitação de TI** no GLPI (Formulário A) |
| **Gestor** (do setor ou do posto) | Aprova a lista de acessos e equipamentos |
| **TI** | Cria as contas, prepara e entrega os equipamentos, registra tudo |
| **Funcionário** | Assina o termo de responsabilidade e recebe as senhas da TI |

## 3. Perfis de entrada e prazos

O **cargo** define o perfil. O perfil define o pacote padrão e com quanta antecedência o RH abre o chamado.

| Perfil | Cargos | O que a TI entrega | RH abre o chamado |
|---|---|---|---|
| **A: Sem acesso de TI** | Motorista, zelador, auxiliar de limpeza, mecânico, borracheiro | Nada. O chamado serve só para registrar a pessoa | Até o **dia do início** (pode começar no mesmo dia) |
| **B: Estoquista** | Estoquista | Celular corporativo, Petroshow, Sigest, Infinitum e Sistema VS | **2 dias úteis antes** do início |
| **C: Escritório** | Administrativo, financeiro, comercial, RH/DP, documentação, compras | E-mail corporativo, Sistema VS, ERP e computador | **3 dias úteis antes** do início |
| **D: Gestão** | Gerentes e supervisores | Tudo do perfil C + celular corporativo e WhatsApp corporativo | **3 dias úteis antes** do início |

Regras:

- **Todo funcionário tem chamado, inclusive o perfil A.** Sem ele a pessoa não fica registrada no GLPI, e a saída (POP-02) e as mudanças (POP-11) não têm de onde partir.
- **O gestor pode pedir mais que o pacote** do perfil (ex.: celular para um motorista). Vale o prazo do perfil que tem aquele item.
- Perfis B, C e D: tudo pronto **até o dia anterior** ao início. Se for preciso **comprar** computador ou celular, o prazo da compra não está incluído: a TI informa no chamado a data em que o equipamento fica pronto.
- Se a pessoa começar antes dos acessos ficarem prontos, ela **espera o acesso: nunca usa o login de um colega**.
- Cargo que não está na tabela: o gestor indica o perfil mais próximo no chamado e a TI confirma.

## 4. Passo a passo

### 4.1 Solicitação (RH)

1. Abrir no GLPI o chamado **Solicitação de TI** (Formulário A) com tipo **Entrada**: nome completo, empresa do grupo, cargo, setor, posto/unidade, gestor, data de início e **perfil de entrada** (seção 3), respeitando o prazo do perfil.
2. Incluir o gestor no chamado para aprovação.
   - **Foto:** pedir ao funcionário a foto no padrão de [anexos/padrao-email.md](../anexos/padrao-email.md) §4 (ou tirar na admissão). O RH edita, monta a imagem de rodapé e anexa as duas ao chamado para a TI.

### 4.2 Aprovação (gestor)

3. Conferir o perfil e marcar no chamado os acessos e equipamentos necessários (lista na seção 5). O pacote do perfil é o padrão; o que for além dele precisa de justificativa no chamado.
4. Para o **Sistema VS**, informar o **perfil** e **quais postos/unidades** a pessoa pode ver. Na dúvida, o mínimo: gerente de posto vê só o próprio posto.
5. **Aprovar o chamado** no GLPI.

### 4.3 Preparação (TI)

> **Perfil A:** a TI só cadastra a pessoa no GLPI, com o Formulário B sem acessos, e fecha o chamado. Os passos 6 a 17 não se aplicam.

6. **E-mail:** criar a conta no padrão de [anexos/padrao-email.md](../anexos/padrao-email.md) (`nome.sobrenome@<domínio-da-empresa>`), no painel da hospedagem da empresa correta. Senha forte gerada pelo Vaultwarden.
7. **Assinatura de e-mail:** receber do RH a **imagem de rodapé** (`rodape-nome.sobrenome.png`) e a foto editada (passo 2).
8. **Sistema VS:** criar o usuário com o perfil e os postos aprovados. Conferir logando com o usuário que ele **não** enxerga posto ou tela fora do aprovado.
9. **ERP / Petroshow / Sigest / Infinitum:** criar os usuários aprovados, com o perfil da função (nunca copiar o perfil de outra pessoa sem conferir).
10. **Computador** (se aprovado):
    - Preparar pela instalação padrão (POP-04 Linux ou POP-05 Windows).
    - Criar o usuário local da pessoa, **sem permissão de administrador**.
    - Registrar no **GLPI**: patrimônio, número de série, quem recebe.
11. **Celular** (se aprovado):
    - Registrar o aparelho no **Headwind MDM** (Android Enterprise).
    - Entrar com o **Gmail da empresa daquele aparelho** (`celularNN.<empresa>@gmail.com`, senha no Vaultwarden). Se o aparelho é novo, a TI cria a conta antes, com e-mail de recuperação `lui.grosz@trrvaledaserra.com.br` e telefone de recuperação do celular corporativo do Lui Grosz (POP-TI §4.1). O funcionário não usa Gmail pessoal no aparelho.
    - Conferir que o aparelho recebeu os **apps padrão** e todas as políticas do POP-TI §4.2 (bloqueio de apps, PIN, bloqueio de reset, bloqueio e wipe remotos, Wi-Fi, localização desativada).
12. **WhatsApp corporativo** (se aprovado): número da empresa no celular corporativo, nome no padrão da empresa e **foto de perfil** = a foto editada pelo RH, incluir nos grupos de trabalho aprovados. Configurar o **backup diário** no Gmail da empresa, sem vídeos e com criptografia (POP-TI §4.3).
13. Preencher no GLPI a ficha **Formulário B: Checklist de acessos** com cada conta criada (sistema, usuário, data, quem criou) e salvar cada senha no **Vaultwarden**, na pasta do funcionário.

### 4.4 Primeiro dia (TI + funcionário)

14. Entregar os equipamentos e o **Formulário C: Termo de responsabilidade** para assinatura (1 via com o funcionário, 1 na pasta do RH).
15. Entregar as senhas ao funcionário pessoalmente e acompanhar o primeiro login em cada sistema. **Todas as senhas da pessoa ficam no Vaultwarden** (pasta do funcionário). O funcionário **não troca** as senhas: se precisar trocar, pede à TI, que troca e atualiza o cofre.
16. Instalar a imagem de rodapé como assinatura no Outlook/webmail e colocar a foto de perfil no e-mail, se o programa permitir (passo a passo em [anexos/padrao-email.md](../anexos/padrao-email.md)).
17. Explicar as regras básicas: senha não se compartilha com colegas, não se troca sem a TI, aparelho perdido avisa a TI na hora (POP-03), app novo só via solicitação (POP-08).

## 5. Lista de acessos e equipamentos possíveis

| Item | Observação |
|---|---|
| E-mail corporativo | Padrão `nome.sobrenome@` do domínio da empresa |
| Sistema VS (site) | Perfil + postos/unidades permitidos |
| ERP / Petroshow / Sigest / Infinitum | Um usuário por pessoa, com perfil da função |
| Computador | Instalação padrão (POP-04/05) + GLPI |
| Celular corporativo | Headwind MDM + políticas decididas |
| WhatsApp corporativo | O número é da empresa, não da pessoa |

## 6. Registro

- Formulários A (chamado aprovado) e B (ficha de acessos) no GLPI.
- Formulário C (termo assinado) na pasta do funcionário no RH.
- Inventário no GLPI atualizado com o equipamento entregue.

## 7. Prazo e conferência

- Perfis B, C e D: tudo criado até o dia anterior ao início (seção 3).
- Perfil A: chamado aberto e fechado até o dia do início.
- Até o fim da **primeira semana**: o gestor confirma que nada está faltando e que não sobra acesso.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
