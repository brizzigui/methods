# Implementação do método de Newton para encontrar zeros de funções

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**5 - 67.1743*x**4 + 1794.09*x**3 - 23805.8*x**2 + 156873*x - 410517

def f_line(x: float) -> float:
    # Retorna o valor de f'(x)
    return 156873 - 47611.6*x + 5382.27*x**2 - 268.697*x**3 + 5*x**4

x = 12
i = 0

print(" n\txn\t\tf(xn)\t\tf'(xn)\t\tERn")

while True:
    if i > 0:
        error = abs(x - prev)/abs(x)
        print(f"{i:2d}\t{x:.10f}\t{f(x):.10f}\t{f_line(x):.10f}\t{error:.10f}")

    else:
        print(f"{i:2d}\t{x:.10f}\t{f(x):.10f}\t{f_line(x):.10f}")

    if i > 0 and error < 1e-6:
        print("Resultado achado")
        break

    prev = x
    x = x - f(x) / f_line(x)
    i += 1
