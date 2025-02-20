import unittest
from run import multiply_matrices, scalar_multiply, dot_product

# FILE: 002_math/test_tests.py


class TestMultiplyMatrices(unittest.TestCase):

    def test_multiply_2x2_matrices(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        result = multiply_matrices(matrix1, matrix2)
        expected = [[19, 22], [43, 50]]
        self.assertEqual(result, expected)

    def test_multiply_3x3_matrices(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        result = multiply_matrices(matrix1, matrix2)
        expected = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(result, expected)

    def test_multiply_by_identity_matrix(self):
        matrix = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        result = multiply_matrices(matrix, identity)
        self.assertEqual(result, matrix)

    def test_incompatible_dimensions(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10]]
        with self.assertRaises(ValueError):
            multiply_matrices(matrix1, matrix2)

class TestScalarMultiply(unittest.TestCase):

    def test_scalar_multiply_with_positive_scalar(self):
        result = scalar_multiply(2, [1, 2, 3])
        self.assertEqual(result, [2, 4, 6])

    def test_scalar_multiply_with_negative_scalar(self):
        result = scalar_multiply(-1, [1, -2, 3])
        self.assertEqual(result, [-1, 2, -3])

    def test_scalar_multiply_with_zero_scalar(self):
        result = scalar_multiply(0, [1, 2, 3])
        self.assertEqual(result, [0, 0, 0])

    def test_scalar_multiply_with_empty_array(self):
        result = scalar_multiply(5, [])
        self.assertEqual(result, [])

    def test_scalar_multiply_with_large_numbers(self):
        result = scalar_multiply(1000, [1000, 2000, 3000])
        self.assertEqual(result, [1000000, 2000000, 3000000])

class TestDotProduct(unittest.TestCase):

    def test_dot_product_with_positive_numbers(self):
        result = dot_product([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, 32)

    def test_dot_product_with_negative_numbers(self):
        result = dot_product([-1, -2, -3], [-4, -5, -6])
        self.assertEqual(result, 32)

    def test_dot_product_with_mixed_numbers(self):
        result = dot_product([1, -2, 3], [-4, 5, -6])
        self.assertEqual(result, -12)

    def test_dot_product_with_zeros(self):
        result = dot_product([0, 0, 0], [0, 0, 0])
        self.assertEqual(result, 0)

    def test_dot_product_with_different_lengths(self):
        with self.assertRaises(ValueError):
            dot_product([1, 2], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()