"""Convert course_notes.md to PDF via LaTeX."""

import re
from pathlib import Path

MD_FILE = Path(__file__).parent / "course_notes.md"
TEX_FILE = Path(__file__).parent / "course_notes.tex"

md = MD_FILE.read_text(encoding="utf-8")

# ---------- helpers ----------

def escape(s):
    """Escape LaTeX special characters (except inside math)."""
    # Split on $...$ and $$...$$ to avoid escaping math
    parts = re.split(r'(\$\$[\s\S]*?\$\$|\$[^$]+?\$)', s)
    out = []
    for i, part in enumerate(parts):
        if part.startswith('$'):
            out.append(part)
        else:
            p = part
            p = p.replace('\\', '\\textbackslash{}')
            p = p.replace('&', '\\&')
            p = p.replace('%', '\\%')
            p = p.replace('#', '\\#')
            p = p.replace('_', '\\_')
            p = p.replace('{', '\\{')
            p = p.replace('}', '\\}')
            p = p.replace('~', '\\textasciitilde{}')
            p = p.replace('^', '\\textasciicircum{}')
            # Undo escapes inside \textbackslash
            p = p.replace('\\textbackslash\\{\\}', '\\textbackslash{}')
            out.append(p)
    return ''.join(out)


def process_inline(line):
    """Handle bold, italic, inline code, and links."""
    # inline code `...`
    line = re.sub(r'`([^`]+)`', r'\\texttt{\1}', line)
    # bold **...**
    line = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)
    # italic *...*
    line = re.sub(r'\*(.+?)\*', r'\\textit{\1}', line)
    # links [text](url) - just keep text
    line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
    return line


# ---------- convert ----------

lines = md.split('\n')
tex_lines = []
in_table = False
in_itemize = False
table_rows = []
item_lines = []

def flush_table():
    global table_rows, in_table
    if not table_rows:
        return
    # parse header
    header = table_rows[0]
    cols = [c.strip() for c in header.strip('|').split('|')]
    ncols = len(cols)
    col_spec = 'l' * ncols

    tex_lines.append('\\begin{center}')
    tex_lines.append('\\begin{tabular}{' + col_spec + '}')
    tex_lines.append('\\toprule')
    tex_lines.append(' & '.join(['\\textbf{' + process_inline(escape(c)) + '}' for c in cols]) + ' \\\\')
    tex_lines.append('\\midrule')

    for row in table_rows[2:]:  # skip header and separator
        cells = [c.strip() for c in row.strip('|').split('|')]
        tex_lines.append(' & '.join([process_inline(escape(c)) for c in cells]) + ' \\\\')

    tex_lines.append('\\bottomrule')
    tex_lines.append('\\end{tabular}')
    tex_lines.append('\\end{center}')
    tex_lines.append('')
    table_rows = []
    in_table = False

def flush_itemize():
    global item_lines, in_itemize
    if not item_lines:
        return
    tex_lines.append('\\begin{itemize}')
    for item in item_lines:
        tex_lines.append('  \\item ' + item)
    tex_lines.append('\\end{itemize}')
    tex_lines.append('')
    item_lines = []
    in_itemize = False

i = 0
while i < len(lines):
    line = lines[i]

    # Display math blocks $$...$$
    if line.strip() == '$$':
        flush_itemize()
        flush_table()
        tex_lines.append('\\[')
        i += 1
        while i < len(lines) and lines[i].strip() != '$$':
            tex_lines.append(lines[i])
            i += 1
        tex_lines.append('\\]')
        i += 1
        continue

    # Table of contents (skip - LaTeX generates its own)
    if line.strip().startswith('## Table of Contents'):
        i += 1
        while i < len(lines) and (lines[i].strip().startswith('[') or lines[i].strip().startswith('1.') or lines[i].strip() == '' or re.match(r'^\d+\.', lines[i].strip())):
            i += 1
        continue

    # Horizontal rule ---
    if re.match(r'^-{3,}\s*$', line.strip()):
        flush_itemize()
        flush_table()
        i += 1
        continue

    # Tables
    if '|' in line and not line.strip().startswith('$'):
        flush_itemize()
        cells = [c.strip() for c in line.strip().split('|')]
        # check it looks like a table row
        if len(cells) >= 3:
            in_table = True
            table_rows.append(line)
            i += 1
            continue

    if in_table and '|' not in line:
        flush_table()

    # Headers
    m = re.match(r'^(#{1,4})\s+(.*)', line)
    if m:
        flush_itemize()
        flush_table()
        level = len(m.group(1))
        title = m.group(2)
        # strip anchor links
        title = re.sub(r'\{#[^}]+\}', '', title).strip()
        title_esc = process_inline(escape(title))

        if level == 1:
            if title.startswith('Part '):
                tex_lines.append('\\part{' + title_esc + '}')
            else:
                tex_lines.append('\\chapter{' + title_esc + '}')
        elif level == 2:
            tex_lines.append('\\chapter{' + title_esc + '}')
        elif level == 3:
            tex_lines.append('\\section{' + title_esc + '}')
        elif level == 4:
            tex_lines.append('\\subsection{' + title_esc + '}')
        tex_lines.append('')
        i += 1
        continue

    # List items
    if re.match(r'^- ', line):
        if not in_itemize:
            flush_table()
            in_itemize = True
        content = line[2:].strip()
        item_lines.append(process_inline(escape(content)))
        i += 1
        continue
    elif re.match(r'^\d+\.\s', line):
        if not in_itemize:
            flush_table()
            in_itemize = True
        content = re.sub(r'^\d+\.\s*', '', line).strip()
        item_lines.append(process_inline(escape(content)))
        i += 1
        continue
    else:
        if in_itemize and line.strip() == '':
            flush_itemize()
            i += 1
            continue
        elif in_itemize and line.strip() != '':
            flush_itemize()
            # fall through to process this line

    # Blank lines
    if line.strip() == '':
        flush_table()
        tex_lines.append('')
        i += 1
        continue

    # Regular paragraph text
    flush_table()
    processed = process_inline(escape(line))
    tex_lines.append(processed)
    i += 1

flush_itemize()
flush_table()

body = '\n'.join(tex_lines)

# Fix some escaping issues in math environments
# Inside \[ ... \] and $ ... $, we need to undo text escaping
def fix_math(m):
    s = m.group(0)
    s = s.replace('\\_', '_')
    s = s.replace('\\&', '&')
    s = s.replace('\\#', '#')
    s = s.replace('\\{', '{')
    s = s.replace('\\}', '}')
    s = s.replace('\\textbackslash{}', '\\')
    s = s.replace('\\textasciicircum{}', '^')
    s = s.replace('\\textasciitilde{}', '~')
    return s

# Fix display math
body = re.sub(r'\\\[[\s\S]*?\\\]', fix_math, body)
# Fix inline math
body = re.sub(r'\$[^$]+?\$', fix_math, body)

# Build document
document = r"""\documentclass[11pt,letterpaper]{report}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue!60!black,
    urlcolor=blue!60!black,
}

\usepackage{titlesec}
\titleformat{\part}[display]
  {\centering\Huge\bfseries}
  {\partname\ \thepart}{20pt}{\Huge}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptername\ \thechapter}{20pt}{\Huge}

\title{\textbf{Investments: Course Notes}}
\author{BUSI 448}
\date{}

\begin{document}

\maketitle
\tableofcontents
\newpage

""" + body + r"""

\end{document}
"""

TEX_FILE.write_text(document, encoding="utf-8")
print(f"Wrote {TEX_FILE}")
