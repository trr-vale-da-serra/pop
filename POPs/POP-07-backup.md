# POP-07: Backup e teste de restauração

> **Versão:** 1.3 · **Data:** 29/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Garantir que **dá para recuperar** os arquivos da empresa, os bancos dos sistemas, o servidor e as conversas do WhatsApp. Backup que nunca foi testado não conta como backup.

## 2. O que tem backup

Os PCs **não têm backup**: os arquivos de trabalho ficam na **nuvem da empresa**, e um PC com defeito é reinstalado pelo POP-04/05. Arquivo salvo fora da nuvem da empresa não tem backup.

| O quê | Onde fica | Proteção | Guarda |
|---|---|---|---|
| Arquivos da empresa | Nuvem da empresa, no espelho de discos do servidor | Espelho (um disco pode morrer) e snapshots a cada hora, dia e mês | 24 horas, 30 dias, 6 meses |
| Bancos dos sistemas | Servidor | Cópia toda noite para o **disco de backup** | 30 dias |
| VM dos sistemas | Servidor | Cópia todo domingo para o **disco de backup** | 2 cópias |
| WhatsApp dos celulares | Backup local do aparelho | Pasta copiada para o servidor (POP-TI §4.3), no espelho com snapshots | Último backup + snapshots |
| Caixa de e-mail de quem saiu | Servidor (POP-02) | Espelho e snapshots | **Permanente** |

O disco de backup fica desmontado fora da hora do backup e **não tem criptografia** (ALTERNATIVAS §1.5).

## 3. Todo dia (automático)

- Snapshots do espelho a cada hora.
- Domingo à 01:30: cópia da VM dos sistemas. A VM fica desligada por alguns minutos.
- 02:00: cópia dos bancos.
- O monitoramento avisa a TI se a cópia dos bancos não terminar bem no dia.
- Teste de saúde dos discos (todo dia às 02h, completo no dia 1). O resultado fica no registro do servidor e é conferido toda semana (§4).

## 4. Toda semana (TI, segunda-feira)

1. No servidor, conferir o espelho e o último backup:
   ```bash
   zpool status dados
   ```
   ```bash
   journalctl -t ti-backup --since "8 days ago"
   ```
   ```bash
   journalctl -u smartmontools --since "8 days ago" -p warning
   ```
   O espelho precisa estar `ONLINE` nos dois discos, cada banco com `ok` em todos os dias, e a saúde dos discos sem nenhuma linha.
2. Disco `DEGRADED` ou `FAULTED`, ou com aviso de saúde: trocar o disco (README do Ansible, "Servidor"). Banco sem `ok`: descobrir por quê e resolver no mesmo dia.

## 5. Todo mês (TI, 1ª semana)

### 5.1 Teste de restauração

3. **Arquivo da nuvem:** escolher uma pasta e restaurar a versão de 7 dias atrás de um snapshot para uma pasta temporária. Abrir alguns arquivos e confirmar que estão bons. Apagar a pasta temporária.
   ```bash
   ls /dados/departamentos/.zfs/snapshot/
   ```
4. **Banco:** restaurar o dump mais recente de um banco diferente a cada mês num banco descartável e conferir que as tabelas têm dados. O CheckVale tem teste próprio (`deploy/backup/restore-test.sh` no repositório dele).
5. **A cada 3 meses:** ligar a cópia da VM do disco de backup numa máquina de teste, **sem rede**, e conferir que os sistemas sobem. Nunca ligar a cópia com rede: os celulares sincronizariam com ela.

### 5.2 WhatsApp

6. No servidor, conferir que a pasta de cada celular em `/dados/whatsapp/` tem o arquivo `msgstore.db.crypt*` de **ontem ou hoje**.
7. Celular sem cópia recente: conferir no aparelho que o Syncthing está ligado e conectado, e que o WhatsApp fez o backup local (WhatsApp → Configurações → Conversas → Backup).
8. Conferir que a senha do backup criptografado de cada aparelho está no cofre de senhas.

## 6. Registro

Chamado mensal no GLPI: o que foi restaurado, se deu certo e os celulares conferidos. Teste que falhou vira chamado urgente.
