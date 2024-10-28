# Tradução da implementação em aula do professor, conforme exemplo dos slides

def main() -> None:
    number_pairs = 5
    x = [0.3, 0.6, 0.9, 1.2, 1.5]
    y = [0.671133, 0.00250768, -0.391769, -0.240425, 0.150645]

    matrix = []
    for _ in range(number_pairs):
        matrix.append([0]*(number_pairs+1))

    for i in range(number_pairs):
        matrix[i][0] = x[i]
        matrix[i][1] = y[i]
    
    # Diferença dividida

    for ord in range(2, number_pairs+1):
        for i in range(number_pairs-ord+1):
            matrix[i][ord] = (matrix[i][ord-1]-matrix[i+1][ord-1])/(matrix[i+ord-1][0]-matrix[i][0])
        
    for l in matrix:
        print(l)


if __name__ == "__main__":
    main()