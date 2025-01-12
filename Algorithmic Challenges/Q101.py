def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element at position ({i+1},{j+1}): ")))
        matrix.append(row)
    return matrix
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))
matrix = get_matrix_input(rows, cols)
transposed_matrix = transpose_matrix(matrix)
print("\nOriginal Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
