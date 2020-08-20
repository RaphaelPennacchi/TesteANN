def jacobi(matrix, x0, TOL=1e-9, MAXIT=10):
    result = []
    diag = []

    b, matrix = [row[-1] for row in matrix], [row[:-1] for row in matrix] 

    for i, row in enumerate(matrix):
        diag.append(row[i])
        row[i] = 0

    for i in range(MAXIT):
        result.append(x0)
        dot_x0 = [sum([row[j] * x0[j] for j, el in enumerate(row)]) for i, row in enumerate(matrix)]
        sub_b = [b[i] - el for i, el in enumerate(dot_x0)]
        x0 = [sub_b[i] / el for i, el in enumerate(diag)]
    print(result)
    return result

def gauss_seidel(matrix, x0, TOL=1e-9, MAXIT=10):
    b, matrix = [row[-1] for row in matrix], [row[:-1] for row in matrix] 
    for x in range(MAXIT):
        for j, row in enumerate(matrix):
            d = b[j]
            for i in range(len(matrix)):
                if j != i:
                    d -= row[i] * x0[i]
            x0[j] = d / row[j]
        print(x0)
    return x0

def gauss(matrix, x0, TOL=1e-9, MAXIT=10):
    for j, row in enumerate(matrix):
        if row[j] == 0:
            for h in range(j + 1, len(matrix)):
                if matrix[h][j] != 0:
                    row[j], matrix[h][j] = matrix[h][j], row[j]
        for i in range(j + 1, len(matrix)):
            value = -(matrix[i][j] / row[j])
            print(value)
            for h in range(j, len(matrix) - 1):
                matrix[i][h] = value * row[h] + matrix[i][h]
        print(matrix)
    return matrix
