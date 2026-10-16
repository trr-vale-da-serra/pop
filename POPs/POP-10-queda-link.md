# POP-10: Queda do link principal

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Manter a empresa com internet quando o link principal cai, usando a Starlink, e saber o que funciona e o que não funciona durante a queda.

## 2. Como funciona

- O **OPNsense** troca para a **Starlink sozinho** quando o link principal cai e volta para o principal sozinho quando ele normaliza.
- O **Uptime Kuma** avisa a TI no WhatsApp quando o link cai e quando volta.

| Durante a queda | Funciona? |
|---|---|
| Internet dentro da empresa (navegar, WhatsApp, e-mail, sistemas na nuvem) | ✅ Sim, pela Starlink |
| Serviços internos (GLPI, Vaultwarden, Headwind) para quem está na empresa | ✅ Sim |
| Acesso de fora ao MeshCentral e à VPN | ❌ Não, até o link principal voltar (a Starlink não tem IP fixo) |

## 3. Passo a passo (TI)

### 3.1 Quando o link cai

1. Conferir no OPNsense que a rede passou para a Starlink.
2. Se **não** passou: no OPNsense, trocar o gateway para a Starlink manualmente.
3. Abrir chamado com a operadora do link principal e anotar o **número do protocolo**.
4. Se a queda passar de **1 hora**: avisar a empresa que o acesso remoto de fora está fora do ar e evitar downloads grandes (atualizações, vídeos) na Starlink.

### 3.2 Quando o link volta

5. Conferir no OPNsense que a rede voltou para o link principal.
6. Conferir no Uptime Kuma que todos os serviços estão no ar.
7. Testar o acesso de fora ao MeshCentral (pelo celular, no 4G).

## 4. Teste a cada 6 meses

Em abril e outubro, fora do expediente: desconectar o cabo do link principal e conferir que a troca para a Starlink e a volta acontecem sozinhas.

## 5. Registro

Chamado no GLPI: horário da queda e da volta, protocolo da operadora e se a troca automática funcionou.

## Perfis de acesso por cargo

> Mesma tabela em todos os POPs. As regras completas estão no [POP-01 §3](POP-01-entrada.md).

| Perfil | Cargos | O que a TI entrega | RH abre o chamado |
|---|---|---|---|
| **A: Sem acesso de TI** | Motorista, zelador, auxiliar de limpeza, mecânico, borracheiro | Nada. O chamado serve só para registrar a pessoa | Até o **dia do início** (pode começar no mesmo dia) |
| **B: Oficina** | Estoquista, documentação, compras | Celular corporativo, e-mail corporativo, Petroshow, Sigest, Infinitum e Sistema VS | **2 dias úteis antes** do início |
| **C: Escritório** | Administrativo, financeiro, comercial, RH/DP | Tudo do perfil B, Orion e computador | **3 dias úteis antes** do início |
| **D: Gestão** | Gerentes e supervisores | Tudo do perfil C | **3 dias úteis antes** do início |
