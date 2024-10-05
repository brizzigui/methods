def f(x: float) -> float:
    return x**5 - 67.1743*x**4 + 1794.09*x**3 - 23805.8*x**2 + 156873*x - 410517

an = 15
bn = 16

i = 0

print("| n | an | xn | bn | f(xn) | ERn |")
print("| - | -- | -- | -- | ----- | --- |")

while True:
    xn = an - ((bn-an)/(f(bn)-f(an)))*f(an)

    print(f"| {i:10d} | {an:.9e} | {xn:.9e} | {bn:.9e} | {f(xn):.9e} |", end=" ")

    if i > 0:
        error = abs(xn - prev)/xn
        print(f"{error:.9e} |")
        if error < 1e-6:
            print(f"## Resultado achado: {xn}")
            break

    else:
        print(" |")

    
    if f(xn) >= 0 and f(an) >= 0:
        an = xn

    else:
        bn = xn

    prev = xn
    i += 1
