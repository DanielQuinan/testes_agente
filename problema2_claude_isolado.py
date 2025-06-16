import unittest
from unittest.mock import patch

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominador não pode ser zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()
    
    def _simplify(self):
        """Simplifica a fração usando o MDC"""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        common_divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        
        # Garantir que o denominador seja sempre positivo
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def isLesser(self, other):
        """Verifica se esta fração é menor que outra fração ou número"""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:  # other é um número
            return self.numerator < other * self.denominator
    
    def isGreater(self, other):
        """Verifica se esta fração é maior que outra fração ou número"""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        else:  # other é um número
            return self.numerator > other * self.denominator
    
    def __eq__(self, other):
        """Verifica se duas frações são iguais"""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            return self.numerator == other * self.denominator

    def getNumerator(self):
        return self.numerator
    
    def getDenominator(self):
        return self.denominator
    
    def toFloat(self):
        """Converte a fração para float"""
        return self.numerator / self.denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


class ComparaSequenze:
    def __init__(self):
        self.sequencia_a = []
        self.sequencia_b = []
    
    def ler_sequencia_A(self):
        """Lê uma sequência de números reais até encontrar 0 e retorna a lista"""
        sequencia = []
        while True:
            try:
                numero = float(input())
                if numero == 0:
                    break
                sequencia.append(numero)
            except ValueError:
                print("Erro: Digite um número válido.")
        self.sequencia_a = sequencia
        return sequencia
    
    def ler_sequencia_B(self):
        """Lê uma sequência de frações até encontrar uma fração menor que 0 e retorna a lista"""
        sequencia = []
        while True:
            try:
                entrada = input().strip()
                if '/' not in entrada:
                    print("Erro: Digite no formato 'numerador/denominador'")
                    continue
                
                numerador_str, denominador_str = entrada.split('/')
                numerador = int(numerador_str.strip())
                denominador = int(denominador_str.strip())
                
                fracao = Fraction(numerador, denominador)
                
                # Verifica se a fração é menor que 0
                if fracao.isLesser(0):
                    break
                
                sequencia.append(fracao)
                
            except ValueError:
                print("Erro: Digite números inteiros válidos para numerador e denominador.")
            except Exception as e:
                print(f"Erro: {e}")
        
        self.sequencia_b = sequencia
        return sequencia
    
    def ler_sequencia_a(self):
        """Método original que também imprime mensagens"""
        print("Digite os números reais da sequência A (digite 0 para terminar):")
        return self.ler_sequencia_A()
    
    def ler_sequencia_b(self):
        """Método original que também imprime mensagens"""
        print("Digite as frações da sequência B no formato 'numerador/denominador'")
        print("(a inserção termina quando uma fração menor que 0 é inserida):")
        return self.ler_sequencia_B()
    
    def validar_sequencias(self):
        """Valida se ambas as sequências não estão vazias"""
        if len(self.sequencia_a) == 0:
            print("Erro: A sequência A está vazia.")
            return False
        
        if len(self.sequencia_b) == 0:
            print("Erro: A sequência B está vazia.")
            return False
        
        return True
    
    def encontrar_fracoes_maiores(self):
        """Encontra frações de B que são maiores que pelo menos metade dos números de A"""
        if not self.validar_sequencias():
            return
        
        metade_tamanho_a = len(self.sequencia_a) / 2
        fracoes_resultado = []
        
        for fracao in self.sequencia_b:
            contador_maiores = 0
            
            # Conta quantos números de A são menores que a fração atual
            for numero in self.sequencia_a:
                if fracao.isGreater(numero):
                    contador_maiores += 1
            
            # Se a fração é maior que pelo menos metade dos números de A
            if contador_maiores >= metade_tamanho_a:
                fracoes_resultado.append(fracao)
        
        # Imprime o resultado
        if fracoes_resultado:
            print("Frações de B que são maiores que pelo menos metade dos números de A:")
            for fracao in fracoes_resultado:
                print(fracao)
        else:
            print("Nenhuma fração de B é maior que pelo menos metade dos números de A.")
    
    def executar(self):
        """Executa o programa principal"""
        self.ler_sequencia_a()
        self.ler_sequencia_b()
        self.encontrar_fracoes_maiores()


def calcola_meta_minore(sequenzaA):
    """Calcula a metade da soma de todos os elementos da sequência A"""
    if not sequenzaA:
        return 0.0
    return sum(sequenzaA) / 2


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
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        comparador = ComparaSequenze()
        comparador.executar()