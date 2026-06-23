import re
import os

def escape_tex(text, is_cell=False):
    # If it's a URL in a href, we don't want to escape its structure, but we do for display text.
    # We will do inline markdown-to-latex replacements later.
    # First, escape standard LaTeX characters:
    # & % $ # _ { } ~ ^ \
    # We must be careful not to escape backslashes that we introduce ourselves.
    
    # We will replace them with placeholders or do standard replacements:
    replacements = [
        ('\\', '\\textbackslash{}'),
        ('%', '\\%'),
        ('$', '\\$'),
        ('#', '\\#'),
        ('_', '\\_'),
        ('{', '\\{'),
        ('}', '\\}'),
        ('~', '\\textasciitilde{}'),
        ('^', '\\textasciicircum{}'),
    ]
    
    # For & (ampersand):
    # In table cells, & is the column separator, so we shouldn't escape it if it's the cell separator.
    # But if is_cell=True, the ampersand inside the cell content must be escaped!
    if is_cell:
        replacements.append(('&', '\\&'))
    else:
        # For general text, ampersands should be escaped.
        replacements.append(('&', '\\&'))
        
    s = text
    for old, new in replacements:
        # Don't escape backslash if it's already part of a LaTeX command we're building,
        # but since we run escape_tex on raw text before converting markdown syntax,
        # we can safely do it.
        s = s.replace(old, new)
    return s

def convert_inline(text):
    # Converts markdown inline formatting to LaTeX
    # **bold** -> \textbf{bold}
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    # *italic* -> \textit{italic}
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    # Inline code `code` -> \texttt{code}
    text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', text)
    # Links [text](url) -> \href{url}{text}
    # Wait, the URL shouldn't have escaped underscores or % in hyperref, but let's make sure it's unescaped
    def replace_link(match):
        label = match.group(1)
        url = match.group(2)
        # Restore URL special characters if they were escaped
        url = url.replace('\\_', '_').replace('\\%', '%').replace('\\&', '&').replace('\\#', '#')
        return f"\\href{{{url}}}{{{label}}}"
    
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)
    return text

def parse_markdown_table(lines, caption=None, label=None):
    if not lines:
        return ""
    
    # Parse header
    header_cells = [cell.strip() for cell in lines[0].split('|')[1:-1]]
    num_cols = len(header_cells)
    
    # Parse alignment from separator row (lines[1])
    align_cells = [cell.strip() for cell in lines[1].split('|')[1:-1]]
    col_aligns = []
    for cell in align_cells:
        if cell.startswith(':') and cell.endswith(':'):
            col_aligns.append('c')
        elif cell.endswith(':'):
            col_aligns.append('r')
        else:
            col_aligns.append('l')
            
    col_spec = "".join(col_aligns)
    
    # Parse data rows
    data_rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        # Pad cells if row has fewer columns
        while len(cells) < num_cols:
            cells.append("")
        cells = cells[:num_cols]
        # Escape and format each cell
        escaped_cells = [convert_inline(escape_tex(cell, is_cell=True)) for cell in cells]
        data_rows.append(" & ".join(escaped_cells) + " \\\\")
        
    # Build LaTeX table
    tex = []
    tex.append("\\begin{table}[H]")
    tex.append("\\centering")
    if caption:
        tex.append(f"\\caption{{{caption}}}")
    if label:
        tex.append(f"\\label{{{label}}}")
    
    # For very wide tables (e.g., Table 1 has 11 columns, Table 8, etc.), wrap in resizebox
    is_wide = num_cols > 5
    if is_wide:
        tex.append("\\resizebox{\\textwidth}{!}{%")
        
    tex.append(f"\\begin{{tabular}}{{{col_spec}}}")
    tex.append("\\toprule")
    
    # Format header
    escaped_headers = [convert_inline(escape_tex(h, is_cell=True)) for h in header_cells]
    tex.append(" & ".join(escaped_headers) + " \\\\")
    tex.append("\\midrule")
    
    # Add data rows
    for row in data_rows:
        tex.append(row)
        
    tex.append("\\bottomrule")
    tex.append("\\end{tabular}")
    
    if is_wide:
        tex.append("}") # Close resizebox
        
    tex.append("\\end{table}")
    return "\n".join(tex)

def main():
    filepath = "Juneau_2026.md"
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Split content into paragraphs/blocks by double newlines
    blocks = re.split(r'\n\n+', content)
    
    tex_body = []
    
    # Metadata variables
    title = ""
    author = ""
    affiliation = ""
    email = ""
    date = ""
    keywords = ""
    abstract_paragraphs = []
    
    in_abstract = False
    in_references = False
    in_appendix = False
    in_supplement = False
    in_list = False
    list_type = None # 'itemize' or 'enumerate'
    
    # Track the last paragraph to see if it was a table caption
    last_paragraph_text = ""
    last_table_index = 1
    
    for block in blocks:
        block_stripped = block.strip()
        if not block_stripped:
            continue
            
        # Check if block is a heading
        heading_match = re.match(r'^(#+)\s+(.*)$', block_stripped)
        if heading_match:
            # If we were in a list, close it
            if in_list:
                tex_body.append(f"\\end{{{list_type}}}")
                in_list = False
                list_type = None
                
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            
            if level == 1:
                # Main titles
                if heading_text.lower() == "abstract":
                    in_abstract = True
                elif "can llms assess risk of bias" in heading_text.lower():
                    title = heading_text
                else:
                    # Treat other h1 as section
                    escaped_heading = convert_inline(escape_tex(heading_text))
                    tex_body.append(f"\\section{{{escaped_heading}}}")
            elif level == 2:
                # Sections
                in_abstract = False
                if heading_text.lower() == "references":
                    in_references = True
                    tex_body.append("\\section*{References}")
                else:
                    in_references = False
                    if "appendix a" in heading_text.lower():
                        in_appendix = True
                        tex_body.append("\\appendix")
                        escaped_heading = convert_inline(escape_tex(heading_text))
                        tex_body.append(f"\\section{{{escaped_heading}}}")
                    elif heading_text.lower() == "supplement":
                        in_supplement = True
                        escaped_heading = convert_inline(escape_tex(heading_text))
                        tex_body.append(f"\\section{{{escaped_heading}}}")
                    else:
                        escaped_heading = convert_inline(escape_tex(heading_text))
                        tex_body.append(f"\\section{{{escaped_heading}}}")
            elif level == 3:
                escaped_heading = convert_inline(escape_tex(heading_text))
                tex_body.append(f"\\subsection{{{escaped_heading}}}")
            elif level == 4:
                escaped_heading = convert_inline(escape_tex(heading_text))
                tex_body.append(f"\\subsubsection{{{escaped_heading}}}")
                
            continue
            
        # Check if block is a table
        if block_stripped.startswith('|'):
            # If we were in a list, close it
            if in_list:
                tex_body.append(f"\\end{{{list_type}}}")
                in_list = False
                list_type = None
                
            lines = block_stripped.split('\n')
            
            # Determine caption and label
            caption = None
            label = None
            
            # If the last paragraph text looked like a table caption:
            # e.g., "**Table 1. Risk of bias...**"
            caption_match = re.match(r'^\*\*Table\s+(\w+)\.\s*(.*?)\*\*$', last_paragraph_text.strip())
            if caption_match:
                table_num = caption_match.group(1)
                table_title = caption_match.group(2)
                caption = f"Table {table_num}. {table_title}"
                label = f"tab:table{table_num}"
                # Remove the caption paragraph from the body if it was added
                if tex_body and tex_body[-1].strip().startswith(f"\\textbf{{Table {table_num}."):
                    tex_body.pop()
            else:
                # If there's no Table X caption, but it's a small supplement table
                # The last paragraph might just be the name of the criterion, like "Representative study group"
                if in_supplement:
                    caption = last_paragraph_text.replace("**", "").replace("*", "").strip()
                    label = f"tab:supp_{last_table_index}"
                    last_table_index += 1
                    # Remove the criterion name paragraph from body if added
                    if tex_body and len(tex_body) > 0:
                        # check if it matches the last paragraph text
                        last_body_line = tex_body[-1].strip()
                        if last_body_line.startswith("\\textbf{") or last_body_line.startswith("Representative") or last_body_line.startswith("Intervention") or last_body_line.startswith("Outcome") or last_body_line.startswith("Follow-up") or last_body_line.startswith("Important") or last_body_line.startswith("Analysis"):
                            tex_body.pop()
            
            table_tex = parse_markdown_table(lines, caption=caption, label=label)
            tex_body.append(table_tex)
            last_paragraph_text = ""
            continue
            
        # Check if block is a bullet or numbered list
        lines = block_stripped.split('\n')
        is_bullet_list = all(re.match(r'^[-*+]\s+', line.strip()) for line in lines)
        is_numbered_list = all(re.match(r'^\d+\.\s+', line.strip()) for line in lines)
        
        if is_bullet_list or is_numbered_list:
            current_list_type = 'itemize' if is_bullet_list else 'enumerate'
            
            # If list type changed or we weren't in a list, open a new list
            if not in_list:
                tex_body.append(f"\\begin{{{current_list_type}}}")
                in_list = True
                list_type = current_list_type
            elif list_type != current_list_type:
                tex_body.append(f"\\end{{{list_type}}}")
                tex_body.append(f"\\begin{{{current_list_type}}}")
                list_type = current_list_type
                
            for line in lines:
                line_stripped = line.strip()
                if is_bullet_list:
                    # Strip the bullet character
                    item_text = re.sub(r'^[-*+]\s+', '', line_stripped)
                else:
                    # Strip the number
                    item_text = re.sub(r'^\d+\.\s+', '', line_stripped)
                escaped_item = convert_inline(escape_tex(item_text))
                tex_body.append(f"\\item {escaped_item}")
                
            continue
            
        # If we reach here, it's a standard paragraph
        # If we were in a list, close it
        if in_list:
            tex_body.append(f"\\end{{{list_type}}}")
            in_list = False
            list_type = None
            
        # Check if it's metadata in the beginning
        if title == "":
            # First non-empty block should be title if not matched by h1, but we already matched # Can LLMs...
            pass
            
        # Parse author, affiliations, emails from beginning blocks
        if "carl-etienne.juneau@umontreal.ca" in block_stripped:
            email = "carl-etienne.juneau@umontreal.ca"
            # Extract ORCID and author
            author = "Carl-Etienne Juneau, PhD"
            affiliation = "Dr. Muscle AI, Sheridan, Wyoming, United States"
            date = "May 7, 2026"
            continue
        elif "Keywords:" in block_stripped:
            keywords = block_stripped.replace("**Keywords:**", "").strip()
            continue
            
        # Abstract collection
        if in_abstract:
            abstract_paragraphs.append(convert_inline(escape_tex(block_stripped)))
            continue
            
        # References parsing
        if in_references:
            # We want each reference block to be formatted as hanging indent
            escaped_ref = convert_inline(escape_tex(block_stripped))
            tex_body.append(f"\\referenceitem{{{escaped_ref}}}")
            continue
            
        # Normal paragraph
        escaped_para = convert_inline(escape_tex(block_stripped))
        tex_body.append(escaped_para)
        last_paragraph_text = block_stripped
        
    # If still in list at the end, close it
    if in_list:
        tex_body.append(f"\\end{{{list_type}}}")
        
    # Build complete LaTeX document
    tex_doc = []
    tex_doc.append("\\documentclass[11pt,a4paper]{article}")
    tex_doc.append("\\usepackage[utf8]{inputenc}")
    tex_doc.append("\\usepackage[margin=1in]{geometry}")
    tex_doc.append("\\usepackage{booktabs}")
    tex_doc.append("\\usepackage{graphicx}")
    tex_doc.append("\\usepackage{float}")
    tex_doc.append("\\usepackage{amsmath}")
    tex_doc.append("\\usepackage{amsfonts}")
    tex_doc.append("\\usepackage{amssymb}")
    tex_doc.append("\\usepackage{microtype}")
    tex_doc.append("\\usepackage{adjustbox}")
    tex_doc.append("\\usepackage[normalem]{ulem}")
    tex_doc.append("\\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}")
    
    # Custom reference style
    tex_doc.append("% Custom command for hanging indent references")
    tex_doc.append("\\newcommand{\\referenceitem}[1]{\\noindent\\hangafter=1\\hangindent=1.5em #1\\par\\medskip}")
    
    # Title & Authors
    tex_doc.append(f"\\title{{{title}}}")
    tex_doc.append(f"\\author{{{author}\\\\ \\small {affiliation} \\\\ \\small Email: \\href{{mailto:{email}}}{{{email}}}}}")
    tex_doc.append(f"\\date{{{date}}}")
    
    tex_doc.append("\\begin{document}")
    tex_doc.append("\\maketitle")
    
    # Abstract & Keywords
    if abstract_paragraphs:
        tex_doc.append("\\begin{abstract}")
        for para in abstract_paragraphs:
            tex_doc.append(para + "\n")
        tex_doc.append("\\end{abstract}")
        
    if keywords:
        tex_doc.append(f"\\noindent\\textbf{{Keywords:}} {convert_inline(escape_tex(keywords))}\\\\")
        tex_doc.append("\\vspace{0.5cm}")
        
    # Body
    for line in tex_body:
        tex_doc.append(line + "\n")
        
    tex_doc.append("\\end{document}")
    
    output_filepath = "Juneau_2026.tex"
    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(tex_doc))
        
    print(f"Success: Converted markdown to {output_filepath}")

if __name__ == "__main__":
    main()
