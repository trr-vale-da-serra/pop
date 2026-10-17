# POP-05: Instalação padrão de computador Windows

> **Versão:** 1.1 · **Data:** 17/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Padronizar os PCs que **continuam no Windows** porque usam algum programa que não roda no Linux. O padrão da empresa é o Linux (POP-04).

## 2. Quando

- PC que precisa de programa só para Windows (o motivo fica registrado no GLPI).
- PC Windows que volta de outra pessoa (POP-02, POP-11 §4).

## 3. Antes de começar

1. Copiar os arquivos de trabalho do PC, se tiver.
2. Pendrive de instalação do Windows, criado com a ferramenta oficial da Microsoft.
3. Número de patrimônio do PC.

## 4. Passo a passo

### 4.1 Instalação do sistema

1. Instalar o Windows apagando o disco.
2. Nome do computador: `<EMPRESA>-PC-<patrimônio>` (ex.: `POSTOS-PC-0007`).
3. Criar a **conta administradora da TI** (senha no cofre de senhas).
4. **Sem criptografia de disco:** se o Windows ligou a criptografia sozinho (*Configurações → Privacidade e segurança*), desligar e esperar terminar a descriptografia.

### 4.2 Configuração padrão (configuração em massa)

5. Liberar o acesso da ferramenta de configuração em massa (comando no [anexo de ferramentas](../anexos/ferramentas.md) §3).
6. No servidor: incluir o PC na ferramenta de configuração em massa e rodar o roteiro padrão do Windows. Ele faz:
   - Atualizações do Windows.
   - Programas padrão.
   - Confere que o **antivírus** está ativo.
   - Agentes: **acesso remoto**, **GLPI Agent**, **painel de segurança** e **backup dos PCs**.
7. Instalar o programa que exige Windows.
8. Programa de suporte de fornecedor: instalar **só** se o PC recebe suporte de fornecedor (POP-TI §3.2).

### 4.3 Usuário da pessoa

9. Criar o usuário local da pessoa **sem permissão de administrador**, com senha forte gerada pelo cofre de senhas e salva na pasta do funcionário.
10. Entregar a senha à pessoa no fim da integração (POP-01 §4.5). A pessoa não troca a senha sem a TI.

### 4.4 Conferência

11. O PC aparece no **acesso remoto**, no **GLPI** e no **painel de segurança**.
12. O primeiro **backup dos PCs** terminou.
13. Registrar no GLPI: patrimônio, número de série, quem recebe e **por que é Windows**.

## 5. Registro

- Inventário no GLPI atualizado.
