import math

def function(x: float) -> float:
    return x**3 - 2*x**2 -4*x + 4


a, b = map(float, input("Digite os limites do intervalo (a b): ").split())

an, bn = a, b
i = 0

print("         n       an          xn          bn         f(xn)       ERn")

while True:
    i += 1
    xn = (an + bn)/2
    
    print(f"{i:10d}  {an:10f}  {xn:10f}  {bn:10f}  {function(xn):10f}", end=" ")
    if i > 1:
        print(f"{abs(xn-prev):10f}")

    else:
        print()


    if math.isclose(function(xn), 0.0, abs_tol=0.0001):
        print("Resultado achado")
        break

    if math.isclose(an, bn, abs_tol=0.0001):
        print("Resultado não achado")
        break

    if function(xn) > 0 and function(an) > 0 or function(xn) < 0 and function(an) < 0:
        an = xn

    else:
        bn = xn

    prev = xn