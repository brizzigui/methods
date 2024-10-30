import sys

def read_input() -> list:
    # input in tilles example format from aa02 test
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    n = int(input())
    
    mat = []
    for _ in range(n):
        mat.append([*map(float, input().replace("−", "-").split())]) 
        # replace method makes it have the right "-"

    return mat, n 


def backsubstitute(mat, n) -> list:
    # goes from last line to first, substituting back
    # returns list with solutions, ordered by index

    solutions = []

    for i in range(n):
        value = mat[n-i-1][-1] 
        for k in range(len(solutions)):
            value -= solutions[k] * mat[n-i-1][-k-2]

        solutions.append(value/mat[n-i-1][n-i-1])

    return solutions


def main() -> None:    
    mat, n = read_input()

    print('\\[')
    print('A_{0} = \\begin{bmatrix}')
    for line in mat:
        for idx, value in enumerate(line):
            if idx < len(line)-1:
                print(f"{value:.10g}", end=" & ")

            else:
                print(f"{value:.10g}", end="\\\\\n")

    print('\\end{bmatrix}')
    print('\\]')
    print()


    for i in range(n-1):
        max = 0
        max_index = None
        for c in range(i, n):
            if abs(mat[c][i]) > max:
                max = abs(mat[c][i])
                max_index = c

        mat[max_index], mat[i] = mat[i], mat[max_index]
                
        for j in range(i+1, n):
            mult = mat[j][i] / mat[i][i]

            mat[j][i] = 0
            for k in range(i+1, n+1):
                mat[j][k] = mat[j][k] - mult * mat[i][k]

        print('\\[')
        print("A_{" + str(i+1) + "} = ", end="")
        print('\\begin{bmatrix}')
        for line in mat:
            for idx, value in enumerate(line):
                if idx < len(line)-1:
                    print(f"{value:.10g}", end=" & ")

                else:
                    print(f"{value:.10g}", end="\\\\\n")

        print('\\end{bmatrix}')
        print('\\]')
        print()

        

    solutions = backsubstitute(mat, n)
    for idx, v in enumerate(solutions):
        print("x_{" + str(len(solutions)-idx) + f"}} = {v:.10g};\n")


if __name__ == "__main__":
    main()