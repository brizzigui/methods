import scipy.integrate
import scipy.special
import latex
import values as v
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

def make_q1_graph(linear_coeficients: list, square_coeficient: list) -> None:
    plt.scatter(v.q1_x, v.q1_y, color="#6784eb")

    x = np.linspace(0, 30)
    y = [linear_coeficients[0] + k*linear_coeficients[1] for k in x]
    plt.plot(x, y, color="#8447c9")

    y = [square_coeficient[0] + k*square_coeficient[1] + (k**2)*square_coeficient[2] for k in x]
    plt.plot(x, y, color="#de67eb")

    plt.text(16, 21, "y = a0 + a1*x", color="#8447c9")
    plt.text(16, 16, "y = a0 + a1*x + a2*x^2", color="#de67eb")

    plt.savefig("./images/q1_graph.png", dpi=600)
    plt.clf()

def make_q2_pt1_graph(coeficients: list) -> None:
    plt.scatter(v.q2_A_x, v.q2_A_y, color="#6784eb")

    x = np.linspace(10, 40)
    y = [coeficients[0] * (coeficients[1]**k) for k in x]
    plt.plot(x, y, color="#8447c9")
    ax = plt.gca()
    ax.set_yscale("log")

    plt.text(30, 30, "y = a * b^x", color="#8447c9")

    plt.savefig("./images/q2_pt1_graph.png", dpi=600)
    plt.clf()

def make_q2_pt2_graph(coeficients: list) -> None:
    plt.scatter(v.q2_B_x, v.q2_B_y, color="#6784eb")
    x = np.linspace(10, 45)
    y = [coeficients[0] * (k**coeficients[1]) for k in x]
    plt.plot(x, y, color="#8447c9")
    ax = plt.gca()
    ax.set_yscale("log")
    ax.set_xscale("log")

    plt.text(12.5, 45, "y = a * x^b", color="#8447c9")

    plt.savefig("./images/q2_pt2_graph.png", dpi=600)
    plt.clf()

def polynomial_least_squares() -> None:
    latex.begin_table(8, "$k$ & $x_{k}$ & $y_{k}$ & $x_{k}^2$ & $x_{k}^3$ & $x_{k}^4$ & $y_{k}x_{k}$ & $y_{k}x_{k}^2$\\\\")

    sum_x = 0
    sum_y = 0
    sum_x_sq = 0
    sum_x_cub = 0
    sum_x_dp_sq = 0
    sum_y_times_x = 0
    sum_y_times_x_sq = 0

    for k in range(len(v.q1_x)):
        sum_x += v.q1_x[k]
        sum_y += v.q1_y[k]
        sum_x_sq += v.q1_x[k]**2
        sum_x_cub += v.q1_x[k]**3
        sum_x_dp_sq += v.q1_x[k]**4
        sum_y_times_x += v.q1_x[k]*v.q1_y[k]
        sum_y_times_x_sq += (v.q1_x[k]**2)*v.q1_y[k]

        print(f"{k+1} & {v.q1_x[k]:.6g}  & {v.q1_y[k]:.6g} & {v.q1_x[k]**2:.6g} & {v.q1_x[k]**3:.6g} & {v.q1_x[k]**4:.6g}  & {v.q1_x[k]*v.q1_y[k]:.6g} & {(v.q1_x[k]**2)*v.q1_y[k]:.6g} \\\\")

    print("\\hline")
    print(f"$\\Sigma$ & {sum_x:.6g}  & {sum_y:.6g} & {sum_x_sq:.6g} & {sum_x_cub:.6g} & {sum_x_dp_sq:.6g}  & {sum_y_times_x:.6g} & {sum_y_times_x_sq:.6g} \\\\")
    latex.end_table()


    print("\\hrule")
    print("\\vspace{0.2cm}")
    print("\\textbf{Ajuste Linear}")
    lin_ak = [(sum_x_sq * sum_y - sum_y_times_x * sum_x)/(len(v.q1_x)*sum_x_sq-(sum_x**2)),(len(v.q1_x) * sum_y_times_x - sum_x * sum_y)/(len(v.q1_x)*sum_x_sq-(sum_x**2))]
    print(f"\n\n$a_{{0}} = {lin_ak[0]:.6g}$")
    print(f"\n\n$a_{{1}} = {lin_ak[1]:.6g}$")

    latex.add_line()
    print("\\textbf{Ajuste Quadrático}")
    print(f"\n\n${len(v.q1_x)}a_{{0}} + {sum_x:.6g}a_{{1}} + {sum_x_sq:.6g}a_{{2}} = {sum_y:.6g}$")
    print(f"\n\n${sum_x:.6g}a_{{0}} + {sum_x_sq:.6g}a_{{1}} + {sum_x_cub:.6g}a_{{2}} = {sum_y_times_x:.6g}$")
    print(f"\n\n${sum_x_sq:.6g}a_{{0}} + {sum_x_cub:.6g}a_{{1}} + {sum_x_dp_sq:.6g}a_{{2}} = {sum_y_times_x_sq:.6g}$")
    print("\\vspace{0.2cm}")
    solution = np.linalg.solve([[len(v.q1_x), sum_x, sum_x_sq], [sum_x, sum_x_sq, sum_x_cub], [sum_x_sq, sum_x_cub, sum_x_dp_sq]], [sum_y, sum_y_times_x, sum_y_times_x_sq])
    print(f"\n\n$a_{{0}} = {solution[0]:.6g}$")
    print(f"\n\n$a_{{1}} = {solution[1]:.6g}$")
    print(f"\n\n$a_{{2}} = {solution[2]:.6g}$")


    latex.add_line()
    print("\\begin{center}")
    print("\\textbf{Gráfico}")
    print("\n\n\\includegraphics[width=8cm]{q1_graph.png}")
    print("\\end{center}")
    make_q1_graph(lin_ak, solution)

def exponential_fitting() -> None:
    print("\\subsection{Ajuste Exponencial}")
    latex.begin_table(5, "$k$ & $x_{k}$ & $log y_{k}$ & $x_{k}^2$ & $x_{k}log y_{k}$\\\\")

    sum_x = 0
    sum_log_y = 0
    sum_x_sq = 0
    sum_x_log_y = 0

    for k in range(len(v.q2_A_x)):
        sum_x += v.q2_A_x[k]
        sum_log_y += math.log(v.q2_A_y[k])
        sum_x_sq += v.q2_A_x[k]**2
        sum_x_log_y += v.q2_A_x[k] * math.log(v.q2_A_y[k])

        print(f"{k+1} & {v.q2_A_x[k]:.6g} & {math.log(v.q2_A_y[k]):.6g} & {v.q2_A_x[k]**2:.6g} & {v.q2_A_x[k] * math.log(v.q2_A_y[k]):.6g} \\\\")

    print("\\hline")
    print(f"$\\Sigma$ & {sum_x:.6g}  & {sum_log_y:.6g} & {sum_x_sq:.6g} & {sum_x_log_y:.6g} \\\\")
    latex.end_table()

    latex.add_line()
    print("\\textbf{Ajuste Linear}")
    lin_ak = [(sum_x_sq * sum_log_y - sum_x_log_y * sum_x)/(len(v.q2_A_x)*sum_x_sq-(sum_x**2)),(len(v.q2_A_x) * sum_x_log_y - sum_x * sum_log_y)/(len(v.q2_A_x)*sum_x_sq-(sum_x**2))]
    print(f"\n\n$a_{{0}} = {lin_ak[0]:.6g}$")
    print(f"\n\n$a_{{1}} = {lin_ak[1]:.6g}$")

    latex.add_line()
    print("\\textbf{Ajuste Exponencial}")
    print(f"\n\n$a = e^{{a_{{0}}}} = {math.exp(lin_ak[0]):.6g}$")
    print(f"\n\n$b = e^{{a_{{1}}}} = {math.exp(lin_ak[1]):.6g}$")

    latex.add_line()
    print("\\textbf{Gráfico}")
    print("\\begin{center}")
    print("\n\n\\includegraphics[width=10cm]{q2_pt1_graph.png}")
    print("\\end{center}")
    make_q2_pt1_graph([math.exp(lin_ak[0]), math.exp(lin_ak[1])])

def power_fitting() -> None:
    print("\\newpage")
    print("\\subsection{Ajuste Potência}")
    latex.begin_table(5, "$k$ & $log x_{k}$ & $log y_{k}$ & $log^2 x_{k}$ & $log y_{k} log x_{k}$\\\\")

    sum_log_x = 0
    sum_log_y = 0
    sum_log_x_sq = 0
    sum_log_x_log_y = 0

    for k in range(len(v.q2_A_x)):
        sum_log_x += math.log(v.q2_B_x[k])
        sum_log_y += math.log(v.q2_B_y[k])
        sum_log_x_sq += math.log(v.q2_B_x[k])**2
        sum_log_x_log_y += math.log(v.q2_B_x[k]) * math.log(v.q2_B_y[k])

        print(f"{k+1} & {math.log(v.q2_B_x[k]):.6g} & {math.log(v.q2_B_y[k]):.6g} & {math.log(v.q2_B_x[k])**2:.6g} & {math.log(v.q2_B_x[k]) * math.log(v.q2_B_y[k]):.6g} \\\\")

    print("\\hline")
    print(f"$\\Sigma$ & {sum_log_x:.6g}  & {sum_log_y:.6g} & {sum_log_x_sq:.6g} & {sum_log_x_log_y:.6g} \\\\")
    latex.end_table()

    latex.add_line()
    print("\\textbf{Ajuste Linear}")
    lin_ak = [(sum_log_x_sq * sum_log_y - sum_log_x_log_y * sum_log_x)/(len(v.q2_B_x)*sum_log_x_sq-(sum_log_x**2)),(len(v.q2_B_x) * sum_log_x_log_y - sum_log_x * sum_log_y)/(len(v.q2_B_x)*sum_log_x_sq-(sum_log_x**2))]
    print(f"\n\n$a_{{0}} = {lin_ak[0]:.6g}$")
    print(f"\n\n$a_{{1}} = {lin_ak[1]:.6g}$")

    latex.add_line()
    print("\\textbf{Ajuste Potência}")
    print(f"\n\n$a = e^{{a_{{0}}}} = {math.exp(lin_ak[0]):.6g}$")
    print(f"\n\n$b = a_{{1}} = {lin_ak[1]:.6g}$")

    latex.add_line()
    print("\\textbf{Gráfico}")
    print("\\begin{center}")
    print("\n\n\\includegraphics[width=10cm]{q2_pt2_graph.png}")
    print("\\end{center}")
    make_q2_pt2_graph([math.exp(lin_ak[0]), lin_ak[1]])

def approximated_function(a : list, x : float, N: int) -> float:
    return sum(a[n] * scipy.special.legendre(n)(x) for n in range(N + 1))

def plot_legendre_method(a : list, N: int) -> None:
    for degree in range(0, N+1, 2):
        x = np.linspace(-1, 1, 1000)
        y = [approximated_function(a, k, degree) for k in x]
        plt.plot(x, y, color="#8447c9")

        y = [v.q3_function(k) for k in x]
        plt.plot(x, y, color="#de67eb")

        plt.gca().set_xlim(-1, 1)
        plt.gca().set_ylim(-1.75, 1.75)

        plt.text(-0.9, 0.5, f"y = P{degree}(x)", color="#8447c9")
        plt.text(0.0, 1.25, "y = f(x)", color="#de67eb")

        plt.savefig(f"./images/q3_P{degree}_graph.png", dpi=600)
        plt.clf()

def legendre_method() -> None:
    print("\\subsection{Polinômios de Legendre}")
    latex.begin_table(4, "$k$ & $a_{k}$ & $EA{k}^{(g)}$ & $ER{k}^{(g)}$\\\\")

    n = 10
    A = [0] * (n+1)
    eA = [0] * (n+1)
    eR = [0] * (n+1)

    legendre = [scipy.special.legendre(k) for k in range(n+1)]

    for k in range(n+1):
        poly = legendre[k]

        inner_integral_term = lambda x: v.q3_function(x) * poly(x)
        result = scipy.integrate.quad(inner_integral_term, -1, 1)[0]

        A[k] = ((2*k + 1) / 2 * result)

        if k == 0:
            print(f"{k+1} & {A[k]} & - & - \\\\")

        else:
            eA[k] = 2 * A[k] ** 2 / (2 * k + 1)
            eR[k] = eA[k] / sum([2 * A[j] ** 2 / (2 * j + 1) for j in range(n+1)])
            print(f"{k+1} & {A[k]} & {eA[k]} & {eR[k]} \\\\")

    plot_legendre_method(A, n)
    latex.end_table()
    latex.add_line()
    print("\\textbf{Os gráficos se encontram na página seguinte.}")
    print("\\newpage")
    latex.write_legendre_figs()
    print("\\newpage")


def apply_trig_method(a : list, b : list, x : float, N : int) -> float:
    return a[0]/2 + sum([a[i] * np.cos(i * math.pi * x) + b[i] * np.sin(i * math.pi * x) for i in range(1, N+1)])

def plot_trig_method(a : list, b : list, N_max : int) -> None:
    for degree in range(0, N_max+1, 2):
        x = np.linspace(-1, 1, 1000)
        y = [apply_trig_method(a, b, k, degree) for k in x]
        plt.plot(x, y, color="#8447c9")

        y = [v.q3_function(k) for k in x]
        plt.plot(x, y, color="#de67eb")

        plt.gca().set_xlim(-1, 1)
        plt.gca().set_ylim(-1.75, 1.75)

        plt.text(-0.9, 0.5, f"y = S{degree}(x)", color="#8447c9")
        plt.text(0.0, 1.25, "y = f(x)", color="#de67eb")

        plt.savefig(f"./images/q3_S{degree}_graph.png", dpi=600)
        plt.clf()

def trigonometric_method() -> None:
    print("\\subsection{Polinômios Trigonométricos}")
    latex.begin_table(5, "$k$ & $a_{k}$ & $b_{k}$ & $EA{k}^{(g)}$ & $ER{k}^{(g)}$\\\\")

    N = 10
    a = []
    b = []

    for k in range(N+1):
        if k == 0:
            func = lambda x: v.q3_function(x)
            ak = scipy.integrate.quad(func, -1, 1)[0]

        else:
            func = lambda x: np.cos(math.pi * k * x) * v.q3_function(x)
            ak = scipy.integrate.quad(func, -1, 1)[0]

        func = lambda x: np.sin(math.pi * k * x) * v.q3_function(x)
        bk = scipy.integrate.quad(func, -1, 1)[0]
        
        a.append(ak)
        b.append(bk)
        
        if k != 0:
            func = lambda x: (apply_trig_method(a, b, x, k) - apply_trig_method(a, b, x, k-1))**2
            EAk = scipy.integrate.quad(func, -1, 1)[0]

            ERk = (a[k]**2 + b[k]**2) / ((a[0]**2/4) + sum([a[m]**2 + b[m]**2 for m in range(1, k+1)])) 
            print(f"{k+1} & {ak:.6g} & {bk:.6g} & {EAk:.6g} & {ERk:.6g} \\\\")         

        else:
            print(f"{k+1} & {ak:.6g} & {bk:.6g} & - & - \\\\")

    latex.end_table()
    latex.add_line()
    print("\\textbf{Os gráficos se encontram na página seguinte.}")
    plot_trig_method(a, b, N)
    print("\\newpage")
    latex.write_trig_figs()



def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    latex.begin_file()

    latex.section("Questão 1")
    polynomial_least_squares()

    print("\\newpage")
    latex.section("Questão 2")
    exponential_fitting()
    power_fitting()

    print("\\newpage")
    latex.section("Questão 3")
    legendre_method()
    trigonometric_method()

    latex.end_file()


if __name__ == "__main__":
    main()