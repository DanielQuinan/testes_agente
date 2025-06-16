import unittest
from unittest.mock import patch

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def isLesser(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def isGreater(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def to_float(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

class ComparaSequenze:
    def ler_sequencia_A(self):
        A = []
        while True:
            try:
                valor = float(input())
                if valor == 0:
                    break
                A.append(valor)
            except ValueError:
                print("Entrada inválida para número real.")
        return A

    def ler_sequencia_B(self):
        B = []
        while True:
            try:
                entrada = input()
                nums = entrada.strip().split('/')
                if len(nums) != 2:
                    print("Entre com a fração no formato numerador/denominador.")
                    continue
                numerador = int(nums[0])
                denominador = int(nums[1])
                if denominador == 0:
                    print("Denominador não pode ser zero.")
                    continue
                frac = Fraction(numerador, denominador)
                if frac.to_float() < 0:
                    break
                B.append(frac)
            except ValueError:
                print("Entrada inválida para fração.")
        return B

    def processar(self):
        print("Digite a sequência A (números reais, termine com 0):")
        A = self.ler_sequencia_A()
        print("Digite a sequência B (frações no formato n/d, termine com fração < 0):")
        B = self.ler_sequencia_B()

        if not A or not B:
            print("Erro: ao menos uma das sequências está vazia.")
            return

        metade = len(A) / 2
        for frac in B:
            count = sum(frac.to_float() > a for a in A)
            if count >= metade:
                print(frac)

def calcola_meta_minore(sequenzaA):
    return sum(sequenzaA) / 2

class TestComparaSequenze(unittest.TestCase):
    def test_AcquisisciSequenzaRealiNotNull(self):
        with patch('builtins.input', side_effect=["0"]):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            self.assertIsNotNone(resultado)

    def test_AcquisisciSequenzaRealiContents(self):
        entradas = ["1.0", "2.0", "3.0", "4.0", "0"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            expected = [1.0, 2.0, 3.0, 4.0]
            self.assertEqual(resultado, expected)

    def test_AcquisisciSequenzaFrazioniNotNull(self):
        entradas = ["-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_B()
            self.assertIsNotNone(resultado)

    def test_AcquisisciSequenzaFrazioniContents(self):
        entradas = ["1/10", "100/2", "100/100", "5/4", "-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_B()
            expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
            self.assertEqual(len(resultado), len(expected))
            for r, e in zip(resultado, expected):
                self.assertEqual(r.getNumerator(), e.getNumerator())
                self.assertEqual(r.getDenominator(), e.getDenominator())

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
        self.assertEqual(frazione.getNumerator(), 2)
        self.assertEqual(frazione.getDenominator(), 3)

    def test_Frazione3IsMaggiore(self):
        frazione1 = Fraction(1, 2)
        frazione2 = Fraction(1, 3)
        self.assertTrue(frazione1.isGreater(frazione2))

if __name__ == "__main__":
    unittest.main()


