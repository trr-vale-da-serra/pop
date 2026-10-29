# POP-11: Funcionário ativo (mudanças durante o contrato)

> **Versão:** 1.2 · **Data:** 29/10/2026 · **Responsáveis:** TI: Lui Grosz · RH: Camila Faverao
> Faz parte do [Plano de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Manter os acessos e equipamentos de quem já trabalha na empresa **iguais ao que a função atual precisa**: nem faltando, nem sobrando. Cobre duas situações:

| Seção | Situação | Quem dispara |
|---|---|---|
| 3 | Revisão periódica de acessos | TI (calendário) |
| 4 | Troca de equipamento | Funcionário, gestor ou TI |

## 2. Quem faz o quê

Mesma divisão do POP-01: **RH avisa, gestor aprova, TI executa e registra.**


---

## 3. Revisão periódica de acessos

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

## 4. Troca de equipamento

Vale para defeito, substituição por um mais novo, perda (ver também POP-03) ou mudança de unidade.

1. Abrir o chamado no GLPI (Formulário A, tipo **Troca de equipamento**) com o motivo.
2. **TI** prepara o equipamento novo (POP-04/05 para PC; MDM com as políticas decididas para celular).
3. **Antes de recolher o antigo:** conferir que os arquivos de trabalho estão na **nuvem da empresa** e ligar as pastas da pessoa no PC novo. Celular: o WhatsApp volta pela cópia no servidor (POP-03, passo 9).
4. Entregar o novo e recolher o antigo **no mesmo momento**, com o **Formulário D: Termo de devolução** para o antigo e um novo **Formulário C** para o novo.
5. Equipamento antigo:
   - **Celular:** remover do MDM só **depois** do wipe e conferir que saiu do painel.
   - **PC:** apagar os dados antes de reaproveitar ou descartar.
   - Defeito: registrar no inventário como "em manutenção" ou "descartado".
6. Atualizar o inventário no **GLPI**: equipamento antigo e novo, quem está com cada um.
---
## 5. Registro

- Formulário A (chamado) de cada solicitação e Formulário B atualizado, no GLPI.
- Formulários C e D (papel) na pasta do funcionário no RH.
- Lista da revisão semestral assinada pelo gestor.
- Inventário no GLPI sempre atualizado.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
