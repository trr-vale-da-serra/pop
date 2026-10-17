# POP-04: Instalação padrão de computador Linux

> **Versão:** 1.1 · **Data:** 17/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Todo PC Linux da empresa sai **igual**: mesmo sistema, mesma aparência, mesmos agentes, disco criptografado e registrado no inventário.

## 2. Quando

- PC novo ou PC migrado do Windows.
- PC que volta de outra pessoa (POP-02, POP-11 §5).

## 3. Antes de começar

1. Copiar os arquivos de trabalho do PC, se tiver (backup dos PCs ou cópia manual).
2. Pendrive com o **Linux padrão** na versão do [anexo de ferramentas](../anexos/ferramentas.md) §2, baixado do site oficial.
3. Número de patrimônio do PC.

## 4. Passo a passo

### 4.1 Instalação do sistema

1. Iniciar pelo pendrive e escolher **Instalar**.
2. Idioma **Português (Brasil)**, teclado **Português (Brasil ABNT2)**.
3. Tipo de instalação: **apagar o disco** e ligar a **criptografia do disco**. A senha do disco vai para o cofre de senhas, no item do PC.
4. Nome do computador: `<EMPRESA>-PC-<patrimônio>` (ex.: `TRR-PC-0012`).
5. Usuário: a **conta administradora da TI** (senha no cofre de senhas).

### 4.2 Configuração padrão (configuração em massa)

6. Na máquina nova: liberar o acesso da ferramenta de configuração em massa (comando no [anexo de ferramentas](../anexos/ferramentas.md) §3).
7. No servidor: incluir o PC na ferramenta de configuração em massa e rodar o roteiro padrão do Linux. Ele faz:
   - Atualizações e atualização de segurança diária automática.
   - Aparência parecida com o Windows (barra de tarefas embaixo e menu Iniciar).
   - Programas padrão (navegador, LibreOffice, leitor de PDF).
   - **Antivírus**.
   - Agentes: **acesso remoto**, **GLPI Agent**, **painel de segurança** e **backup dos PCs**.
8. Programa de suporte de fornecedor: instalar **só** se o PC recebe suporte de fornecedor (POP-TI §3.2).

### 4.3 Usuário da pessoa

9. Criar o usuário da pessoa **sem permissão de administrador**, com senha forte gerada pelo cofre de senhas e salva na pasta do funcionário.
10. Entregar a senha à pessoa no primeiro dia (POP-01 §4.4). A pessoa não troca a senha sem a TI.

### 4.4 Conferência

11. O PC aparece no **acesso remoto** e abre a tela remota.
12. O PC aparece no **GLPI** com o hardware e o software corretos.
13. O PC aparece no **painel de segurança** como ativo.
14. O primeiro **backup dos PCs** terminou.
15. Registrar no GLPI: patrimônio, número de série e quem recebe.

## 5. Registro

- Item do PC no cofre de senhas: senha do disco.
- Inventário no GLPI atualizado.
