import values as v

def trapezoid_method() -> float:
    lower_limit = v.a
    upper_limit = v.a + v.r()

    i = 0
    error = 1.0
    last = None

    while True:
        left_term = (upper_limit-lower_limit)/(2*(2**i))
        intervals = [v.h(lower_limit)] + [2*v.h(lower_limit+k*((upper_limit-lower_limit)/2**i)) for k in range(1, 2**i)] + [v.h(upper_limit)]
        right_term = sum(intervals)
        integral = left_term * right_term

        if last != None:
            error = abs((last - integral) / integral)

        print(f"{i:.10g} & {integral:.10g} & {error:.10g} \\\\")

        if error < 1e-6:
            break


        i += 1
        last = integral

    return integral