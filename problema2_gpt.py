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

def testAcquisisciSequenzaRealiNotNull():
    import builtins
    original_input = builtins.input
    builtins.input = lambda: "0"  # Simula o usuário digitando apenas 0
    cs = ComparaSequenze()
    resultado = cs.ler_sequencia_A()
    assert resultado is not None, "Sequenza A should not be null"
    builtins.input = original_input
    print("testAcquisisciSequenzaRealiNotNull passou!")

def testAcquisisciSequenzaRealiContents():
    import builtins
    original_input = builtins.input
    inputs = iter(["1.0", "2.0", "3.0", "4.0", "0"])
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    resultado = cs.ler_sequencia_A()
    expected = [1.0, 2.0, 3.0, 4.0]
    assert resultado == expected, f"Esperado {expected}, mas obteve {resultado}"
    builtins.input = original_input
    print("testAcquisisciSequenzaRealiContents passou!")

def testAcquisisciSequenzaFrazioniNotNull():
    import builtins
    original_input = builtins.input
    # Simula o usuário digitando uma fração negativa logo de início
    inputs = iter(["-1/2"])
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    resultado = cs.ler_sequencia_B()
    assert resultado is not None, "Sequenza B should not be null"
    builtins.input = original_input
    print("testAcquisisciSequenzaFrazioniNotNull passou!")

def testAcquisisciSequenzaFrazioniContents():
    import builtins
    original_input = builtins.input
    inputs = iter(["1/10", "100/2", "100/100", "5/4", "-1/2"])
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    resultado = cs.ler_sequencia_B()
    expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
    # Compara numerador e denominador de cada fração
    assert len(resultado) == len(expected), f"Esperado {len(expected)} frações, mas obteve {len(resultado)}"
    for r, e in zip(resultado, expected):
        assert r.getNumerator() == e.getNumerator() and r.getDenominator() == e.getDenominator(), \
            f"Esperado {e.getNumerator()}/{e.getDenominator()}, mas obteve {r.getNumerator()}/{r.getDenominator()}"
    builtins.input = original_input
    print("testAcquisisciSequenzaFrazioniContents passou!")

def calcola_meta_minore(sequenzaA):
    # Soma todos os elementos e divide por 2
    return sum(sequenzaA) / 2


def testCalcolaMetaMinore():
    sequenzaA = [2.0, 4.0, 6.0]
    expected = 6.0
    result = calcola_meta_minore(sequenzaA)
    assert abs(result - expected) < 0.001, f"Esperado {expected}, mas obteve {result}"
    print("testCalcolaMetaMinore passou!")

def testCalcolaMetaMinoreEmptyList():
    sequenzaA = []
    expected = 0.0
    result = calcola_meta_minore(sequenzaA)
    assert abs(result - expected) < 0.001, f"Esperado {expected}, mas obteve {result}"
    print("testCalcolaMetaMinoreEmptyList passou!")

def testFrazione3Constructor():
    frazione = Fraction(2, 3)
    assert frazione is not None, "Frazione3 object should not be null"
    assert frazione.getNumerator() == 2, f"Esperado numerador 2, mas obteve {frazione.getNumerator()}"
    assert frazione.getDenominator() == 3, f"Esperado denominador 3, mas obteve {frazione.getDenominator()}"
    print("testFrazione3Constructor passou!")

def testFrazione3IsMaggiore():
    frazione1 = Fraction(1, 2)
    frazione2 = Fraction(1, 3)
    assert frazione1.isGreater(frazione2), "1/2 should be greater than 1/3"
    print("testFrazione3IsMaggiore passou!")

if __name__ == "__main__":
    cs = ComparaSequenze()
    testAcquisisciSequenzaRealiNotNull()
    testAcquisisciSequenzaRealiContents()
    testAcquisisciSequenzaFrazioniNotNull()
    testAcquisisciSequenzaFrazioniContents()
    testCalcolaMetaMinore()
    testCalcolaMetaMinoreEmptyList()
    testFrazione3Constructor()
    testFrazione3IsMaggiore()


