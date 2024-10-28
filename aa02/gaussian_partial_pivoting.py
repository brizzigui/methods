def read_input() -> list:
    # input in tilles example format from aa02 test
    n = int(input("Número de linhas: "))
    
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
        print(value)
        for k in range(len(solutions)):
            value -= solutions[k] * mat[n-i-1][-k-2]
            print(solutions[k], mat[n-i-1][-k-2])

        solutions.append(value/mat[n-i-1][n-i-1])

    print(solutions)


def main() -> None:    
    mat, n = read_input()


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

    for line in mat:
        print(line)

    print()

    backsubstitute(mat, n)


if __name__ == "__main__":
    main()