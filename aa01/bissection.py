# Implementação do método da bisseção para encontrar zeros de funções


import math

def function(x: float) -> float:
    return x**5 + 28.3001*x**4 + 308.576*x**3 + 1614.77*x**2 + 4044.8*x + 3880.73


a, b = map(float, input("Digite os limites do intervalo (a b): ").split())

an, bn = a, b
i = 0

print("         n        an             xn             bn           f(xn)          ERn")

while True:
    xn = (an + bn)/2
    
    print(f"{i:10d}  {an:.9e}  {xn:.9e}  {bn:.9e}  {function(xn):.9e}", end=" ")
    if i > 0:
        relative_error = abs(xn-prev)/abs(xn)
        print(f"\t{relative_error:.9e}")

    else:
        print()


    if i > 0 and relative_error < 1e-6:
        print("Resultado achado")
        break

    if function(xn) > 0 and function(an) > 0 or function(xn) < 0 and function(an) < 0:
        an = xn

    else:
        bn = xn

    prev = xn
    i += 1
