n = 4

mat = []
mat.append([-17, 19, -3, 8, 86])
mat.append([13, -10, -18, -20,-297])
mat.append([-1, 15, -11, 9, 64])
mat.append([-18, 2, 18, -7, 6])


for i in range(n-1):
    for j in range(i+1, n):
        mult = mat[j][i] / mat[i][i]

        mat[j][i] = 0
        for k in range(i+1, n+1):
            mat[j][k] = mat[j][k] - mult * mat[i][k]

for line in mat:
    print(line)
