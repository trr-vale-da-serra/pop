# POP-01: Entrada de funcionário

> **Versão:** 0.1 (rascunho) · **Data:** 15/10/2026 · **Responsável:** _a definir_
> Faz parte do [Plano de POP de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Garantir que todo funcionário novo comece a trabalhar no primeiro dia com **só os acessos e equipamentos que a função precisa**, todos registrados e com termo assinado.

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **RH/DP** | Dispara o POP: preenche a **Solicitação de TI** (Formulário A) |
| **Gestor** (do setor ou do posto) | Aprova a lista de acessos e equipamentos |
| **TI** | Cria as contas, prepara e entrega os equipamentos, registra tudo |
| **Funcionário** | Assina o termo de responsabilidade e troca as senhas provisórias no primeiro acesso |

## 3. Quando

- RH envia a solicitação **no mínimo 3 dias úteis antes** da data de início.
- Tudo pronto **até o dia anterior** ao início.

## 4. Passo a passo

### 4.1 Solicitação (RH)

1. Preencher o **Formulário A: Solicitação de TI** com tipo **Entrada**: nome completo, empresa do grupo, cargo, setor, posto/unidade, gestor, data de início.
2. Enviar para a TI e para o gestor.

### 4.2 Aprovação (gestor)

3. Marcar no Formulário A os acessos e equipamentos necessários (lista na seção 5).
4. Para o **Sistema VS**, informar o **perfil** e **quais postos/unidades** a pessoa pode ver. Na dúvida, o mínimo: gerente de posto vê só o próprio posto.
5. Devolver o formulário aprovado para a TI.

### 4.3 Preparação (TI)

6. **E-mail:** criar a conta no padrão de [anexos/padrao-email.md](../anexos/padrao-email.md) (`nome.sobrenome@<domínio-da-empresa>`), no painel da hospedagem da empresa correta. Senha provisória.
7. **Assinatura de e-mail:** gerar a assinatura a partir de [anexos/assinatura-modelo.html](../anexos/assinatura-modelo.html) com nome, cargo, empresa e telefone/WhatsApp.
8. **Grupos/aliases de setor:** incluir o e-mail novo nos endereços do setor (ex.: `financeiro@`), se aprovado.
9. **Sistema VS:** criar o usuário com o perfil e os postos aprovados. Conferir logando com o usuário que ele **não** enxerga posto ou tela fora do aprovado.
10. **ERP / Petroshow / Infinitum:** criar os usuários aprovados, com o perfil da função (nunca copiar o perfil de outra pessoa sem conferir).
11. **Computador** (se aprovado):
    - Preparar pela instalação padrão (POP-04 Linux ou POP-05 Windows).
    - Criar o usuário local/de domínio da pessoa.
    - Registrar no inventário: patrimônio, número de série, quem recebe _(ferramenta de inventário em avaliação: GLPI/Snipe-IT, ver POP-TI §3.3; até decidir, registrar no Formulário C)_.
12. **Celular** (se aprovado):
    - Registrar o aparelho no **Android Enterprise**.
    - Aplicar as políticas já decididas: **bloqueio de apps** (só os aprovados via Play Store gerenciada), **bloqueio remoto** ativo e **depuração USB/Opções do desenvolvedor desativadas**.
    - Recomendado (POP-TI §4.2, ainda não decidido): PIN forte, bloqueio de restauração de fábrica, bloqueio de APK de fonte desconhecida.
    - Se a localização do aparelho estiver ativa, o funcionário assina a **ciência por escrito** (Formulário E, LGPD).
13. **WhatsApp corporativo** (se aprovado): número da empresa no celular corporativo, nome/foto do perfil no padrão da empresa, incluir nos grupos de trabalho aprovados.
14. Preencher o **Formulário B: Checklist de acessos** com cada conta criada (sistema, usuário, data, quem criou).

### 4.4 Primeiro dia (TI + funcionário)

15. Entregar os equipamentos e o **Formulário C: Termo de responsabilidade** para assinatura (1 via com o funcionário, 1 na pasta do RH).
16. Acompanhar o primeiro login em cada sistema; o funcionário **troca todas as senhas provisórias** na hora.
17. Configurar a assinatura de e-mail no Outlook/webmail (passo a passo em [anexos/padrao-email.md](../anexos/padrao-email.md)).
18. Explicar as regras básicas: senha não se compartilha, aparelho perdido avisa a TI na hora (POP-03), app novo só via solicitação (POP-08).

## 5. Lista de acessos e equipamentos possíveis

| Item | Observação |
|---|---|
| E-mail corporativo | Padrão `nome.sobrenome@` do domínio da empresa |
| Alias de setor | Ex.: `financeiro@`, `vendas@` |
| Sistema VS (site) | Perfil + postos/unidades permitidos |
| ERP / Petroshow / Infinitum | Um usuário por pessoa, com perfil da função |
| Computador | Instalação padrão + inventário |
| Celular corporativo | Android Enterprise + políticas decididas |
| WhatsApp corporativo | O número é da empresa, não da pessoa |

## 6. Registro

- Formulário A (aprovado), B (checklist) e C (termo assinado) na pasta do funcionário no RH.
- Inventário atualizado com o equipamento entregue.

## 7. Prazo e conferência

- Tudo criado até o dia anterior ao início.
- Até o fim da **primeira semana**: o gestor confirma que nada está faltando e que não sobra acesso.
