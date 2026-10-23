# POP-04: Instalação padrão de computador Linux

> **Versão:** 1.3 · **Data:** 23/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Todo PC Linux da empresa sai **igual**: mesmo sistema, mesma aparência, mesmos agentes e registrado no inventário.

## 2. Quando

- PC novo ou PC migrado do Windows.
- PC que volta de outra pessoa (POP-02, POP-11 §4).

## 3. Antes de começar

1. Copiar os arquivos de trabalho do PC, se tiver (backup dos PCs ou cópia manual).
2. Pendrive com o **Linux padrão** na versão do [anexo de ferramentas](../anexos/ferramentas.md) §2, baixado do site oficial.
3. Número de patrimônio do PC.

## 4. Passo a passo

### 4.1 Instalação do sistema

1. Iniciar pelo pendrive e escolher **Instalar**.
2. Idioma **Português (Brasil)**, teclado **Português (Brasil ABNT2)**.
3. Tipo de instalação: **apagar o disco**, **sem** criptografia do disco.
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

### 4.3 Conta dos funcionários

9. O pendrive de instalação já cria a **conta dos funcionários** (`usuario`), **com permissão de administrador**, **sem senha** e com **login automático** (POP-TI §3.1). Não há conta por pessoa.
   - Só se o PC foi instalado à mão: *Configurações → Sistema → Usuários → Adicionar usuário*, tipo **Administrador**; apagar a senha no terminal da conta da TI (`sudo passwd -d usuario`); ligar o **login automático** desse usuário. O funcionário **nunca** usa o terminal.
10. **PC do gestor do departamento:** se o gestor quiser senha, na entrega (POP-01 §4.5) a TI abre *Configurações → Sistema → Usuários → Desbloquear* (com a senha da TI), escolhe a conta dos funcionários → **Senha → Definir uma senha agora**, e o **gestor digita** a senha que escolheu. Desligar o login automático. A senha não vai para o cofre. Se ele esquecer, a TI troca pela mesma tela.

### 4.4 Conferência

11. O PC aparece no **acesso remoto** e abre a tela remota.
12. O PC aparece no **GLPI** com o hardware e o software corretos.
13. O PC aparece no **painel de segurança** como ativo.
14. O primeiro **backup dos PCs** terminou.
15. Registrar no GLPI: patrimônio, número de série e quem recebe.

## 5. Registro

- Inventário no GLPI atualizado.
