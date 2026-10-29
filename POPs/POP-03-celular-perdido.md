# POP-03: Celular perdido ou roubado

> **Versão:** 1.2 · **Data:** 29/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Proteger os dados da empresa e o número do WhatsApp quando um celular corporativo some, **no menor tempo possível**.

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **Funcionário** | Avisa a TI **na hora** que perceber o sumiço. Faz o B.O. se foi roubo |
| **TI** | Bloqueia, limpa o aparelho, bloqueia o chip e registra |
| **Gestor** | Decide quem atende o WhatsApp até o aparelho novo chegar |

## 3. Quando

Assim que o funcionário perceber. **Não esperar** "para ver se aparece": o bloqueio pode ser desfeito se o aparelho for encontrado.

## 4. Passo a passo

### 4.1 Na hora (TI)

1. **Bloqueio remoto** pelo MDM.
2. Avisar o gestor e confirmar quem atende o WhatsApp enquanto isso.

### 4.2 Em até 2 horas (TI)

3. Se o aparelho não apareceu: **limpeza remota (wipe)** pelo MDM. O aparelho continua preso ao Gmail da empresa (FRP): quem pegou não consegue usar.
4. Ligar para a operadora e **bloquear o chip**. Pedir um chip novo com o **mesmo número**.
5. Trocar a senha do Gmail do aparelho no cofre de senhas.

### 4.3 Se foi roubo (funcionário)

6. Fazer o **boletim de ocorrência (B.O.) online em até 24 horas** e mandar uma cópia para a TI e para o RH.
7. Perda simples (esqueceu, caiu, sumiu): **não precisa de B.O.**

### 4.4 Reposição (TI)

8. Preparar um aparelho novo pelo POP-11 §4 (troca de equipamento), com o chip novo.
9. No aparelho novo, **antes de abrir o WhatsApp**, copiar a pasta do aparelho antigo do servidor (`/dados/whatsapp/<aparelho>`) para a pasta do WhatsApp no aparelho novo (POP-TI §4.3). Depois entrar no WhatsApp com o mesmo número e **restaurar o backup** (senha do backup no cofre de senhas).
10. Atualizar o inventário no GLPI: aparelho antigo como "perdido" ou "roubado".

## 5. Se o aparelho aparecer

- Antes do wipe: desbloquear pelo MDM e conferir que nada foi alterado.
- Depois do wipe: desbloquear com o Gmail da empresa e registrar de novo no MDM.

## 6. Registro

- Chamado no GLPI com data e hora do aviso, do bloqueio, do wipe e do bloqueio do chip.
- Cópia do B.O. (se roubo) na pasta do funcionário no RH.
