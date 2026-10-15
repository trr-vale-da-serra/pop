# POP-04: Instalação padrão de computador Linux

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Todo PC Linux da empresa sai **igual**: mesmo sistema, mesma aparência, mesmos agentes, disco criptografado e registrado no inventário.

## 2. Quando

- PC novo ou PC migrado do Windows.
- PC que volta de outra pessoa (POP-02, POP-11 §5).

## 3. Antes de começar

1. Copiar os arquivos de trabalho do PC, se tiver (UrBackup ou cópia manual).
2. Pendrive com o **Ubuntu 26.04 LTS** (Desktop), baixado do site oficial `ubuntu.com`.
3. Número de patrimônio do PC.

## 4. Passo a passo

### 4.1 Instalação do sistema

1. Iniciar pelo pendrive e escolher **Instalar Ubuntu**.
2. Idioma **Português (Brasil)**, teclado **Português (Brasil ABNT2)**.
3. Tipo de instalação: **apagar o disco** e marcar **criptografia do disco (LUKS)**. A senha do disco vai para o Vaultwarden, no item do PC.
4. Nome do computador: `<EMPRESA>-PC-<patrimônio>` (ex.: `TRR-PC-0012`).
5. Usuário: a **conta administradora da TI** (senha no Vaultwarden).

### 4.2 Configuração padrão (Ansible)

6. Na máquina nova: instalar o SSH (`sudo apt install openssh-server`).
7. No servidor: incluir o PC no inventário do Ansible e rodar o playbook padrão do Linux. Ele faz:
   - Atualizações e `unattended-upgrades` (atualização de segurança diária).
   - Extensões **Dash to Panel** e **ArcMenu** (aparência parecida com o Windows).
   - Programas padrão (navegador, LibreOffice, leitor de PDF).
   - **ClamAV**.
   - Agentes: **MeshCentral**, **GLPI Agent**, **Wazuh** e **UrBackup**.
8. AnyDesk: instalar **só** se o PC recebe suporte de fornecedor (POP-TI §3.2).

### 4.3 Usuário da pessoa

9. Criar o usuário da pessoa **sem permissão de administrador**, com senha forte gerada pelo Vaultwarden e salva na pasta do funcionário.
10. Entregar a senha à pessoa no primeiro dia (POP-01 §4.4). A pessoa não troca a senha sem a TI.

### 4.4 Conferência

11. O PC aparece no **MeshCentral** e abre a tela remota.
12. O PC aparece no **GLPI** com o hardware e o software corretos.
13. O PC aparece no **Wazuh** como ativo.
14. O primeiro backup do **UrBackup** terminou.
15. Registrar no GLPI: patrimônio, número de série e quem recebe.

## 5. Registro

- Item do PC no Vaultwarden: senha do disco (LUKS).
- Inventário no GLPI atualizado.
