// Gera impressao/POPs-RH-revisao.docx: os documentos que o RH revisa, num Word so,
// com "Controlar alteracoes" ja ligado (cada correcao do RH vira sugestao para aceitar ou recusar).
//
// Uso:  cd tools && npm install && node gerar-docx.mjs
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";
import {
  AlignmentType, BorderStyle, Document, Footer, HeadingLevel, LevelFormat, Packer, PageBreak,
  PageNumber, Paragraph, ShadingType, Table, TableCell, TableRow, TextRun, WidthType,
} from "docx";

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ARQUIVOS = [
  "POPs/POP-01-entrada.md",
  "POPs/POP-02-saida.md",
  "POPs/POP-11-funcionario-ativo.md",
  "anexos/padrao-email.md",
  "anexos/formularios.md",
];
const SAIDA = path.join(RAIZ, "impressao", "POPs-RH-revisao.docx");

const FONTE = "Calibri";
const LARGURA = 9638; // A4 com margens de 2 cm, em DXA
const CINZA = "999999";

// ---------- texto em linha ----------

function limparEntidades(t) {
  return t.replace(/&nbsp;/g, " ").replace(/&middot;/g, "·").replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'");
}

function runs(tokens, estilo = {}) {
  const saida = [];
  for (const t of tokens || []) {
    switch (t.type) {
      case "strong": saida.push(...runs(t.tokens, { ...estilo, bold: true })); break;
      case "em": saida.push(...runs(t.tokens, { ...estilo, italics: true })); break;
      case "del": saida.push(...runs(t.tokens, { ...estilo, strike: true })); break;
      case "codespan": saida.push(new TextRun({ ...estilo, text: limparEntidades(t.text), font: "Consolas", size: 19 })); break;
      case "link": saida.push(...runs(t.tokens, estilo)); break;
      case "br": saida.push(new TextRun({ break: 1 })); break;
      case "html": {
        const texto = limparEntidades(t.text.replace(/<[^>]+>/g, ""));
        if (texto.trim()) saida.push(new TextRun({ ...estilo, text: texto }));
        break;
      }
      case "text":
        if (t.tokens) saida.push(...runs(t.tokens, estilo));
        else saida.push(new TextRun({ ...estilo, text: limparEntidades(t.text) }));
        break;
      case "escape": saida.push(new TextRun({ ...estilo, text: t.text })); break;
      default: if (t.text) saida.push(new TextRun({ ...estilo, text: limparEntidades(t.text) }));
    }
  }
  return saida;
}

// Linhas seguidas do mesmo paragrafo (cabecalho "> ..." e formularios) viram quebras de linha.
function runsComQuebras(token) {
  const partes = [];
  for (const t of token.tokens || []) {
    if (t.type === "text" && !t.tokens && t.text.includes("\n")) {
      t.text.split("\n").forEach((linha, i) => {
        if (i > 0) partes.push({ type: "br" });
        partes.push({ type: "text", text: linha });
      });
    } else partes.push(t);
  }
  return runs(partes);
}

// ---------- blocos ----------

const HEADINGS = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 };

function celula(token, largura, cabecalho) {
  return new TableCell({
    width: { size: largura, type: WidthType.DXA },
    shading: cabecalho ? { type: ShadingType.CLEAR, color: "auto", fill: "EEEEEE" } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: runs(token.tokens, cabecalho ? { bold: true } : {}) })],
  });
}

function tabela(t) {
  const n = t.header.length;
  // Coluna de texto longo ganha mais espaco: peso pelo tamanho medio do conteudo.
  const pesos = t.header.map((h, i) => {
    const textos = [h.text, ...t.rows.map((r) => r[i]?.text || "")];
    return Math.max(6, Math.min(60, textos.reduce((a, x) => a + x.length, 0) / textos.length));
  });
  const soma = pesos.reduce((a, b) => a + b, 0);
  const larguras = pesos.map((p) => Math.floor((p / soma) * LARGURA));
  larguras[n - 1] += LARGURA - larguras.reduce((a, b) => a + b, 0);
  const borda = { style: BorderStyle.SINGLE, size: 4, color: CINZA };
  return new Table({
    width: { size: LARGURA, type: WidthType.DXA },
    columnWidths: larguras,
    borders: { top: borda, bottom: borda, left: borda, right: borda, insideHorizontal: borda, insideVertical: borda },
    rows: [
      new TableRow({ tableHeader: true, children: t.header.map((h, i) => celula(h, larguras[i], true)) }),
      ...t.rows.map((r) => new TableRow({ children: r.map((c, i) => celula(c, larguras[i], false)) })),
    ],
  });
}

// Listas numeradas usam o numero escrito no markdown: os passos dos POPs continuam
// de uma secao para a outra (4.2 comeca no 3), e a numeracao do Word recomecaria do 1.
function lista(t, nivel, saida) {
  const inicio = t.ordered ? Number(t.start || 1) : 0;
  t.items.forEach((item, indice) => {
    let primeiro = true;
    for (const filho of item.tokens) {
      if (filho.type === "list") { lista(filho, nivel + 1, saida); continue; }
      const conteudo = filho.type === "text" || filho.type === "paragraph" ? runs(filho.tokens || [{ type: "text", text: filho.text }]) : runs([filho]);
      if (primeiro && t.ordered) {
        saida.push(new Paragraph({
          indent: { left: 720 * (nivel + 1), hanging: 400 },
          tabStops: [{ type: "left", position: 720 * (nivel + 1) }],
          children: [new TextRun({ text: `${inicio + indice}.\t` }), ...conteudo],
        }));
        primeiro = false;
      } else if (primeiro) {
        saida.push(new Paragraph({
          numbering: { reference: "marcadores", level: nivel },
          children: conteudo,
        }));
        primeiro = false;
      } else {
        saida.push(new Paragraph({ indent: { left: 720 * (nivel + 1) }, children: conteudo }));
      }
    }
  });
}

function blocos(tokens, ehFormulario) {
  const saida = [];
  for (const t of tokens) {
    switch (t.type) {
      case "heading":
        if (ehFormulario && t.depth === 2 && t.text.startsWith("Formulário")) saida.push(new Paragraph({ children: [new PageBreak()] }));
        saida.push(new Paragraph({ heading: HEADINGS[t.depth] || HeadingLevel.HEADING_4, children: runs(t.tokens) }));
        break;
      case "paragraph":
        saida.push(new Paragraph({ spacing: { after: 120 }, children: ehFormulario ? runsComQuebras(t) : runs(t.tokens) }));
        break;
      case "blockquote":
        for (const p of t.tokens.filter((x) => x.type === "paragraph")) {
          saida.push(new Paragraph({
            spacing: { after: 160 },
            indent: { left: 240 },
            border: { left: { style: BorderStyle.SINGLE, size: 12, color: CINZA, space: 8 } },
            children: runsComQuebras(p).map((r) => r),
          }));
        }
        break;
      case "list":
        lista(t, 0, saida);
        break;
      case "table": saida.push(tabela(t)); saida.push(new Paragraph({ children: [] })); break;
      case "html": {
        const texto = limparEntidades(t.text.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ")).trim();
        if (texto) saida.push(new Paragraph({
          spacing: { before: 120, after: 120 },
          border: { top: { style: BorderStyle.DASHED, size: 4, color: CINZA, space: 4 }, bottom: { style: BorderStyle.DASHED, size: 4, color: CINZA, space: 4 } },
          children: [new TextRun({ text: texto, italics: true, color: "555555" })],
        }));
        break;
      }
      case "code": saida.push(new Paragraph({ children: [new TextRun({ text: t.text, font: "Consolas", size: 19 })] })); break;
      default: break; // hr e espacos: o espacamento dos paragrafos ja separa
    }
  }
  return saida;
}

// ---------- documento ----------

const secoes = ARQUIVOS.map((nome, i) => {
  const texto = fs.readFileSync(path.join(RAIZ, nome), "utf8");
  const filhos = blocos(marked.lexer(texto), nome.endsWith("formularios.md"));
  return {
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "Revisão RH · página ", size: 16, color: "777777" }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "777777" })],
        })],
      }),
    },
    children: filhos,
  };
});

const niveis = (formato, texto) => [0, 1, 2].map((nivel) => ({
  level: nivel, format: formato, text: texto(nivel), alignment: AlignmentType.LEFT,
  style: { paragraph: { indent: { left: 720 * (nivel + 1), hanging: 360 } } },
}));

const doc = new Document({
  creator: "TI Grupo Vale da Serra",
  title: "POPs de TI: revisão do RH",
  features: { trackRevisions: true },
  styles: {
    default: { document: { run: { font: FONTE, size: 21 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 34, bold: true, font: FONTE }, paragraph: { spacing: { before: 0, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, font: FONTE }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 22, bold: true, font: FONTE }, paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "marcadores", levels: niveis(LevelFormat.BULLET, (n) => ["•", "◦", "▪"][n]) },
    ],
  },
  sections: secoes,
});

fs.mkdirSync(path.dirname(SAIDA), { recursive: true });
fs.writeFileSync(SAIDA, await Packer.toBuffer(doc));
console.log(`Gerado: ${SAIDA}`);
