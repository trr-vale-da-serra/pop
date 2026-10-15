# POP-09: Incidente de segurança

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Agir rápido e de forma organizada quando acontece algo como vírus, invasão de conta, vazamento de dados ou acesso indevido.

## 2. Exemplos de incidente

- Alerta crítico no Wazuh ou vírus encontrado pelo Defender ou pelo ClamAV.
- Funcionário clicou em link suspeito ou digitou a senha num site falso.
- Conta de e-mail ou de WhatsApp mandando mensagens que a pessoa não mandou.
- Arquivos que de repente não abrem ou mudam de nome (possível ransomware).
- Acesso a sistema por quem não deveria ter (ex.: ex-funcionário).
- Celular ou PC perdido com dados (ver também POP-03).

## 3. Quem avisar

| Situação | Quem a TI avisa |
|---|---|
| Qualquer incidente | O **gestor** do funcionário ou do setor afetado |
| Pode ter vazado **dado pessoal** de clientes ou funcionários (nome, CPF, telefone, dados bancários) | Também a **direção (Artur)**, que decide e faz a comunicação à **ANPD** e às pessoas afetadas. A LGPD pede essa comunicação em **até 3 dias úteis** quando há risco relevante |

**Funcionário que perceber algo estranho:** avisa a TI **na hora**, sem desligar o PC, sem tentar resolver sozinho.

## 4. Passo a passo (TI)

### 4.1 Conter (na hora)

1. **Isolar o equipamento:** tirar o PC da rede (cabo e Wi-Fi). Não desligar, para não perder evidência. Celular: bloqueio remoto pelo Headwind MDM.
2. **Trocar as senhas** das contas envolvidas, atualizar no Vaultwarden e desconectar as sessões abertas (e-mail, sistemas).
3. Se for conta de ex-funcionário: bloquear na hora e conferir o POP-02.

### 4.2 Entender (no mesmo dia)

4. Ver no Wazuh e no MeshCentral o que aconteceu, desde quando e em quais máquinas.
5. Responder: **vazou dado pessoal?** Se sim ou se não der para saber, avisar a direção (seção 3).
6. Avisar o gestor do setor afetado.

### 4.3 Resolver

7. PC com vírus ou ransomware: **reinstalar** pelo POP-04 ou POP-05 e restaurar os arquivos do backup (UrBackup) de **antes** do incidente.
8. Conferir se outras máquinas foram afetadas.
9. Corrigir a causa (atualização pendente, senha fraca, app não aprovado, falha de processo).

### 4.4 Depois

10. Conversar com o funcionário sobre o que aconteceu e como evitar, sem punição por ter avisado.
11. Se o incidente mostrou falha num POP, atualizar o POP.

## 5. Registro

Chamado no GLPI com: o que aconteceu, quando foi percebido, o que foi feito e quem foi avisado. Se envolveu dado pessoal, guardar também o que a direção decidiu sobre a comunicação à ANPD.
