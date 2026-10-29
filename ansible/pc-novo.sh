#!/usr/bin/env bash
# PC novo (POP-04 §4.2, POP-05 §4.2): põe o PC no inventário e roda o
# linux-padrao ou o windows-padrao (descobre sozinho se é Linux ou Windows).
# Uso:  ./pc-novo.sh <EMPRESA>-PC-<patrimônio> <IP>   [opções do ansible-playbook]
# Ex.:  ./pc-novo.sh TRR-PC-0003 10.10.10.123
#       ./pc-novo.sh TRR-PC-0003 10.10.10.123 -e reiniciar=false   (alguém usando o PC)
# IP: no Linux "hostname -I", no Windows "ipconfig", ou a lista de DHCP do
# firewall (nome pc-novo-XXXX / PC-NOVO-XXXX).
set -euo pipefail
cd "$(dirname "$0")"

nome=${1:-}
ip=${2:-}
if [[ ! $nome =~ ^(POSTOS|SERTAO|TRR)-PC-[0-9]{4}$ || ! $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Uso: ./pc-novo.sh <EMPRESA>-PC-<patrimônio> <IP>   ex.: ./pc-novo.sh TRR-PC-0003 10.10.10.123"
  exit 1
fi
shift 2

porta_aberta() { timeout 5 bash -c "</dev/tcp/$ip/$1" 2>/dev/null; }

if porta_aberta 22; then
  grupo=linux
  # PC reinstalado tem chave SSH nova: troca a antiga do known_hosts pela atual.
  mkdir -p ~/.ssh
  ssh-keygen -R "$ip" >/dev/null 2>&1 || true
  ssh-keyscan -T 10 -t ed25519 "$ip" >> ~/.ssh/known_hosts 2>/dev/null
elif porta_aberta 5985; then
  grupo=windows
  if ! python3 -c "import winrm" 2>/dev/null; then
    echo "Falta o acesso ao Windows no WSL. Rodar uma vez: sudo apt install -y python3-winrm"
    exit 1
  fi
else
  echo "O PC $ip não respondeu (nem SSH, nem WinRM). Está ligado e na rede? Foi instalado pelo pendrive?"
  exit 1
fi

# Inventário local (não vai para o git): inclui o PC ou atualiza o IP dele.
python3 - "$nome" "$ip" "$grupo" <<'PY'
import os, sys, yaml
nome, ip, grupo = sys.argv[1:]
arq = "inventario/hosts.yml"
inv = (yaml.safe_load(open(arq, encoding="utf-8")) if os.path.exists(arq) else None) or {}
grupos = inv.setdefault("all", {}).setdefault("children", {})
dados = {}
for g in ("linux", "windows"):
    grupos[g] = grupos.get(g) or {}
    pcs = grupos[g]["hosts"] = grupos[g].get("hosts") or {}
    dados.update(pcs.pop(nome, None) or {})  # PC que trocou de sistema sai do grupo antigo
grupos[grupo]["hosts"][nome] = {**dados, "ansible_host": ip}
with open(arq, "w", encoding="utf-8") as f:
    yaml.safe_dump(inv, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
print(f"Inventário: {nome} = {ip} ({grupo})")
PY

extra=()
[[ -f inventario/group_vars/all/vault.yml ]] && extra+=(--ask-vault-pass)

if [[ $grupo == linux ]]; then
  echo "Senha pedida a seguir (BECOME password): a da conta da TI."
  ansible-playbook playbooks/linux-padrao.yml -l "$nome" -K "${extra[@]}" "$@"
else
  echo "Senha pedida a seguir (SSH password): a da conta da TI no Windows."
  ansible-playbook playbooks/windows-padrao.yml -l "$nome" -k "${extra[@]}" "$@"
fi
