import matplotlib.pyplot as plt
import numpy as np

def divided_differences() -> tuple[list, list, list]:
    number_pairs = 10

    print("x & y & ", end="")
    for i in range(1, number_pairs-1):
        print(f"DD{i} & ", end="")
    print(f"DD{number_pairs-1} \\\\")
    

    x, y = [], []

    for i in range(number_pairs):
        x_cur, y_cur = map(float, input().split())
        x.append(x_cur)
        y.append(y_cur)

    matrix = []
    for _ in range(number_pairs):
        matrix.append([0]*(number_pairs+1))

    for i in range(number_pairs):
        matrix[i][0] = x[i]
        matrix[i][1] = y[i]
    
    # Diferença dividida

    for ord in range(2, number_pairs+1):
        for i in range(number_pairs-ord+1):
            matrix[i][ord] = (matrix[i+1][ord-1]-matrix[i][ord-1])/(matrix[i+ord-1][0]-matrix[i][0])
        
    for l in matrix:
        for v in range(len(l)):
            if v < len(l) - 1:
                if l[v] == 0:
                    print(f"- & ", end="") 
                
                else:
                    print(f"{l[v]:.6g} & ", end="")

            else:
                if l[v] == 0:
                    print(f"- \\\\ ", end="") 

                else:
                    print(f"{l[v]:.6g} \\\\ ", end="")

        print()

    return matrix, x, y


def apply_polynomial(matrix: list, z: float, size: int) -> None:
    result = 0
    for col in range(1, size):
        partial = matrix[0][col]

        for deg in range(col-1):
            partial *= (z-matrix[deg][0])

        result += partial

    return result


def graph(matrix: list, size: int, x_points: list, y_points: list) -> None:
    # Generate x values
    x_values = np.linspace(0, 2, 1000)  # Adjust the range and number of points as needed

    # Compute y values using the function
    y_values = []
    for v in x_values:
        y_values.append(apply_polynomial(matrix, v, size))

    # Plot the function

    plt.plot(x_values, y_values, color="lightgreen")


    ax = plt.gca()
    ax.set_xlim([0, 2])
    ax.set_ylim([-1, 6])

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.scatter(x_points, y_points, color="black", marker="o", zorder=10) 
    plt.show()
        


def main() -> None:
    matrix, x, y = divided_differences()

    print()

    past = None
    for size in range(2, len(matrix[0])+1):
        
        result = apply_polynomial(matrix, 0.821, size)
        print(f"{size-2:.10g} & {result:.10g} & ", end=" ")

        if past is not None:
            print(f"{abs((result-past)/result):.10g} \\\\")

        else:
            print("- \\\\")

        past = result


        if size % 2 == 0:
            # graph(matrix, size, x, y)
            pass
        

    


if __name__ == "__main__":
    main()