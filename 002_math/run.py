import examples 

def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two 2D matrices and returns the resulting matrix.

    Args:
        matrix1 (list of list of int/float): The first matrix to be multiplied.
        matrix2 (list of list of int/float): The second matrix to be multiplied.

    Returns:
        list of list of int/float: The resulting matrix after multiplication.

    Raises:
        ValueError: If the number of columns in the first matrix is not equal to the number of rows in the second matrix.
    """

    return examples.multiply_matrices(matrix1, matrix2) 

def scalar_multiply(scalar, array):
    """
    Multiplies a scalar by an array of numbers element-wise.

    Args:
        scalar (int/float): The scalar value to multiply.
        array (list of int/float): The array of numbers to be multiplied.

    Returns:
        list of int/float: The resulting array after element-wise multiplication.
    """
    return examples.scalar_multiply(scalar, array)  

def dot_product(array1, array2): 
    """
    Computes the dot product of two arrays.

    Args:
        array1 (list of int/float): The first array.
        array2 (list of int/float): The second array.

    Returns:
        int/float: The dot product of the two arrays.

    Raises:
        ValueError: If the lengths of the two arrays are not equal.
    """
    return examples.dot_product(array1, array2)