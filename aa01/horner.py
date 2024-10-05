# Implementação do método de Horner para encontrar zeros de funções

def print_coeficients(a_size: int, b_list: list, c_list: list) -> None:
    # Impressão formatada dos coeficientes

    print("## Coeficientes bi do Polinômio f(x)")
    print("| k | ", end="")
    for i in range(a_size):
        print(f"b{i},k |", end="")
    print()
    print("|", end="")
    for i in range(a_size+1):
        print(f"-|", end="")
    print()

    for k, item in enumerate(b_list):
        print(f"| {k} |", end="")
        for value in item:
            print(f"{value:.9e}| ", end="")
        print()

    print("## Coeficientes ci do Polinômio f(x)")
    print("| k | ", end="")
    for i in range(a_size-1, 0, -1):
        print(f"c{i},k |", end="")
    print()
    print("|", end="")
    for i in range(a_size):
        print(f"-|", end="")
    print()
    for k, item in enumerate(c_list):
        print(f"| {k} |", end="")
        for idx, value in enumerate(reversed(item)):
            if idx == a_size-1:
                continue

            print(f"{value:.9e}| ", end="")
        print()

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**5 - 67.1743*x**4 + 1794.09*x**3 - 23805.8*x**2 + 156873*x - 410517


def f_line(x: float) -> float:
    # Retorna o valor de f'(x)
    return 156873 - 47611.6*x + 5382.27*x**2 - 268.697*x**3 + 5*x**4


def main() -> None:
    # Chute inicial
    x = 16.5 

    b_list = []
    c_list = []

    # Coeficientes do Polinômio devem ser modificados aqui!
    a = [-410517, 156873, -23805.8, 1794.09, -67.1743, 1] 

    b = [0] * len(a)
    c = [0] * len(a)

    print("## Estimativas")
    print("| k | xk | f(xk) | f'(xk) | ERk |")
    print("| - | -- | ----- | ------ | --- |")


    idx = 0
    while True:
        print(f"| {idx:10d} | {x:.9e} | {f(x):.9e} | {f_line(x):.9e} |", end=" ")
        if idx > 0:
            relative_error = abs(x-prev)/abs(x)
            print(f" {relative_error:.9e} |")

        else:
            print(" |")

            
        if idx > 0 and relative_error < 1e-6:
            print(f"## Resultado achado: {x}")
            break


        b[-1] = a[-1]
        for k in range(len(a)-2, -1, -1):   
            b[k] = a[k] + b[k+1] * x


        c[-1] = a[-1]
        for k in range(len(a)-2, 0, -1):   
            c[k] = b[k] + c[k+1] * x

        prev = x
        x = x - b[0]/c[1]

        b_list.append(b.copy())
        c_list.append(c.copy())

        idx += 1

    print_coeficients(len(a), b_list, c_list)



if __name__ == "__main__":
    main()