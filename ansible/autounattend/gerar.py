r"""Gera o autounattend.xml do pendrive de instalação do Windows (POP-05 §4.1).

Uso:  python3 gerar.py /mnt/d      (no WSL)
      python gerar.py E:\         (no Windows)
      (pendrive feito com a Ferramenta de Criação de Mídia da Microsoft;
       ver ../README.md)

Pede a edição (Home ou Pro), a senha da conta da TI (no Vaultwarden) e o nome
da conta dos funcionários (sem senha) e grava o arquivo na raiz do pendrive.
Nada fica nesta pasta.
"""
import base64
import getpass
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

# Chaves genéricas de instalação da Microsoft: só escolhem a edição, não ativam.
CHAVES = {
    "home": "YTMG3-N6DKC-DKB77-7M9GH-8HVX7",
    "pro": "VK7JG-NPHTM-C97JM-9MPGT-3V66T",
}


def senha(pergunta, minimo):
    while True:
        s = getpass.getpass(pergunta)
        if len(s) < minimo:
            print(f"  Mínimo de {minimo} caracteres.")
        elif s != getpass.getpass("  Repita: "):
            print("  As senhas não conferem.")
        else:
            return s


def nome_conta(pergunta, padrao):
    nome = input(pergunta).strip() or padrao
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,20}", nome):
        sys.exit("Usuário só com letras, números, ponto, hífen ou sublinhado (até 20).")
    return nome


def codificar(s):
    """Formato do Windows para senha de conta local no autounattend (não é criptografia)."""
    return base64.b64encode((s + "Password").encode("utf-16-le")).decode("ascii")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    destino = sys.argv[1]
    if not os.path.isdir(destino):
        sys.exit(f"Pasta não existe: {destino}")
    fontes = os.path.join(destino, "sources")
    if not any(os.path.exists(os.path.join(fontes, f)) for f in ("install.wim", "install.esd", "install.swm")):
        sys.exit(f"{destino} não parece o pendrive do Windows (falta sources/install.wim ou .esd).")

    edicao = ""
    while edicao not in CHAVES:
        edicao = (input("Edição do Windows (home/pro) [pro]: ").strip().lower() or "pro")

    usuario = nome_conta("Usuário da conta da TI [ti]: ", "ti")
    ti = codificar(senha("Senha da conta da TI: ", 12))
    func = nome_conta("Usuário da conta dos funcionários [usuario]: ", "usuario")
    if func.lower() == usuario.lower():
        sys.exit("A conta dos funcionários precisa ter outro nome.")

    with open(os.path.join(AQUI, "autounattend.modelo.xml"), encoding="utf-8") as f:
        texto = f.read()
    for marca, valor in {
        "@@CHAVE_EDICAO@@": CHAVES[edicao],
        "@@TI_USUARIO@@": usuario,
        "@@TI_SENHA@@": ti,
        "@@FUNC_USUARIO@@": func,
    }.items():
        texto = texto.replace(marca, valor)

    saida = os.path.join(destino, "autounattend.xml")
    with open(saida, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(texto)
    print(f"Gravado: {saida}")


if __name__ == "__main__":
    main()
