import math

# my values
m_c1 = 0.77
m_c2 = 0.019
m_c3 = 0.74
m_c4 = 0.39

m_a = 2.79
m_b = 4.06


# tilles values
t_c1 = 1.3
t_c2 = 0.89
t_c3 = 0.73
t_c4 = 0.31

t_a = -0.657
t_b = 3.15


# used values
c1 = t_c1
c2 = t_c2
c3 = t_c3
c4 = t_c4

a = t_a
b = t_b
string = "tilles"

def r() -> float:
    return (b - a) / 4

def g(x: float) -> float:
    return 2*math.cos(2*math.pi*x*(c3-c4*x))

def f(x: float) -> float:
    return math.sin(2 * math.pi * (x * (c1 - c2*x) + g(x)))

def h(x: float) -> float:
    return math.exp(-x) * f(x)