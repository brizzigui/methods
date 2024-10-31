import sys

def read_input() -> list:
    # input in tilles example format from aa02 test
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    n = int(input())
    
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
    while any(e > 1e-5 for e in error[k]):
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

    print("\\begin{table}[h!]")
    print("\\centering")
    string = "{" + "|c" * (n+1) + "|}"
    print("\\begin{tabular}" + string)
    print("\\hline")
    string = "k " 
    for idx in range(n):
        string += ("& x_{" + str(idx+1) + ",k} ")
    string += "\\\\"
    print(string)
    print("\\hline")


    for k, v in x.items():
        print(k, end=" & ")
        for idx, single_v in enumerate(v):
            if idx < len(v)-1:
                print(f"{single_v:.10g}", end=" & ")
            else:
                print(f"{single_v:.10g}", end=" \\\\\n")

    print()

    print("\\hline")
    print("\\end{tabular}")
    print("\\label{tab:data_table}")
    print("\\end{table}")

    print()


    print("\\begin{table}[h!]")
    print("\\centering")
    print("\\small")
    string = "{" + "|c" * (n+1) + "|}"
    print("\\begin{tabular}" + string)
    print("\\hline")
    string = "k " 
    for idx in range(n):
        string += ("& ER_{" + str(idx+1) + ",k} ")
    string += "\\\\"
    print(string)
    print("\\hline")
    
    
    for k, v in error.items():
        print(k, end=" & ")
        for idx, single_v in enumerate(v):
            if single_v == float("inf"):
                if idx < len(v)-1:
                    print(f"-", end=" & ")
                else:
                    print(f"-", end=" \\\\\n")

                continue
            
            if idx < len(v)-1:
                print(f"{single_v:.10g}", end=" & ")
            else:
                print(f"{single_v:.10g}", end=" \\\\\n")

    print("\\hline")
    print("\\end{tabular}")
    print("\\label{tab:data_table}")
    print("\\end{table}")


if __name__ == "__main__":
    main()