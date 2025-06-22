import unittest
from problema1_claude import diff

class TestProblema1Claude(unittest.TestCase):
    def test_exemplo(self):
        self.assertTrue(True)  # Substitua por testes reais

class TestDiff(unittest.TestCase):
    def test_diff_normal_case(self):
        a = [1, 3, 5, 7, 9]
        b = [1, 5, 7]
        expected = [3, 9]
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_empty_array(self):
        a = []
        b = [1, 2, 3]
        expected = []
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_both_empty_arrays(self):
        a = []
        b = []
        expected = []
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_all_common_elements(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        expected = []
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_no_common_elements(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        expected = [1, 2, 3]
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_duplicates(self):
        a = [1, 1, 2, 2]
        b = [2, 3, 4]
        expected = [1, 1]
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_negative_numbers(self):
        a = [-1, -2, -3]
        b = [-2, -3, -4]
        expected = [-1]
        result = diff(a, b)
        self.assertEqual(result, expected)

    def test_diff_null_array(self):
        with self.assertRaises(TypeError):
            diff(None, [1, 5, 7])

    def test_diff_both_null_arrays(self):
        with self.assertRaises(TypeError):
            diff(None, None)

if __name__ == "__main__":
    unittest.main()
