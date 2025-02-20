def multiply_matrices(matrix1, matrix2):
    # Get the number of rows and columns for both matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if matrices can be multiplied
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Incompatible dimensions for matrix multiplication")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def scalar_multiply(scalar, array):
    return [scalar * element for element in array]

def dot_product(array1, array2):
    return sum(a * b for a, b in zip(array1, array2))   