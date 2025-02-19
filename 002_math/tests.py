import unittest
from run import multiply_matrices

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

if __name__ == '__main__':
    unittest.main()