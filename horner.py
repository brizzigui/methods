# Implementação do método de Horner para encontrar zeros de funções

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**3 -2*(x**2) -4*x + 4

def f_line(x: float) -> float:
    # Retorna o valor de f'(x)
    return 3*(x**2) -(4*x) -4

x = 0.5


a = [4, -4, -2, 1]
b = [0] * len(a)
c = [0] * len(a)


for idx in range(10):
    x = x - f(x) / f_line(x)

    b[-1] = a[-1]

    for i in range(1, len(a)):
        k = len(a)-i-1
        b[k] = a[k] + b[k+1] * x
    
    c[k] = a[-1]
    for i in range(1, len(a)-1):
        k = len(a)-i-1
        c[k] = b[k] + c[k+1] * x

    x = x - b[0]/c[1]

    print(idx, a, b, c, x)
