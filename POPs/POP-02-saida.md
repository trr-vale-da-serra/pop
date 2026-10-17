# POP-02: Saída de funcionário

> **Versão:** 1.1 · **Data:** 17/10/2026 · **Responsáveis:** TI: Lui Grosz · RH: Camila Faverao
> Faz parte do [Plano de TI](../POP-TI.md). Formulários em [anexos/formularios.md](../anexos/formularios.md).

## 1. Objetivo

Garantir que, quando alguém sai da empresa, **nenhum acesso continue ativo**, todos os equipamentos voltem e os dados de trabalho fiquem com a empresa.

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **RH/DP** | Dispara o POP: chamado no GLPI (Formulário A) com tipo **Saída** e a data/hora do desligamento |
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

1. **RH** abre o chamado no GLPI (Formulário A), tipo **Saída**: data e hora, tipo de saída, gestor.
2. **Gestor** informa: quem recebe os e-mails, quem fica com o WhatsApp corporativo, para onde vão os arquivos.
3. **TI** abre no GLPI o Formulário B (checklist de acessos) da pessoa. Ele é a lista do que bloquear.
4. **TI** confere que o PC tem backup recente no **backup dos PCs** e copia os arquivos de trabalho para quem assume.

### 4.2 Bloqueio (no horário da tabela da seção 3)

Seguir o Formulário B item por item e marcar cada um como bloqueado no GLPI, com data e hora:

5. **E-mail:**
   - Trocar a senha no painel da hospedagem (a pessoa perde o acesso na hora) e atualizar no cofre de senhas.
   - Desconectar as sessões abertas e remover o e-mail de celulares/Outlook, se o painel permitir.
   - Ativar resposta automática: "Fulano não faz mais parte da equipe. Para assuntos de <setor>, escreva para <e-mail do gestor>".
   - Encaminhar para o gestor (ou para quem ele indicou) por **90 dias**.
6. **Sistema VS:** desativar o usuário (não excluir: o histórico de quem fez o quê precisa continuar).
7. **ERP / Petroshow / Infinitum:** desativar os usuários (não excluir, pelo mesmo motivo).
8. **WhatsApp corporativo:** o número é da empresa. Conferir que o backup do dia foi feito (POP-TI §4.3), recolher o aparelho, passar o atendimento para quem assume e trocar o nome/foto do perfil.
9. **Grupos de WhatsApp pessoais de trabalho:** se a pessoa estava em grupos de trabalho com o número pessoal, removê-la.
10. **Senhas compartilhadas** que a pessoa conhecia (Wi-Fi, contas de setor, sistemas com login único): trocar. Atualizar as senhas novas no cofre de senhas.
11. **Acesso remoto:** remover a pessoa da **ferramenta de acesso remoto** e da **VPN**, se tinha acesso.

### 4.3 Equipamentos

12. Recolher todos os equipamentos do Formulário C (termo de responsabilidade) e conferir a lista item por item.
13. Preencher o **Formulário D: Termo de devolução**, assinado pelo funcionário e pela TI. Equipamento faltando ou danificado: registrar no termo e avisar o RH.
14. **Celular corporativo:** fazer o **wipe** pelo MDM. Depois do wipe, desbloquear com o Gmail da empresa do aparelho (FRP) e trocar a senha dessa conta no cofre de senhas antes de entregar o aparelho a outra pessoa. Se o aparelho não foi devolvido: **bloqueio remoto** na hora e seguir o POP-03.
    - **Se quem sai é o responsável de TI:** antes de excluir o e-mail dele, trocar o e-mail e o telefone de recuperação de **todas** as contas Gmail dos aparelhos para o do novo responsável e atualizar o cofre de senhas.
15. **Computador:** depois da cópia dos arquivos (passo 4), apagar o usuário da pessoa ou reinstalar pela instalação padrão (POP-04/05) antes de passar para outra pessoa.
16. Atualizar o inventário no **GLPI**: equipamento devolvido, "disponível" ou "em manutenção".

### 4.4 Depois da saída

17. **Após 90 dias:**
    - **Backup permanente da caixa:** baixar a caixa de e-mail inteira (todas as pastas: entrada, enviados, arquivadas) por IMAP para o servidor, na pasta `emails-ex-funcionarios/<nome.sobrenome>/`. Abrir alguns e-mails do backup para conferir. **Esse backup nunca é apagado** e entra na cópia noturna do servidor (backup do servidor).
    - Só depois do backup conferido: desligar o encaminhamento e **excluir a conta de e-mail** (libera a licença na hospedagem).
18. Fechar o chamado no GLPI com o Formulário B todo marcado. Arquivar o Formulário D (papel) na pasta do funcionário no RH.

## 5. Conferência

- No dia seguinte ao desligamento, a TI tenta logar (ou pede o relatório do sistema) e confirma que **nenhum** acesso do Formulário B continua ativo.
- A revisão semestral (POP-11 §4) procura contas que escaparam deste POP.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
