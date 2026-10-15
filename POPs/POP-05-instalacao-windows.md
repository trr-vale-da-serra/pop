# POP-05: Instalação padrão de computador Windows

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Padronizar os PCs que **continuam no Windows** porque usam algum programa que não roda no Linux. O padrão da empresa é o Linux (POP-04).

## 2. Quando

- PC que precisa de programa só para Windows (o motivo fica registrado no GLPI).
- PC Windows que volta de outra pessoa (POP-02, POP-11 §5).

## 3. Antes de começar

1. Copiar os arquivos de trabalho do PC, se tiver.
2. Pendrive de instalação do Windows, criado com a ferramenta oficial da Microsoft.
3. Número de patrimônio do PC.

## 4. Passo a passo

### 4.1 Instalação do sistema

1. Instalar o Windows apagando o disco.
2. Nome do computador: `<EMPRESA>-PC-<patrimônio>` (ex.: `POSTOS-PC-0007`).
3. Criar a **conta administradora da TI** (senha no Vaultwarden).
4. **Criptografia:**
   - Windows **Pro**: ligar o **BitLocker**. A chave de recuperação vai para o Vaultwarden, no item do PC.
   - Windows **Home**: ligar a **Criptografia do dispositivo** se aparecer em *Configurações → Privacidade e segurança*. Se não aparecer, registrar no GLPI como "sem criptografia: migrar ou atualizar para Pro".

### 4.2 Configuração padrão (Ansible)

5. Ligar o WinRM (comando da TI, guardado com o playbook).
6. No servidor: incluir o PC no inventário do Ansible e rodar o playbook padrão do Windows. Ele faz:
   - Atualizações do Windows.
   - Programas padrão.
   - Confere que o **Microsoft Defender** está ativo.
   - Agentes: **MeshCentral**, **GLPI Agent**, **Wazuh** e **UrBackup**.
7. Instalar o programa que exige Windows.
8. AnyDesk: instalar **só** se o PC recebe suporte de fornecedor (POP-TI §3.2).

### 4.3 Usuário da pessoa

9. Criar o usuário local da pessoa **sem permissão de administrador**, com senha forte gerada pelo Vaultwarden e salva na pasta do funcionário.
10. Entregar a senha à pessoa no primeiro dia (POP-01 §4.4). A pessoa não troca a senha sem a TI.

### 4.4 Conferência

11. O PC aparece no **MeshCentral**, no **GLPI** e no **Wazuh**.
12. O primeiro backup do **UrBackup** terminou.
13. Registrar no GLPI: patrimônio, número de série, quem recebe e **por que é Windows**.

## 5. Registro

- Item do PC no Vaultwarden: chave do BitLocker (se Pro).
- Inventário no GLPI atualizado.
