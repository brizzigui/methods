def begin_table(columns: int, column_definition : str) -> None:
    print("\\begin{table}[h!]")
    print("\\centering")
    string = "|c" * columns + "|"
    print("\\begin{tabular}{" + string + "}")
    print("\\hline")
    print(column_definition)
    print("\\hline")

def end_table() -> None:
    print("\\hline")
    print("\\end{tabular}")
    print("\\label{tab:data_table}")
    print("\\end{table}")

def section(name : str) -> None:
    print(f"\\section{{{name}}}")

def begin_file() -> None:
    string = '''\\documentclass{article}
\\usepackage{amsmath}
\\usepackage[left=1cm, right=1cm, top=1cm, bottom=2cm]{geometry}
\\usepackage{graphicx} % Required for inserting images
\\usepackage[portuguese]{babel}
\\usepackage{float}

\\title{AA05 - Métodos Numéricos Computacionais}
\\author{Guilherme Brizzi}
\\date{}

\\begin{document}

\\maketitle    
'''
    print(string)

def end_file() -> None:
    print("\\end{document}")

def add_line() -> None:
    print("\\vspace{1cm}")
    print("\\hrule")
    print("\\vspace{0.2cm}")

def write_legendre_figs() -> None:
    string = f'''
\\begin{{figure}}[H]
    \\centering
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P0_graph.png}}
        \\caption{{$P_{{0}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P2_graph.png}}
        \\caption{{$P_{{2}}(x)$}}
    \\end{{minipage}}

    \\vspace{{1em}}

    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P4_graph.png}}
        \\caption{{$P_{{4}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P6_graph.png}}
        \\caption{{$P_{{6}}(x)$}}
    \\end{{minipage}}

    \\vspace{{1em}}


    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P8_graph.png}}
        \\caption{{$P_{{8}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_P10_graph.png}}
        \\caption{{$P_{{10}}(x)$}}
    \\end{{minipage}}
\\end{{figure}}
'''
    
    print(string)

def write_trig_figs() -> None:
    string = f'''
\\begin{{figure}}[H]
    \\centering
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S0_graph.png}}
        \\caption{{$S_{{0}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S2_graph.png}}
        \\caption{{$S_{{2}}(x)$}}
    \\end{{minipage}}

    \\vspace{{1em}}

    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S4_graph.png}}
        \\caption{{$S_{{4}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S6_graph.png}}
        \\caption{{$S_{{6}}(x)$}}
    \\end{{minipage}}

    \\vspace{{1em}}


    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S8_graph.png}}
        \\caption{{$S_{{8}}(x)$}}
    \\end{{minipage}}%
    \\hspace{{0.05\\textwidth}}
    \\begin{{minipage}}{{0.45\\textwidth}}
        \\centering
        \\includegraphics[width=\\textwidth]{{q3_S10_graph.png}}
        \\caption{{$S_{{10}}(x)$}}
    \\end{{minipage}}
\\end{{figure}}
'''
    
    print(string)