"""Gera o autoinstall.yaml do pendrive de instalação do Linux (POP-04 §4.1).

Uso:  python gerar.py E:\
      (E: = pendrive gravado com o Rufus no modo ISO; ver ../README.md)

Pede a senha da conta da TI (no Vaultwarden) e grava o arquivo na raiz do
pendrive. Nada fica nesta pasta.
"""
import getpass
import os
import shutil
import subprocess
import sys

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

    hash_ti = subprocess.run(
        [openssl(), "passwd", "-6", "-stdin"], input=ti, capture_output=True, text=True, check=True
    ).stdout.strip()

    with open(os.path.join(AQUI, "autoinstall.modelo.yaml"), encoding="utf-8") as f:
        texto = f.read()
    for marca, valor in {
        "@@TI_USUARIO@@": usuario,
        "@@TI_SENHA_HASH@@": hash_ti,
        "@@CHAVE_SSH@@": chave,
    }.items():
        texto = texto.replace(marca, valor)

    saida = os.path.join(destino, "autoinstall.yaml")
    with open(saida, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print(f"Gravado: {saida}")


if __name__ == "__main__":
    main()
