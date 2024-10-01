# Implementação do método de Newton para encontrar zeros de funções

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**3 -2*(x**2) -4*x + 4

def f_line(x: float) -> float:
    # Retorna o valor de f'(x)
    return 3*(x**2) -(4*x) -4

x = 100

for i in range(100):
    x = x - f(x) / f_line(x)

    print(x)