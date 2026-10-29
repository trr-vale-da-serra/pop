# POP-02: Saída de funcionário

> **Versão:** 1.2 · **Data:** 29/10/2026 · **Responsáveis:** TI: Lui Grosz · RH: Camila Faverao
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
4. **TI** confere que não ficou arquivo de trabalho fora da **nuvem da empresa** no PC (se ficou, passa para a nuvem) e copia o que for de trabalho da pasta pessoal da pessoa para a pasta de quem assume ou do departamento. Depois, desativa a conta da pessoa na nuvem (os arquivos dela ficam no servidor).

### 4.2 Bloqueio (no horário da tabela da seção 3)

Seguir o Formulário B item por item e marcar cada um como bloqueado no GLPI, com data e hora:

5. **E-mail:**
   - Trocar a senha no painel da hospedagem (a pessoa perde o acesso na hora) e atualizar no cofre de senhas.
6. **Sistema VS:** desativar o usuário (não excluir: o histórico de quem fez o quê precisa continuar).
7. **Petroshow / Infinitum / Orion:** desativar os usuários (não excluir, pelo mesmo motivo).
8. **WhatsApp corporativo:** o número é da empresa. Conferir que o backup do dia chegou ao servidor (POP-TI §4.3), recolher o aparelho, passar o atendimento para quem assume e trocar o nome/foto do perfil.
9. **Grupos de WhatsApp pessoais de trabalho:** se a pessoa estava em grupos de trabalho com o número pessoal, removê-la.
10. **Acesso remoto:** remover a pessoa da **ferramenta de acesso remoto** e da **VPN**, se tinha acesso.

### 4.3 Equipamentos

11. Recolher todos os equipamentos do Formulário C (termo de responsabilidade) e conferir a lista item por item.
12. Preencher o **Formulário D: Termo de devolução**, assinado pelo funcionário e pela TI. Equipamento faltando ou danificado: registrar no termo e avisar o RH.
13. **Celular corporativo:** fazer o **wipe** pelo MDM. Depois do wipe, desbloquear com o Gmail da empresa do aparelho (FRP) e trocar a senha dessa conta no cofre de senhas antes de entregar o aparelho a outra pessoa. Se o aparelho não foi devolvido: **bloqueio remoto** na hora e seguir o POP-03.
    - **Se quem sai é o responsável de TI:** antes de excluir o e-mail dele, trocar o e-mail e o telefone de recuperação de **todas** as contas Gmail dos aparelhos para o do novo responsável e atualizar o cofre de senhas.
14. **Computador:** depois da cópia dos arquivos (passo 4), apagar o usuário da pessoa ou reinstalar pela instalação padrão (POP-04/05) antes de passar para outra pessoa.
15. Atualizar o inventário no **GLPI**: equipamento devolvido, "disponível" ou "em manutenção".

### 4.4 Depois da saída

16. **Após 90 dias:**
    - **Backup permanente da caixa:** baixar a caixa de e-mail inteira (todas as pastas: entrada, enviados, arquivadas) por IMAP para o servidor, na pasta `emails-ex-funcionarios/<nome.sobrenome>/`. Abrir alguns e-mails do backup para conferir. **Esse backup nunca é apagado** e fica no espelho de discos do servidor, com snapshots (backup do servidor).
    - Só depois do backup conferido: **excluir a conta de e-mail** (libera a licença na hospedagem).
17. Fechar o chamado no GLPI com o Formulário B todo marcado. Arquivar o Formulário D (papel) na pasta do funcionário no RH.

## 5. Conferência

- No dia seguinte ao desligamento, a TI tenta logar (ou pede o relatório do sistema) e confirma que **nenhum** acesso do Formulário B continua ativo.
- A revisão semestral (POP-11 §3) procura contas que escaparam deste POP.

## Aprovação

| Área | Nome | Assinatura | Data |
|---|---|---|---|
| RH | Camila Faverao | | ___/___/____ |
| TI | Lui Grosz | | ___/___/____ |
