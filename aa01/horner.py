# Implementação do método de Horner para encontrar zeros de funções

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**5 + 28.3001*x**4 + 308.576*x**3 + 1614.77*x**2 + 4044.8*x + 3880.73


def f_line(x: float) -> float:
    # Retorna o valor de f'(x)
    return 4044.8 + 3229.54*x + 925.728*x**2 + 113.2*x**3 + 5*x**4

x = -2

b_list = []
c_list = []


a = [3880.73, 4044.8, 1614.77, 308.576, 28.3001, 1]
b = [0] * len(a)
c = [0] * len(a)

print("Estimativas")

idx = 0
while True:
    print(f"{idx:10d}  {x:.9e}  {f(x):.9e}  {f_line(x):.9e}", end=" ")
    if idx > 0:
        relative_error = abs(x-prev)/abs(x)
        print(f"\t{relative_error:.9e}")

    else:
        print()

        
    if idx > 0 and relative_error < 1e-6:
        print("Resultado achado")
        break

    # x = x - (f(x) / f_line(x))

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

print("Coeficientes bi do Polinômio f(x)")
for item in b_list:
    print(item)

print("Coeficientes ci do Polinômio f(x)")
for item in c_list:
    print(item)
