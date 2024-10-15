# Implementação do método da secante para encontrar zeros de funções

def f(x: float) -> float:
    # Retorna o valor de f(x)
    return x**5 - 67.1743*x**4 + 1794.09*x**3 - 23805.8*x**2 + 156873*x - 410517


print("| n | xn | f(xn) | ERn |")
print("| - | -- | ----- | --- |")


i = 0
x_curr = 14
print(f"| {i:2d} | {x_curr:.10g} | {f(x_curr):.10g} | |")


i = 1
x_prev = x_curr
x_curr = 13
error = abs(x_curr - x_prev)/abs(x_curr)
print(f"| {i:2d} | {x_curr:.10g} | {f(x_curr):.10g} | {error:.10g} |")

i = 2

while True:
    angular_coefficient = (f(x_curr) - f(x_prev)) / (x_curr - x_prev)

    x_prev = x_curr
    x_curr = x_curr - f(x_curr)/angular_coefficient

    error = abs(x_curr - x_prev)/abs(x_curr)
    print(f"| {i:2d} | {x_curr:.10g} | {f(x_curr):.10g} | {error:.10g} |")


    if i > 0 and error < 1e-6:
        print(f"## Resultado achado: {x_curr}")
        break

    i += 1