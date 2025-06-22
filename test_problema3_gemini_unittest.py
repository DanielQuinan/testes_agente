import unittest
from problema3_gemini import MatriceStringa, MatriceException

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
