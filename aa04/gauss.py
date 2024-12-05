import values as v
import math
import numpy as np

def gauss_quadrature(a, b, n) -> float:
    # Get Gauss-Legendre nodes and weights
    nodes, weights = np.polynomial.legendre.leggauss(n)
    # Map nodes to [a, b]
    mapped_nodes = 0.5 * (nodes + 1) * (b - a) + a
    # Compute the integral
    integral = sum(weights[i] * v.h(mapped_nodes[i]) for i in range(n))
    return 0.5 * (b - a) * integral



def gauss_method(n_points: int, lower_limit: float, upper_limit: float) -> float:
    i = 0
    error = 1.0
    last = None

    while True:
        integral = 0       
        for intervals in range(2**i):
            lower_bound = lower_limit + (intervals)*((upper_limit - lower_limit)/2**i)
            upper_bound = lower_limit + (intervals+1)*((upper_limit - lower_limit)/2**i)

            integral += gauss_quadrature(a=lower_bound, b=upper_bound, n=n_points)

        if last != None:
            error = abs((last - integral) / integral)

        print(f"{i:.10g} & {integral:.10g} & {error:.10g} \\\\")

        if error < 1e-6:
            break

        i += 1
        last = integral

    return integral


def gauss_method_2pts() -> float:
    lower_limit = v.a + 2*v.r()
    upper_limit = v.a + 3*v.r()

    return gauss_method(2, lower_limit, upper_limit)

def gauss_method_3pts() -> float:
    lower_limit = v.a + 3*v.r()
    upper_limit = v.a + 4*v.r()

    return gauss_method(3, lower_limit, upper_limit)