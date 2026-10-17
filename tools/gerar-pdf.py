"""Gera os PDFs de impressao:

- impressao/POPs-TI-completo.pdf: o plano, todos os POPs e os anexos.
- impressao/POPs-RH-revisao.pdf: so o que o RH revisa e aprova (POP-01, POP-02, POP-11, e-mail, formularios).

Uso:  python tools/gerar-pdf.py
Requer: pip install markdown, e Microsoft Edge ou Google Chrome instalado.
ALTERNATIVAS.md fica de fora de proposito: nao vai para impressao.
"""
import pathlib
import re
import shutil
import subprocess
import tempfile

import markdown

RAIZ = pathlib.Path(__file__).resolve().parent.parent

ANEXOS = ["anexos/padrao-email.md", "anexos/formularios.md"]
ANEXOS_TI = ["anexos/ferramentas.md"]
PDFS = {
    "POPs-TI-completo.pdf": ["POP-TI.md", *sorted(p.relative_to(RAIZ).as_posix() for p in (RAIZ / "POPs").glob("POP-*.md")), *ANEXOS_TI, *ANEXOS],
    "POPs-RH-revisao.pdf": ["POPs/POP-01-entrada.md", "POPs/POP-02-saida.md", "POPs/POP-11-funcionario-ativo.md", *ANEXOS],
}

# Chrome primeiro: o Edge headless deste PC sai sem erro e sem gerar o PDF.
NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "google-chrome", "chromium", "chromium-browser", "msedge",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: "Segoe UI", Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
h1 { font-size: 17pt; border-bottom: 2px solid #111; padding-bottom: 4px; margin-top: 0; }
h2 { font-size: 13pt; margin-top: 18px; }
h3 { font-size: 11pt; margin-top: 14px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; }
tr { page-break-inside: avoid; }
h2, h3 { page-break-after: avoid; }
th, td { border: 1px solid #999; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #eee; }
td:empty::after { content: "\\00a0"; }
blockquote { margin: 0 0 10px; padding: 4px 10px; border-left: 3px solid #999; color: #333; }
code { font-family: Consolas, monospace; font-size: 9.5pt; }
hr { border: 0; border-top: 1px solid #ccc; margin: 14px 0; }
a { color: inherit; text-decoration: none; }
.doc { page-break-before: always; }
.doc:first-child { page-break-before: auto; }
.form { page-break-before: always; }
"""


def para_html(texto, quebrar_formularios):
    extensoes = ["tables", "sane_lists"] + (["nl2br"] if quebrar_formularios else [])  # formularios: cada linha e um campo
    html = markdown.markdown(texto, extensions=extensoes)
    if quebrar_formularios:
        # Cada formulario numa folha propria.
        html = html.replace("<h2>Formulário", '<h2 class="form">Formulário')
    return html


def gerar(navegador, nome_pdf, arquivos):
    partes = []
    for nome in arquivos:
        texto = (RAIZ / nome).read_text(encoding="utf-8")
        texto = re.sub(r"\n---\n", "\n", texto)  # separadores viram espaco, nao linha
        texto = re.sub(r"(?m)^(>.*\S)$", r"\1  ", texto)  # cada linha do cabecalho na sua propria linha
        partes.append(f'<section class="doc">{para_html(texto, nome.endswith("formularios.md"))}</section>')
    documento = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}</body></html>'

    saida = RAIZ / "impressao" / nome_pdf
    saida.parent.mkdir(exist_ok=True)
    try:
        saida.unlink(missing_ok=True)
    except PermissionError:
        raise SystemExit(f"{saida.name} esta aberto em outro programa. Feche o PDF e rode de novo.")
    with tempfile.TemporaryDirectory() as tmp:
        html = pathlib.Path(tmp) / "pops.html"
        html.write_text(documento, encoding="utf-8")
        subprocess.run([navegador, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={tmp}",
                        f"--print-to-pdf={saida}", html.as_uri()], check=True, capture_output=True)
    if not saida.exists():
        raise SystemExit(f"O navegador nao gerou {saida}.")
    print(f"Gerado: {saida}")


def main():
    navegador = next((n for n in NAVEGADORES if pathlib.Path(n).exists() or shutil.which(n)), None)
    if not navegador:
        raise SystemExit("Edge ou Chrome nao encontrado.")
    for nome_pdf, arquivos in PDFS.items():
        gerar(navegador, nome_pdf, arquivos)


if __name__ == "__main__":
    main()
