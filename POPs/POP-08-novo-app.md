# POP-08: Solicitação de app novo (celular ou computador)

> **Versão:** 1.0 · **Data:** 15/10/2026 · **Responsável:** TI: Lui Grosz
> Faz parte do [Plano de TI](../POP-TI.md).

## 1. Objetivo

Só entram nos equipamentos da empresa programas e apps **conferidos pela TI**. O funcionário não instala nada por conta própria (não tem permissão de administrador no PC, e o celular só aceita apps da lista aprovada).

## 2. Quem faz o quê

| Papel | Responsabilidade |
|---|---|
| **Funcionário** | Abre o chamado no GLPI dizendo qual app e para quê |
| **TI** | Avalia, aprova ou recusa, instala e registra. **A decisão é só da TI** |

## 3. Passo a passo

1. **Funcionário** abre um chamado no GLPI: nome do app, em qual equipamento e para que vai usar no trabalho.
2. **TI** avalia:
   - Vem da loja oficial (Play Store, `apt`/loja do Ubuntu, site oficial do fabricante)?
   - É gratuito ou a empresa já tem licença?
   - Que permissões pede (contatos, arquivos, câmera) e se fazem sentido para o uso?
   - Tem histórico de problema de segurança?
   - Já existe app aprovado que faz a mesma coisa?
3. **TI** responde no chamado: **aprovado** ou **recusado**, com o motivo, em até **3 dias úteis**.
4. Se aprovado:
   - **Celular:** incluir na lista de apps aprovados do Headwind MDM. Vale para todos os aparelhos daquele grupo.
   - **PC:** instalar pelo MeshCentral ou pelo Ansible.
5. App pago: só depois que a compra for autorizada por quem paga.

## 4. Lista de apps aprovados

Os **apps padrão** de todo celular estão no POP-TI §4.2 e não precisam de solicitação. A lista completa fica no Headwind MDM (celulares) e no playbook do Ansible (PCs). Na revisão semestral de acessos (POP-11 §4), a TI remove o que ninguém usa mais.

## 5. Registro

Chamado no GLPI com a decisão e o motivo.
