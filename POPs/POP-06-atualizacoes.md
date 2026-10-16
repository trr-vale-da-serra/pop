# POP-06: Atualizações mensais

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Manter todos os PCs, celulares e o servidor com as atualizações de segurança em dia, **sem atrapalhar o trabalho**.

## 2. Quando

**2ª quarta-feira de cada mês, à noite** (depois do expediente). É o dia seguinte às atualizações mensais da Microsoft.

Entre uma janela e outra:

- **Linux:** atualizações de segurança automáticas todos os dias.
- **Celulares:** atualização automática em janela noturna (Headwind MDM).
- **Falha grave anunciada** (Wazuh ou notícia): a TI atualiza no mesmo dia, sem esperar a janela.

## 3. Passo a passo

### 3.1 No dia (até o fim do expediente)

1. Avisar no grupo da empresa: "Hoje à noite os computadores vão atualizar e reiniciar. Salve seu trabalho e deixe o PC ligado."
2. Conferir no UrBackup que o backup da noite anterior deu certo em todos os PCs.

### 3.2 À noite (TI)

3. Rodar no Ansible o playbook de atualização do **Linux** (`apt`).
4. Rodar no Ansible o playbook de atualização do **Windows** (`win_updates`).
5. Os playbooks reiniciam as máquinas que precisarem.
6. Atualizar o **servidor** por último: imagens Docker e sistema. Esperar todos os serviços voltarem no Uptime Kuma.

### 3.3 No dia seguinte

7. No MeshCentral: conferir que todos os PCs voltaram online.
8. No Wazuh: conferir a lista de vulnerabilidades. PC que ficou sem atualizar recebe atualização manual.
9. No Headwind MDM: conferir celulares com o sistema muito atrasado.

## 4. Registro

Chamado mensal no GLPI: data, máquinas atualizadas, máquinas com problema e o que foi feito.

## Perfis de acesso por cargo

> Mesma tabela em todos os POPs. As regras completas estão no [POP-01 §3](POP-01-entrada.md).

| Perfil | Cargos | O que a TI entrega | RH abre o chamado |
|---|---|---|---|
| **A: Sem acesso de TI** | Motorista, zelador, auxiliar de limpeza, mecânico, borracheiro | Nada. O chamado serve só para registrar a pessoa | Até o **dia do início** (pode começar no mesmo dia) |
| **B: Oficina** | Estoquista, documentação, compras | Celular corporativo, e-mail corporativo, Petroshow, Sigest, Infinitum e Sistema VS | **2 dias úteis antes** do início |
| **C: Escritório** | Administrativo, financeiro, comercial, RH/DP | Tudo do perfil B, Orion e computador | **3 dias úteis antes** do início |
| **D: Gestão** | Gerentes e supervisores | Tudo do perfil C | **3 dias úteis antes** do início |
