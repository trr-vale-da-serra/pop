#!/usr/bin/env bash
# PC novo (POP-04 §4.2): põe o PC no inventário e roda o linux-padrao.
# Uso:  ./pc-novo.sh <EMPRESA>-PC-<patrimônio> <IP>   [opções do ansible-playbook]
# Ex.:  ./pc-novo.sh TRR-PC-0003 10.10.10.123
#       ./pc-novo.sh TRR-PC-0003 10.10.10.123 -e reiniciar=false   (alguém usando o PC)
# IP = "hostname -I" no PC, ou a lista de DHCP do firewall (nome pc-novo-XXXX).
set -euo pipefail
cd "$(dirname "$0")"

nome=${1:-}
ip=${2:-}
if [[ ! $nome =~ ^(POSTOS|SERTAO|TRR)-PC-[0-9]{4}$ || ! $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Uso: ./pc-novo.sh <EMPRESA>-PC-<patrimônio> <IP>   ex.: ./pc-novo.sh TRR-PC-0003 10.10.10.123"
  exit 1
fi
shift 2

# PC reinstalado tem chave SSH nova: troca a antiga do known_hosts pela atual.
mkdir -p ~/.ssh
ssh-keygen -R "$ip" >/dev/null 2>&1 || true
if ! ssh-keyscan -T 10 -t ed25519 "$ip" >> ~/.ssh/known_hosts 2>/dev/null; then
  echo "O PC $ip não respondeu no SSH. Está ligado e na rede? Foi instalado pelo pendrive?"
  exit 1
fi

# Inventário local (não vai para o git): inclui o PC ou atualiza o IP dele.
python3 - "$nome" "$ip" <<'PY'
import os, sys, yaml
nome, ip = sys.argv[1:]
arq = "inventario/hosts.yml"
inv = (yaml.safe_load(open(arq, encoding="utf-8")) if os.path.exists(arq) else None) or {}
grupos = inv.setdefault("all", {}).setdefault("children", {})
linux = grupos["linux"] = grupos.get("linux") or {}
pcs = linux["hosts"] = linux.get("hosts") or {}
pcs[nome] = {**(pcs.get(nome) or {}), "ansible_host": ip}
grupos.setdefault("windows", {"hosts": {}})
with open(arq, "w", encoding="utf-8") as f:
    yaml.safe_dump(inv, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
print(f"Inventário: {nome} = {ip}")
PY

extra=()
[[ -f inventario/group_vars/linux/vault.yml ]] && extra+=(--ask-vault-pass)

echo "Senha pedida a seguir (BECOME password): a da conta da TI."
ansible-playbook playbooks/linux-padrao.yml -l "$nome" -K "${extra[@]}" "$@"
