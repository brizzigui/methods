def begin_table() -> None:
    print("\\begin{table}[h!]")
    print("\\centering")
    print("\\begin{tabular}{|c|c|c|}")
    print("\\hline")
    print("k & $A_{k}(z)$ & $ER_{k}$ \\\\")
    print("\\hline")

def end_table() -> None:
    print("\\hline")
    print("\\end{tabular}")
    print("\\label{tab:data_table}")
    print("\\end{table}")
    print("\\newpage")

def begin_file() -> None:
    string = '''\\documentclass{article}
\\usepackage{amsmath}
\\usepackage[left=1cm, right=1cm, top=3cm, bottom=3cm]{geometry}

\\title{AA04 - Métodos Numéricos Computacionais}
\\author{Guilherme Brizzi}
\\date{}

\\begin{document}

\\maketitle    
'''
    print(string)

def end_file() -> None:
    print("\\end{document}")