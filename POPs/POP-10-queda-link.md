# POP-10: Queda do link principal

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Manter a empresa com internet quando o link principal cai, usando o link reserva, e saber o que funciona e o que não funciona durante a queda.

## 2. Como funciona

- O **firewall** troca para o **link reserva sozinho** quando o link principal cai e volta para o principal sozinho quando ele normaliza.
- O **monitoramento** avisa a TI por e-mail quando o link cai e quando volta.

| Durante a queda | Funciona? |
|---|---|
| Internet dentro da empresa (navegar, WhatsApp, e-mail, sistemas na nuvem) | ✅ Sim, pelo link reserva |
| Serviços internos (GLPI, cofre de senhas, MDM) para quem está na empresa | ✅ Sim |
| Acesso remoto e VPN, de fora da empresa | ❌ Não, até o link principal voltar (o link reserva não tem IP fixo) |

## 3. Passo a passo (TI)

### 3.1 Quando o link cai

1. Conferir no firewall que a rede passou para o link reserva.
2. Se **não** passou: no firewall, trocar o gateway para o link reserva manualmente.
3. Abrir chamado com a operadora do link principal e anotar o **número do protocolo**.
4. Se a queda passar de **1 hora**: avisar a empresa que o acesso remoto de fora está fora do ar e evitar downloads grandes (atualizações, vídeos) no link reserva.

### 3.2 Quando o link volta

5. Conferir no firewall que a rede voltou para o link principal.
6. Conferir no monitoramento que todos os serviços estão no ar.
7. Testar o acesso de fora à ferramenta de acesso remoto (pelo celular, no 4G).

## 4. Teste a cada 6 meses

Em abril e outubro, fora do expediente: desconectar o cabo do link principal e conferir que a troca para o link reserva e a volta acontecem sozinhas.

## 5. Registro

Chamado no GLPI: horário da queda e da volta, protocolo da operadora e se a troca automática funcionou.
