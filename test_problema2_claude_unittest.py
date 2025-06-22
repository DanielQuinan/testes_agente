import unittest
from unittest.mock import patch
from problema2_claude import Fraction, ComparaSequenze

def calcola_meta_minore(sequenzaA):
    return sum(sequenzaA) / 2 if sequenzaA else 0.0

class TestComparaSequenze(unittest.TestCase):
    def testAcquisisciSequenzaRealiNotNull(self):
        with patch('builtins.input', side_effect=["0"]):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado, [])

    def testAcquisisciSequenzaRealiContents(self):
        entradas = ["1.0", "2.0", "3.0", "4.0", "0"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            expected = [1.0, 2.0, 3.0, 4.0]
            self.assertEqual(resultado, expected)

    def testAcquisisciSequenzaFrazioniNotNull(self):
        entradas = ["-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_B()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado, [])

    def testAcquisisciSequenzaFrazioniContents(self):
        entradas = ["1/10", "100/2", "100/100", "5/4", "-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_B()
            expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
            self.assertEqual(len(resultado), len(expected))
            for r, e in zip(resultado, expected):
                self.assertEqual(r.getNumerator(), e.getNumerator())
                self.assertEqual(r.getDenominator(), e.getDenominator())

    def testCalcolaMetaMinore(self):
        sequenzaA = [2.0, 4.0, 6.0]
        expected = 6.0
        result = calcola_meta_minore(sequenzaA)
        self.assertAlmostEqual(result, expected, places=3)

    def testCalcolaMetaMinoreEmptyList(self):
        sequenzaA = []
        expected = 0.0
        result = calcola_meta_minore(sequenzaA)
        self.assertAlmostEqual(result, expected, places=3)

    def testFrazione3Constructor(self):
        frazione = Fraction(2, 3)
        self.assertIsNotNone(frazione)
        self.assertEqual(frazione.getNumerator(), 2)
        self.assertEqual(frazione.getDenominator(), 3)

    def testFrazione3IsMaggiore(self):
        frazione1 = Fraction(1, 2)
        frazione2 = Fraction(1, 3)
        self.assertTrue(frazione1.isGreater(frazione2))

if __name__ == "__main__":
    unittest.main()
