def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        print("Matrix multiplication is not possible. The number of columns in matrix1 must equal the number of rows in matrix2.")
        return None
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element at position ({i+1},{j+1}): ")))
        matrix.append(row)
    return matrix
rows1 = int(input("Enter number of rows for matrix 1: "))
cols1 = int(input("Enter number of columns for matrix 1: "))
rows2 = int(input("Enter number of rows for matrix 2: "))
cols2 = int(input("Enter number of columns for matrix 2: "))
if cols1 != rows2:
    print("Matrix multiplication is not possible due to incompatible dimensions.")
else:
    print("Matrix 1:")
    matrix1 = get_matrix_input(rows1, cols1)

    print("Matrix 2:")
    matrix2 = get_matrix_input(rows2, cols2)
    result_matrix = matrix_multiplication(matrix1, matrix2)
    if result_matrix:
        print("\nResulting Matrix after Multiplication:")
        for row in result_matrix:
            print(row)
