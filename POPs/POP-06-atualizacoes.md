# POP-06: Atualizações mensais

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Manter todos os PCs, celulares e o servidor com as atualizações de segurança em dia, **sem atrapalhar o trabalho**.

## 2. Quando

**2ª quarta-feira de cada mês, depois do expediente.** É o dia seguinte às atualizações mensais da Microsoft.

Atualiza só os PCs que estiverem ligados e na rede. **Ninguém precisa deixar o PC ligado:** o PC que estava desligado ou fora da empresa (ex.: notebook que o gerente levou para casa) é atualizado quando voltar à rede (seção 3.3).

Entre uma janela e outra:

- **Linux:** atualizações de segurança automáticas todos os dias.
- **Celulares:** atualização automática em janela noturna (MDM).
- **Falha grave anunciada** (painel de segurança ou notícia): a TI atualiza no mesmo dia, sem esperar a janela.

## 3. Passo a passo

### 3.1 No dia (até o fim do expediente)

1. Conferir no backup dos PCs que cada PC tem backup recente.

### 3.2 Depois do expediente (TI)

2. Rodar na ferramenta de configuração em massa o roteiro de atualização do **Linux**, nos PCs que estiverem ligados.
3. Rodar na ferramenta de configuração em massa o roteiro de atualização do **Windows**, nos PCs que estiverem ligados.
4. Os roteiros reiniciam as máquinas que precisarem.
5. Atualizar o **servidor** por último: contêineres e sistema. Esperar todos os serviços voltarem no monitoramento.

### 3.3 Nos dias seguintes

6. Anotar os PCs que ficaram de fora (estavam desligados ou fora da empresa).
7. Quando cada um aparecer online no acesso remoto, rodar o roteiro de atualização só nele. Se o reinício atrapalhar quem está usando, combinar o horário com a pessoa.
8. No painel de segurança: conferir a lista de vulnerabilidades. PC que continuar sem atualizar recebe atualização manual.
9. No MDM: conferir celulares com o sistema muito atrasado.

## 4. Registro

Chamado mensal no GLPI: data, máquinas atualizadas, máquinas com problema e o que foi feito.
