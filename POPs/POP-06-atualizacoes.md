# POP-06: Atualizações mensais

> **Versão:** 1.1 · **Data:** 17/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Manter todos os PCs, celulares e o servidor com as atualizações de segurança em dia, **sem atrapalhar o trabalho**.

## 2. Quando

**2ª quarta-feira de cada mês, à noite** (depois do expediente). É o dia seguinte às atualizações mensais da Microsoft.

Entre uma janela e outra:

- **Linux:** atualizações de segurança automáticas todos os dias.
- **Celulares:** atualização automática em janela noturna (MDM).
- **Falha grave anunciada** (painel de segurança ou notícia): a TI atualiza no mesmo dia, sem esperar a janela.

## 3. Passo a passo

### 3.1 No dia (até o fim do expediente)

1. Avisar no grupo da empresa: "Hoje à noite os computadores vão atualizar e reiniciar. Salve seu trabalho e deixe o PC ligado."
2. Conferir no backup dos PCs que o backup da noite anterior deu certo em todos os PCs.

### 3.2 À noite (TI)

3. Rodar na ferramenta de configuração em massa o roteiro de atualização do **Linux**.
4. Rodar na ferramenta de configuração em massa o roteiro de atualização do **Windows**.
5. Os roteiros reiniciam as máquinas que precisarem.
6. Atualizar o **servidor** por último: contêineres e sistema. Esperar todos os serviços voltarem no monitoramento.

### 3.3 No dia seguinte

7. No acesso remoto: conferir que todos os PCs voltaram online.
8. No painel de segurança: conferir a lista de vulnerabilidades. PC que ficou sem atualizar recebe atualização manual.
9. No MDM: conferir celulares com o sistema muito atrasado.

## 4. Registro

Chamado mensal no GLPI: data, máquinas atualizadas, máquinas com problema e o que foi feito.
