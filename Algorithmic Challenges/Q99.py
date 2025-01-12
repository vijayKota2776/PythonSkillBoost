def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
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
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Matrix 1:")
matrix1 = get_matrix_input(rows, cols)

print("Matrix 2:")
matrix2 = get_matrix_input(rows, cols)
result_matrix = matrix_addition(matrix1, matrix2)
print("\nResulting Matrix after Addition:")
for row in result_matrix:
    print(row)
