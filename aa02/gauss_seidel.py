def read_input() -> list:
    # input in tilles example format from aa02 test
    n = int(input("Número de linhas: "))
    
    a = []
    for _ in range(n):
        a.append([*map(float, input().replace("−", "-").split())]) 
        # replace method makes it have the right "-"

    b = []
    for _ in range(n):
        b.append(float(input().replace("−", "-"))) 
        # replace method makes it have the right "-"


    return a, b, n 

def main():
    
    a, b, n = read_input()
    x = {0: [0]*n}

    error = {0: [float("inf")]*n} 

    k = 0
    while any(e > 1e-6 for e in error[k]):
        for i in range(n):
            acc = 0
            for j in range(i):
                if j != i:
                    acc += a[i][j] * x[k+1][j]

            for j in range(i, n):
                if j != i:
                    acc += a[i][j] * x[k][j]

            if k+1 not in x:
                x[k+1] = [0]*n

            x[k+1][i] = (b[i]-acc)/a[i][i]

            if k+1 not in error:
                error[k+1] = [float("inf")]*n     

            if (k+1) == 1:
                error[k+1][i] = 1
            
            else:
                error[k+1][i] = abs((x[k+1][i]-x[k][i])/x[k+1][i])


        k += 1

    for k, v in x.items():
        print(v)
        
    for k, v in error.items():
        print(v)


if __name__ == "__main__":
    main()