class MatriceException(Exception):
    """Custom exception for matrix operations"""
    def __init__(self):
        super().__init__()


class MatriceStringa:
    def __init__(self, r, c, val):
        """
        Initialize the matrix with r rows and c columns, filling each position with val.
        
        Args:
            r (int): number of rows
            c (int): number of columns  
            val (str): value to fill each position
            
        Raises:
            RuntimeError: if r or c are not valid (less than or equal to 0)
        """
        if r <= 0 or c <= 0:
            raise RuntimeError()
        
        self.m = [[val for _ in range(c)] for _ in range(r)]
        self.rows = r
        self.cols = c
    
    def set(self, r, c, val):
        """
        Set the value at position (r, c) in the matrix.
        
        Args:
            r (int): row index
            c (int): column index
            val (str): value to set
            
        Raises:
            MatriceException: if r or c are outside valid bounds
        """
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            raise MatriceException()
        
        self.m[r][c] = val
    
    def rigaToString(self, idx, separatore):
        """
        Convert a row to string with the given separator.
        
        Args:
            idx (int): row index
            separatore (str): separator to use between elements
            
        Returns:
            str: string representation of the row
            
        Raises:
            MatriceException: if idx is outside valid bounds
        """
        if idx < 0 or idx >= self.rows:
            raise MatriceException()
        
        return separatore.join(self.m[idx])


# Example usage and testing
""" if __name__ == "__main__":
    try:
        # Test valid constructor
        matrix = MatriceStringa(3, 4, "default")
        print("Matrix created successfully")
        
        # Test set method
        matrix.set(0, 0, "hello")
        matrix.set(1, 2, "world")
        print("Values set successfully")
        
        # Test rigaToString method
        row_string = matrix.rigaToString(0, " | ")
        print(f"Row 0: {row_string}")
        
        row_string = matrix.rigaToString(1, ", ")
        print(f"Row 1: {row_string}")
        
        # Test exceptions
        try:
            invalid_matrix = MatriceStringa(-1, 5, "test")
        except RuntimeError:
            print("RuntimeError caught for invalid constructor parameters")
        
        try:
            matrix.set(10, 0, "invalid")
        except MatriceException:
            print("MatriceException caught for invalid set parameters")
        
        try:
            matrix.rigaToString(10, ",")
        except MatriceException:
            print("MatriceException caught for invalid rigaToString parameters")
            
    except Exception as e:
        print(f"Unexpected error: {e}") """

import unittest

class TestMatriceStringa(unittest.TestCase):
    def test_valid_matrix_creation(self):
        matrice = MatriceStringa(3, 3, "test")
        self.assertIsNotNone(matrice)

    def test_matrix_creation_with_zero_rows(self):
        with self.assertRaises(RuntimeError):
            MatriceStringa(0, 3, "test")

    def test_matrix_creation_with_zero_columns(self):
        with self.assertRaises(RuntimeError):
            MatriceStringa(3, 0, "test")

    def test_matrix_creation_with_negative_rows(self):
        with self.assertRaises(RuntimeError):
            MatriceStringa(-1, 3, "test")

    def test_matrix_creation_with_negative_columns(self):
        with self.assertRaises(RuntimeError):
            MatriceStringa(3, -1, "test")

    def test_set_valid_cell(self):
        matrice = MatriceStringa(3, 3, "test")
        matrice.set(1, 1, "newValue")
        self.assertEqual(matrice.m[1][1], "newValue")

    def test_set_cell_with_row_out_of_bounds(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.set(3, 1, "value")

    def test_set_cell_with_column_out_of_bounds(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.set(1, 3, "value")

    def test_set_cell_with_negative_column(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.set(1, -1, "value")

    def test_set_cell_with_negative_row(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.set(-1, 1, "value")

    def test_riga_to_string_valid(self):
        matrice = MatriceStringa(3, 3, "test")
        expected = "test.test.test"
        self.assertEqual(expected, matrice.rigaToString(1, "."))

    def test_riga_to_string_with_high_index(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.rigaToString(3, ".")

    def test_riga_to_string_with_negative_index(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.rigaToString(-1, ".")

    def test_riga_to_string_with_null_separator(self):
        matrice = MatriceStringa(3, 3, "test")
        with self.assertRaises(MatriceException):
            matrice.rigaToString(1, None)

    def test_riga_to_string_with_empty_separator(self):
        matrice = MatriceStringa(3, 3, "test")
        expected = "testtesttest"
        self.assertEqual(expected, matrice.rigaToString(1, ""))

    def test_matrix_creation_with_null_value(self):
        matrice = MatriceStringa(3, 3, None)
        self.assertIsNone(matrice.m[0][0])

    def test_matrix_creation_with_empty_string(self):
        matrice = MatriceStringa(3, 3, "")
        self.assertEqual(",,", matrice.rigaToString(0, ","))

if __name__ == "__main__":
    unittest.main()