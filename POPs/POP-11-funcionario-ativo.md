# POP-11: Funcionário ativo (mudanças durante o contrato)

> **Versão:** 1.1 · **Data:** 16/10/2026 · **Responsáveis:** TI: Lui Grosz · RH: Camila Faverao
> Faz parte do [Plano de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Manter os acessos e equipamentos de quem já trabalha na empresa **iguais ao que a função atual precisa**: nem faltando, nem sobrando. Cobre três situações:

| Seção | Situação | Quem dispara |
|---|---|---|
| 3 | Mudança de função ou de posto/unidade | RH |
| 4 | Revisão periódica de acessos | TI (calendário) |
| 5 | Troca de equipamento | Funcionário, gestor ou TI |

**Férias, atestados e afastamentos são assunto só do RH:** não abrem chamado para a TI e não mudam acessos nem equipamentos. Se o afastamento virar desligamento, segue o POP-02.

## 2. Quem faz o quê

Mesma divisão do POP-01: **RH avisa, gestor aprova, TI executa e registra.**

---

## 3. Mudança de função ou de posto/unidade

**Regra principal:** primeiro **remove** o que a função antiga tinha e não é mais necessário, depois **libera** o que a função nova precisa. Ex.: gerente que vai do Posto A para o Posto B não pode continuar vendo o Posto A no Sistema VS.

1. **RH** abre o chamado no GLPI (Formulário A) com tipo **Mudança**: função/posto antigo, função/posto novo, data da mudança, gestor novo.
2. **Gestor novo** marca os acessos da função nova. **Gestor antigo** confirma o que deixa de ser necessário.
3. **TI**, na data da mudança:
   1. **Sistema VS:** trocar perfil e postos. Conferir logando com o usuário que o posto antigo **sumiu**.
   2. **Petroshow (ERP) / Sigest / Infinitum / Orion:** ajustar perfil; remover acesso à unidade antiga.
   3. **E-mail:** a conta continua a mesma. O **RH refaz a imagem de rodapé** com o cargo novo (e empresa, se mudou de empresa do grupo) e a TI troca a assinatura no mesmo dia.
   4. **Mudou de empresa do grupo:** criar conta no domínio novo e tratar a antiga como saída (POP-02, seção de e-mail).
   5. **WhatsApp:** sair dos grupos da função antiga; entrar nos da nova.
   6. **Equipamentos:** se mudou de unidade e o equipamento fica no local, seguir a seção 5 (troca).
4. Atualizar no GLPI o Formulário B (checklist de acessos): o que saiu e o que entrou, com data.

---

## 4. Revisão periódica de acessos

**Frequência:** a cada **6 meses** (abril e outubro).

1. **TI** gera a lista, por gestor, de cada pessoa da equipe com todos os acessos e equipamentos (Formulário B atualizado + GLPI).
2. **Gestor** marca para cada item: **mantém** ou **remove**. Prazo: 10 dias.
3. **TI** remove o que foi marcado e registra.
4. **TI** confere também:
   - Contas sem dono (pessoa que já saiu e ficou com acesso ativo): **bloquear na hora** e investigar como escapou do POP-02.
   - Contas compartilhadas (um login para várias pessoas): trocar por um usuário por pessoa sempre que o sistema permitir.
   - Equipamento no inventário com a pessoa errada ou sumido.
5. Guardar a lista assinada pelo gestor como registro da revisão.

---

## 5. Troca de equipamento

Vale para defeito, substituição por um mais novo, perda (ver também POP-03) ou mudança de unidade.

1. Abrir o chamado no GLPI (Formulário A, tipo **Troca de equipamento**) com o motivo.
2. **TI** prepara o equipamento novo (POP-04/05 para PC; Headwind MDM com as políticas decididas para celular).
3. **Antes de recolher o antigo:** copiar os dados de trabalho da pessoa para o novo (restaurando do **UrBackup**). Celular: o WhatsApp volta pelo backup do Gmail da empresa.
4. Entregar o novo e recolher o antigo **no mesmo momento**, com o **Formulário D: Termo de devolução** para o antigo e um novo **Formulário C** para o novo.
5. Equipamento antigo:
   - **Celular:** remover do Headwind MDM só **depois** do wipe e conferir que saiu do painel.
   - **PC:** apagar os dados antes de reaproveitar ou descartar.
   - Defeito: registrar no inventário como "em manutenção" ou "descartado".
6. Atualizar o inventário no **GLPI**: equipamento antigo e novo, quem está com cada um.

---

## 6. Registro

- Formulário A (chamado) de cada solicitação e Formulário B atualizado, no GLPI.
- Formulários C e D (papel) na pasta do funcionário no RH.
- Lista da revisão semestral assinada pelo gestor.
- Inventário no GLPI sempre atualizado.

## Perfis de acesso por cargo

> Mesma tabela em todos os POPs. As regras completas estão no [POP-01 §3](POP-01-entrada.md).

| Perfil | Cargos | O que a TI entrega | RH abre o chamado |
|---|---|---|---|
| **A: Sem acesso de TI** | Motorista, zelador, auxiliar de limpeza, mecânico, borracheiro | Nada. O chamado serve só para registrar a pessoa | Até o **dia do início** (pode começar no mesmo dia) |
| **B: Oficina** | Estoquista, documentação, compras | Celular corporativo, e-mail corporativo, Petroshow, Sigest, Infinitum e Sistema VS | **2 dias úteis antes** do início |
| **C: Escritório** | Administrativo, financeiro, comercial, RH/DP | Tudo do perfil B, Orion e computador | **3 dias úteis antes** do início |
| **D: Gestão** | Gerentes e supervisores | Tudo do perfil C | **3 dias úteis antes** do início |

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
