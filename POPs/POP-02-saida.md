# POP-02: Saída de funcionário

> **Versão:** 0.1 (rascunho) · **Data:** 15/10/2026 · **Responsável:** _a definir_
> Faz parte do [Plano de POP de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Garantir que, quando alguém sai da empresa, **nenhum acesso continue ativo**, todos os equipamentos voltem e os dados de trabalho fiquem com a empresa.

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **RH/DP** | Dispara o POP: Formulário A com tipo **Saída** e a data/hora do desligamento |
| **Gestor** | Diz quem assume os e-mails, o WhatsApp e os arquivos da pessoa |
| **TI** | Bloqueia os acessos, recolhe e limpa os equipamentos, registra |

## 3. Quando

| Tipo de saída | Quando bloquear |
|---|---|
| Pedido de demissão ou fim de contrato | No fim do **último dia** de trabalho |
| Demissão pela empresa | **No mesmo horário** da comunicação ao funcionário |
| Justa causa ou suspeita de má-fé | **Antes** da comunicação ao funcionário |

O RH avisa a TI **com antecedência**. No caso de justa causa, o aviso é sigiloso: só RH, gestor e TI sabem.

## 4. Passo a passo

### 4.1 Antes do desligamento

1. **RH** preenche o Formulário A, tipo **Saída**: data e hora, tipo de saída, gestor.
2. **Gestor** informa: quem recebe os e-mails, quem fica com o WhatsApp corporativo, para onde vão os arquivos.
3. **TI** separa o Formulário B (checklist de acessos) da pessoa. Ele é a lista do que bloquear.
4. **TI** copia os arquivos de trabalho do PC _(ferramenta de backup em avaliação, ver POP-TI §3.5)_.

### 4.2 Bloqueio (no horário da tabela da seção 3)

Seguir o Formulário B item por item e marcar cada um como bloqueado, com data e hora:

5. **E-mail:**
   - Trocar a senha no painel da hospedagem (a pessoa perde o acesso na hora).
   - Desconectar as sessões abertas e remover o e-mail de celulares/Outlook, se o painel permitir.
   - Ativar resposta automática: "Fulano não faz mais parte da equipe. Para assuntos de <setor>, escreva para <e-mail do setor/gestor>".
   - Encaminhar para o gestor (ou para quem ele indicou) por **90 dias**.
   - Remover dos aliases de setor.
6. **Sistema VS:** desativar o usuário (não excluir: o histórico de quem fez o quê precisa continuar).
7. **ERP / Petroshow / Infinitum:** desativar os usuários (não excluir, pelo mesmo motivo).
8. **WhatsApp corporativo:** o número é da empresa. Recolher o aparelho, passar as conversas para quem assume e trocar o nome/foto do perfil.
9. **Grupos de WhatsApp pessoais de trabalho:** se a pessoa estava em grupos de trabalho com o número pessoal, removê-la.
10. **Senhas compartilhadas** que a pessoa conhecia (Wi-Fi, contas de setor, sistemas com login único): trocar. _(Cofre de senhas Vaultwarden em avaliação, ver POP-TI §3.6; ele facilita saber quem conhecia o quê.)_
11. **Acesso remoto:** remover a pessoa de qualquer ferramenta de acesso remoto e VPN _(ferramenta em avaliação: MeshCentral, ver POP-TI §3.1)_.

### 4.3 Equipamentos

12. Recolher todos os equipamentos do Formulário C (termo de responsabilidade) e conferir a lista item por item.
13. Preencher o **Formulário D: Termo de devolução**, assinado pelo funcionário e pela TI. Equipamento faltando ou danificado: registrar no termo e avisar o RH.
14. **Celular corporativo:** fazer o **wipe** pelo Android Enterprise. Se o aparelho não foi devolvido: **bloqueio remoto** na hora e seguir o POP-03.
15. **Computador:** depois da cópia dos arquivos (passo 4), apagar o usuário da pessoa ou reinstalar pela instalação padrão (POP-04/05) antes de passar para outra pessoa.
16. Atualizar o inventário: equipamento devolvido, "disponível" ou "em manutenção".

### 4.4 Depois da saída

17. **Após 90 dias:** desligar o encaminhamento e **excluir a conta de e-mail** (libera a licença na hospedagem). Antes, conferir com o gestor se ainda precisa de algo da caixa.
18. Arquivar os Formulários A, B (com os bloqueios marcados) e D na pasta do funcionário no RH.

## 5. Conferência

- No dia seguinte ao desligamento, a TI tenta logar (ou pede o relatório do sistema) e confirma que **nenhum** acesso do Formulário B continua ativo.
- A revisão semestral (POP-11 §4) procura contas que escaparam deste POP.
