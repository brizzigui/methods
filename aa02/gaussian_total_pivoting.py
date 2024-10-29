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

    return solutions

def main() -> None:    
    mat, n = read_input()
    x_vector = [index for index in range(n)]

    print()

    for i in range(n-1):
        max = 0
        max_index = None
        for l in range(i, n):
            for c in range(i, n):
                if abs(mat[l][c]) > max:
                    max = abs(mat[l][c])
                    max_index = (l, c)

        l, c = max_index
        mat[l], mat[i] = mat[i], mat[l]
        for k in range(n):
            mat[k][c], mat[k][i] = mat[k][i], mat[k][c]

        x_vector[c], x_vector[i] = x_vector[i], x_vector[c]
                
        for j in range(i+1, n):
            mult = mat[j][i] / mat[i][i]

            mat[j][i] = 0
            for k in range(i+1, n+1):
                mat[j][k] = mat[j][k] - mult * mat[i][k]

        for line in mat:
            print(line)

        print()

    solutions = backsubstitute(mat, n)
    ordered = []
    for iter, index in enumerate(x_vector):
        ordered.append((index+1, solutions[-iter-1]))

    ordered.sort()

    for v in ordered:
        print(f"x{v[0]} = {v[1]}; ")


if __name__ == "__main__":
    main()