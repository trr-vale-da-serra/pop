# POP-07: Backup e teste de restauração

> **Versão:** 1.2 · **Data:** 20/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Garantir que **dá para recuperar** os arquivos dos PCs, o servidor e as conversas do WhatsApp. Backup que nunca foi testado não conta como backup.

## 2. O que tem backup

| O quê | Ferramenta | Frequência | Guarda |
|---|---|---|---|
| Arquivos dos PCs | Backup dos PCs | Todo dia, sempre que o PC está ligado na rede da empresa | 30 dias |
| Imagem completa do disco dos PCs | Backup dos PCs | Toda semana, sempre que o PC está ligado na rede da empresa | 4 imagens |
| Servidor inteiro | Backup do servidor, para disco USB externo | Toda noite | 30 dias |
| WhatsApp dos celulares | Google Drive do Gmail do aparelho | Todo dia, sem vídeos | Último backup |
| Caixa de e-mail de quem saiu | Download por IMAP para o servidor (POP-02) | Na saída | Permanente |

## 3. Todo dia (automático)

- O backup do servidor roda sozinho à noite.
- O backup dos PCs roda sozinho, durante o dia, sempre que o PC está ligado na rede da empresa. **Ninguém precisa deixar o PC ligado.**
- O monitoramento avisa a TI por e-mail se um backup falhar.

## 4. Toda semana (TI, segunda-feira)

1. No backup dos PCs: conferir que **todos** os PCs têm backup de arquivos recente e a imagem da semana.
2. PC sem backup há mais de 2 dias: descobrir por quê (desligado, fora da empresa, sem rede, disco cheio) e resolver.

## 5. Todo mês (TI, 1ª semana)

### 5.1 Teste de restauração

3. **PC:** escolher um PC diferente a cada mês e restaurar uma pasta do backup dos PCs para outro lugar. Abrir alguns arquivos e confirmar que estão bons.
4. **Servidor:** restaurar do disco USB (backup do servidor) os dados do cofre de senhas para uma pasta temporária e confirmar que os dados estão lá. Apagar a pasta temporária depois.
5. **A cada 3 meses:** restaurar uma **imagem completa** de PC num computador de teste.

### 5.2 WhatsApp

6. Em cada celular: WhatsApp → Configurações → Conversas → Backup. Conferir:
   - Último backup de **ontem ou hoje**.
   - Conta: o **Gmail da empresa** do aparelho.
   - Vídeos **fora** do backup e criptografia de ponta a ponta **ligada**.
   - Tamanho **abaixo de 12 GB**. Acima disso: limpar arquivos grandes antigos em "Gerenciar armazenamento".
7. Conferir que a senha do backup criptografado de cada aparelho está no cofre de senhas.

## 6. Registro

Chamado mensal no GLPI: o que foi restaurado, se deu certo e os celulares conferidos. Teste que falhou vira chamado urgente.
