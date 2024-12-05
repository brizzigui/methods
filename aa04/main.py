# Chamador das soluções da AA04 de Métodos Numéricos Computacionais

import trapezoid
import simpson
import gauss
import values as v
import latex

import sys



def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    ####################################################
    # VERIFIQUE SE OS SEUS VALORES ESTÃO CORRETAMENTE  #
    # DEFINIDOS EM VALUES.PY                           #
    ####################################################

    latex.begin_file()

    total = 0.0
    print("\\section{Regra do Trapézio}")
    latex.begin_table()
    total += trapezoid.trapezoid_method()
    latex.end_table()
    print()
    
    print("\\section{Método de Simpson}")
    latex.begin_table()
    total += simpson.simpson_method()
    latex.end_table()
    print()

    print("\\section{Método de Gauss com 2 pontos gaussianos}")
    latex.begin_table()
    total += gauss.gauss_method_2pts()
    latex.end_table()
    print()
    
    print("\\section{Método de Gauss com 3 pontos gaussianos}")
    latex.begin_table()
    total += gauss.gauss_method_3pts()
    latex.end_table()
    print()

    print("\\section{Valor total da integral}")
    print(f"Somando as quatro contribuições, obtém-se o valor numérico da integral definida A: \\\\\n")
    print("\\centering")
    print(f"$A = {total:.10g}$")

    latex.end_file()
    

if __name__ == "__main__":
    main()