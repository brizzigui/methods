# Implementação do método da bisseção para encontrar zeros de funções


import math

def function(x: float) -> float:
    return x**5 - 67.1743*x**4 + 1794.09*x**3 - 23805.8*x**2 + 156873*x - 410517


def main() -> None:
    a, b = 10, 11

    an, bn = a, b
    i = 0

    print("Método da bissecção")
    print("| n | an | xn | bn | f(xn) | ERn |")
    print("|-|-|-|-|-|-|")


    while True:
        xn = (an + bn)/2
        
        print(f"| {i:10d} | {an:.9e} | {xn:.9e} | {bn:.9e} | {function(xn):.9e} |", end=" ")
        if i > 0:
            relative_error = abs(xn-prev)/abs(xn)
            print(f"\t{relative_error:.9e} |")

        else:
            print(" |")


        if i > 0 and relative_error < 1e-6:
            print(f"\nResultado achado: {xn}")
            break

        if function(xn) > 0 and function(an) > 0 or function(xn) < 0 and function(an) < 0:
            an = xn

        else:
            bn = xn

        prev = xn
        i += 1

if __name__ == "__main__":
    main()
