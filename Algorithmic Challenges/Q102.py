def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def is_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    transposed = transpose_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != transposed[i][j]:
                return False  
    return True 
n = int(input("Enter the size of the square matrix (n x n): "))
matrix = []

print("Enter the elements of the matrix:")
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1}: ").split()))
    matrix.append(row)
if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
