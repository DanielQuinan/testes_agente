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


