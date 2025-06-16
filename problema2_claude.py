class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominador não pode ser zero")
        self.numerator = numerator
        self.denominator = denominator

    def isLesser(self, other):
        if isinstance(other, (int, float)):
            return self.numerator / self.denominator < other
        return self.numerator * other.denominator < other.numerator * self.denominator

    def isGreater(self, other):
        if isinstance(other, (int, float)):
            return self.numerator / self.denominator > other
        return self.numerator * other.denominator > other.numerator * self.denominator

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def to_float(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.to_float() < other
        return self.isLesser(other)

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.to_float() > other
        return self.isGreater(other)


class ComparaSequenze:
    def __init__(self):
        self.sequencia_A = []
        self.sequencia_B = []

    def ler_sequencia_A(self):
        """Lê uma sequência de números reais da entrada padrão até encontrar 0"""
        sequencia = []
        while True:
            try:
                numero = float(input())
                if numero == 0:
                    break
                sequencia.append(numero)
            except ValueError:
                print("Erro: entrada inválida. Digite um número real.")
        
        self.sequencia_A = sequencia
        return sequencia

    def ler_sequencia_B(self):
        """Lê uma sequência de frações da entrada padrão até encontrar uma fração < 0"""
        sequencia = []
        while True:
            try:
                entrada = input().strip()
                
                # Verifica se a entrada está no formato numerador/denominador
                if '/' in entrada:
                    partes = entrada.split('/')
                    if len(partes) != 2:
                        print("Erro: formato inválido. Use numerador/denominador.")
                        continue
                    
                    numerador = int(partes[0])
                    denominador = int(partes[1])
                    
                    if denominador == 0:
                        print("Erro: denominador não pode ser zero.")
                        continue
                    
                    fracao = Fraction(numerador, denominador)
                else:
                    # Trata entrada como número inteiro (ex: "5" vira "5/1")
                    numerador = int(entrada)
                    fracao = Fraction(numerador, 1)
                
                # Verifica se a fração é menor que 0 para terminar a leitura
                if fracao < 0:
                    break
                
                sequencia.append(fracao)
                
            except ValueError:
                print("Erro: entrada inválida. Digite uma fração no formato numerador/denominador.")
        
        self.sequencia_B = sequencia
        return sequencia

    def processar(self):
        """Método principal que executa todo o processamento"""
        # Lê as sequências
        self.ler_sequencia_A()
        self.ler_sequencia_B()
        
        # Verifica se alguma das sequências está vazia
        if not self.sequencia_A or not self.sequencia_B:
            print("Erro: ao menos uma das sequências está vazia.")
            return
        
        # Calcula metade do tamanho da sequência A
        metade_tamanho_A = len(self.sequencia_A) / 2
        
        # Encontra frações de B que são maiores que pelo menos metade dos números de A
        fracoes_resultado = []
        
        for fracao in self.sequencia_B:
            contador_maiores = 0
            
            # Conta quantos números de A são menores que a fração atual
            for numero in self.sequencia_A:
                if fracao > numero:
                    contador_maiores += 1
            
            # Se a fração é maior que pelo menos metade dos números de A
            if contador_maiores >= metade_tamanho_A:
                fracoes_resultado.append(fracao)
        
        # Imprime o resultado
        for fracao in fracoes_resultado:
            print(fracao)


# Testes unitários
# def testAcquisisciSequenzaRealiNotNull():
#     import builtins
#     original_input = builtins.input
#     builtins.input = lambda: "0"  # Simula o usuário digitando apenas 0
#     cs = ComparaSequenze()
#     cs.ler_sequencia_A()
#     assert cs.sequencia_A is not None, "Sequenza A should not be null"
#     builtins.input = original_input
#     print("testAcquisisciSequenzaRealiNotNull passou!")

# def testAcquisisciSequenzaRealiContents():
#     import builtins
#     original_input = builtins.input
#     inputs = iter(["1.0", "2.0", "3.0", "4.0", "0"])
#     builtins.input = lambda: next(inputs)
#     cs = ComparaSequenze()
#     cs.ler_sequencia_A()
#     expected = [1.0, 2.0, 3.0, 4.0]
#     assert cs.sequencia_A == expected, f"Esperado {expected}, mas obteve {cs.sequencia_A}"
#     builtins.input = original_input
#     print("testAcquisisciSequenzaRealiContents passou!")

# def testAcquisisciSequenzaFrazioniNotNull():
#     import builtins
#     original_input = builtins.input
#     inputs = iter(["-1/2"])
#     builtins.input = lambda: next(inputs)
#     cs = ComparaSequenze()
#     cs.ler_sequencia_B()
#     assert cs.sequencia_B is not None, "Sequenza B should not be null"
#     builtins.input = original_input
#     print("testAcquisisciSequenzaFrazioniNotNull passou!")

# def testAcquisisciSequenzaFrazioniContents():
#     import builtins
#     original_input = builtins.input
#     inputs = iter(["1/10", "100/2", "100/100", "5/4", "-1/2"])
#     builtins.input = lambda: next(inputs)
#     cs = ComparaSequenze()
#     cs.ler_sequencia_B()
#     expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
#     assert len(cs.sequencia_B) == len(expected), f"Esperado {len(expected)} frações, mas obteve {len(cs.sequencia_B)}"
#     for r, e in zip(cs.sequencia_B, expected):
#         assert r.getNumerator() == e.getNumerator() and r.getDenominator() == e.getDenominator(), \
#             f"Esperado {e.getNumerator()}/{e.getDenominator()}, mas obteve {r.getNumerator()}/{r.getDenominator()}"
#     builtins.input = original_input
#     print("testAcquisisciSequenzaFrazioniContents passou!")

# def calcola_meta_minore(sequenzaA):
#     # Soma todos os elementos e divide por 2
#     return sum(sequenzaA) / 2

# def testCalcolaMetaMinore():
#     sequenzaA = [2.0, 4.0, 6.0]
#     expected = 6.0
#     result = calcola_meta_minore(sequenzaA)
#     assert abs(result - expected) < 0.001, f"Esperado {expected}, mas obteve {result}"
#     print("testCalcolaMetaMinore passou!")

# def testCalcolaMetaMinoreEmptyList():
#     sequenzaA = []
#     expected = 0.0
#     result = calcola_meta_minore(sequenzaA)
#     assert abs(result - expected) < 0.001, f"Esperado {expected}, mas obteve {result}"
#     print("testCalcolaMetaMinoreEmptyList passou!")

# def testFrazione3Constructor():
#     frazione = Fraction(2, 3)
#     assert frazione is not None, "Frazione3 object should not be null"
#     assert frazione.getNumerator() == 2, f"Esperado numerador 2, mas obteve {frazione.getNumerator()}"
#     assert frazione.getDenominator() == 3, f"Esperado denominador 3, mas obteve {frazione.getDenominator()}"
#     print("testFrazione3Constructor passou!")

# def testFrazione3IsMaggiore():
#     frazione1 = Fraction(1, 2)
#     frazione2 = Fraction(1, 3)
#     assert frazione1.isGreater(frazione2), "1/2 should be greater than 1/3"
#     print("testFrazione3IsMaggiore passou!")

import unittest
from unittest.mock import patch

class TestComparaSequenze(unittest.TestCase):
    def testAcquisisciSequenzaRealiNotNull(self):
        # Simula o usuário digitando apenas 0
        with patch('builtins.input', side_effect=["0"]):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado, [])

    def testAcquisisciSequenzaRealiContents(self):
        # Simula o usuário digitando 1.0, 2.0, 3.0, 4.0, 0
        entradas = ["1.0", "2.0", "3.0", "4.0", "0"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_A()
            expected = [1.0, 2.0, 3.0, 4.0]
            self.assertEqual(resultado, expected)

    def testAcquisisciSequenzaFrazioniNotNull(self):
        # Simula o usuário digitando uma fração negativa logo de início
        entradas = ["-1/2"]
        with patch('builtins.input', side_effect=entradas):
            cs = ComparaSequenze()
            resultado = cs.ler_sequencia_B()
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado, [])

    def testAcquisisciSequenzaFrazioniContents(self):
        # Simula o usuário digitando várias frações e depois uma negativa
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
        # Testa metade da soma de uma lista
        sequenzaA = [2.0, 4.0, 6.0]
        expected = 6.0
        result = sum(sequenzaA) / 2
        self.assertAlmostEqual(result, expected, places=3)

    def testCalcolaMetaMinoreEmptyList(self):
        # Testa lista vazia
        sequenzaA = []
        expected = 0.0
        result = sum(sequenzaA) / 2
        self.assertAlmostEqual(result, expected, places=3)

    def testFrazione3Constructor(self):
        # Testa construtor da fração
        frazione = Fraction(2, 3)
        self.assertIsNotNone(frazione)
        self.assertEqual(frazione.getNumerator(), 2)
        self.assertEqual(frazione.getDenominator(), 3)

    def testFrazione3IsMaggiore(self):
        # Testa comparação de frações
        frazione1 = Fraction(1, 2)
        frazione2 = Fraction(1, 3)
        self.assertTrue(frazione1.isGreater(frazione2))


if __name__ == "__main__":
    unittest.main()
    
    # Executa o programa principal
    print("\n--- Executando ComparaSequenze ---")
    print("Digite os números reais para a sequência A (termine com 0):")
    cs = ComparaSequenze()
    print("Digite as frações para a sequência B no formato num/den (termine com fração < 0):")
    cs.processar()