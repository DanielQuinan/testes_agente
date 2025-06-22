import unittest
from unittest.mock import patch
from fractions import Fraction
from problema2_gemini import ComparaSequenze, calcola_meta_minore

class TestComparaSequenze(unittest.TestCase):
    def test_AcquisisciSequenzaRealiNotNull(self):
        with patch('builtins.input', side_effect=["0"]):
            cs = ComparaSequenze()
            cs.ler_sequencia_A()
            self.assertIsNotNone(cs.sequencia_A)
            self.assertEqual(cs.sequencia_A, [])

    def test_AcquisisciSequenzaRealiContents(self):
        entradas = ["1.0", "2.0", "3.0", "4.0", "0"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            cs.ler_sequencia_A()
            expected = [1.0, 2.0, 3.0, 4.0]
            self.assertEqual(cs.sequencia_A, expected)

    def test_AcquisisciSequenzaFrazioniNotNull(self):
        entradas = ["-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            cs.ler_sequencia_B()
            self.assertIsNotNone(cs.sequencia_B)
            self.assertEqual(cs.sequencia_B, [])

    def test_AcquisisciSequenzaFrazioniContents(self):
        entradas = ["1/10", "100/2", "100/100", "5/4", "-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            cs.ler_sequencia_B()
            expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
            self.assertEqual(len(cs.sequencia_B), len(expected))
            for r, e in zip(cs.sequencia_B, expected):
                self.assertEqual(r.numerator, e.numerator)
                self.assertEqual(r.denominator, e.denominator)

    def test_CalcolaMetaMinore(self):
        sequenzaA = [2.0, 4.0, 6.0]
        expected = 6.0
        result = calcola_meta_minore(sequenzaA)
        self.assertAlmostEqual(result, expected, places=3)

    def test_CalcolaMetaMinoreEmptyList(self):
        sequenzaA = []
        expected = 0.0
        result = calcola_meta_minore(sequenzaA)
        self.assertAlmostEqual(result, expected, places=3)

    def test_Frazione3Constructor(self):
        frazione = Fraction(2, 3)
        self.assertIsNotNone(frazione)
        self.assertEqual(frazione.numerator, 2)
        self.assertEqual(frazione.denominator, 3)

    def test_Frazione3IsMaggiore(self):
        frazione1 = Fraction(1, 2)
        frazione2 = Fraction(1, 3)
        self.assertTrue(frazione1 > frazione2)

if __name__ == "__main__":
    unittest.main()
