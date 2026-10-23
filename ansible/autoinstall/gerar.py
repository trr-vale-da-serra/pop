"""Gera o autoinstall.yaml do pendrive de instalação do Linux (POP-04 §4.1).

Uso:  python gerar.py E:\
      (E: = pendrive gravado com o Rufus no modo ISO; ver ../README.md)

Pede a senha da conta da TI, o nome da conta dos funcionários (sem senha) e,
se quiser, o Wi-Fi da empresa (senhas no Vaultwarden) e grava o arquivo na
raiz do pendrive. Nada fica nesta pasta.
"""
import base64
import getpass
import os
import re
import shutil
import subprocess
import sys
import uuid

AQUI = os.path.dirname(os.path.abspath(__file__))
OPENSSL_WINDOWS = r"C:\Program Files\Git\usr\bin\openssl.exe"


def openssl():
    caminho = shutil.which("openssl") or (OPENSSL_WINDOWS if os.path.exists(OPENSSL_WINDOWS) else None)
    if not caminho:
        sys.exit("openssl não encontrado (vem com o Git para Windows).")
    return caminho


def senha(pergunta, minimo):
    while True:
        s = getpass.getpass(pergunta)
        if len(s) < minimo:
            print(f"  Mínimo de {minimo} caracteres.")
        elif s != getpass.getpass("  Repita: "):
            print("  As senhas não conferem.")
        elif '"' in s or "\\" in s:
            print('  Não use aspas (") nem barra invertida (\\).')
        else:
            return s


def wifi_comando(rede, senha_wifi):
    """Comando que grava a conexão Wi-Fi no PC instalado (só o root lê a senha)."""
    conexao = "\n".join([
        "[connection]",
        f"id={rede}",
        f"uuid={uuid.uuid4()}",
        "type=wifi",
        "autoconnect=true",
        "",
        "[wifi]",
        "mode=infrastructure",
        f"ssid={rede}",
        "",
        "[wifi-security]",
        "key-mgmt=wpa-psk",
        f"psk={senha_wifi}",
        "",
        "[ipv4]",
        "method=auto",
        "",
        "[ipv6]",
        "method=auto",
        "",
    ])
    # Em base64 para nenhum caractere do nome ou da senha atrapalhar o comando.
    b64 = base64.b64encode(conexao.encode("utf-8")).decode("ascii")
    arquivo = "/target/etc/NetworkManager/system-connections/wifi-empresa.nmconnection"
    return f"sh -c 'echo {b64} | base64 -d > {arquivo} && chmod 600 {arquivo}'"


def hash_senha(s):
    return subprocess.run(
        [openssl(), "passwd", "-6", "-stdin"], input=s, capture_output=True, text=True, check=True
    ).stdout.strip()


def func_comando(nome):
    """Comando que cria a conta dos funcionários no PC instalado: sem senha, com sudo."""
    script = "\n".join([
        # nopasswdlogin: a tela de login do GNOME entra sem pedir senha.
        "groupadd -f nopasswdlogin",
        f"useradd -m -s /bin/bash -G sudo,users,plugdev,nopasswdlogin -c {nome} {nome}",
        f"passwd -d {nome}",
        f"echo '{nome} ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/90-funcionarios",
        "chmod 440 /etc/sudoers.d/90-funcionarios",
        # Login automático nessa conta (POP-04 §4.3).
        "sed -i -E 's/^#?[[:space:]]*AutomaticLoginEnable[[:space:]]*=.*/AutomaticLoginEnable = true/' /etc/gdm3/custom.conf",
        f"sed -i -E 's/^#?[[:space:]]*AutomaticLogin[[:space:]]*=.*/AutomaticLogin = {nome}/' /etc/gdm3/custom.conf",
        "",
    ])
    # Em base64 para nenhum caractere atrapalhar o comando.
    b64 = base64.b64encode(script.encode("utf-8")).decode("ascii")
    return f"sh -c 'echo {b64} | base64 -d > /target/tmp/ti-func.sh && curtin in-target -- sh /tmp/ti-func.sh; rm -f /target/tmp/ti-func.sh'"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    destino = sys.argv[1]
    if not os.path.isdir(destino):
        sys.exit(f"Pasta não existe: {destino}")
    if not os.path.isdir(os.path.join(destino, "casper")):
        sys.exit(f"{destino} não parece o pendrive do Ubuntu (falta a pasta casper).")

    padrao = os.path.expanduser(os.path.join("~", ".ssh", "id_ed25519.pub"))
    caminho_chave = input(f"Chave SSH pública do servidor Ansible [{padrao}]: ").strip() or padrao
    with open(caminho_chave, encoding="utf-8") as f:
        chave = f.read().strip()
    if not chave.startswith("ssh-"):
        sys.exit("Isso não parece uma chave SSH pública.")

    usuario = input("Usuário da conta da TI [ti]: ").strip() or "ti"
    ti = senha("Senha da conta da TI: ", 12)
    func = input("Usuário da conta dos funcionários [usuario]: ").strip() or "usuario"
    if not re.fullmatch(r"[a-z][a-z0-9_-]{0,30}", func) or func == usuario:
        sys.exit("Conta dos funcionários: minúsculas, números, - ou _, e diferente da conta da TI.")
    comando_func = func_comando(func)

    rede = input("Wi-Fi da empresa, nome da rede [vazio = sem Wi-Fi]: ").strip()
    comando_wifi = wifi_comando(rede, senha("Senha do Wi-Fi: ", 8)) if rede else ""

    hash_ti = hash_senha(ti)

    with open(os.path.join(AQUI, "autoinstall.modelo.yaml"), encoding="utf-8") as f:
        texto = f.read()
    for marca, valor in {
        "@@TI_USUARIO@@": usuario,
        "@@TI_SENHA_HASH@@": hash_ti,
        "@@CHAVE_SSH@@": chave,
        "@@FUNC_COMANDO@@": comando_func,
    }.items():
        texto = texto.replace(marca, valor)
    if comando_wifi:
        texto = texto.replace("@@WIFI_COMANDO@@", comando_wifi)
    else:
        texto = "".join(l for l in texto.splitlines(True) if "@@WIFI_COMANDO@@" not in l and "Wi-Fi da empresa" not in l)

    saida = os.path.join(destino, "autoinstall.yaml")
    with open(saida, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print(f"Gravado: {saida}")


if __name__ == "__main__":
    main()
