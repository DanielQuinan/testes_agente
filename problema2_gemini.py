from fractions import Fraction

class ComparaSequenze:
    def __init__(self):
        self.sequencia_A = []
        self.sequencia_B = []

    def ler_sequencia_A(self):
        print("Insira os números reais para a sequência A (insira 0 para terminar):")
        while True:
            try:
                entrada = input()
                numero = float(entrada)
                if numero == 0:
                    break
                self.sequencia_A.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número real.")

    def ler_sequencia_B(self):
        print("Insira as frações para a sequência B no formato num/den (insira uma fração < 0 para terminar):")
        while True:
            try:
                entrada = input()
                # Tenta converter para fração diretamente. Se for um número como "-1", Fraction("-1") funciona.
                # Para o critério de parada "fração menor que 0", precisamos avaliar a fração.
                
                # Primeiro, vamos verificar se a entrada é um número simples que pode ser < 0
                # para o caso de entrada como "-1" para parar, antes de tentar Fraction(entrada)
                # que poderia falhar para "negativo" sem ser num/den.
                # No entanto, a especificação é "fração menor que 0".
                # Então, é melhor construir a fração e depois compará-la.

                if "/" in entrada:
                    num_str, den_str = entrada.split('/')
                    numerador = int(num_str)
                    denominador = int(den_str)
                    if denominador == 0:
                        print("Denominador não pode ser zero. Tente novamente.")
                        continue
                    fracao = Fraction(numerador, denominador)
                else: # Tenta interpretar como um inteiro, ex: "2" -> 2/1, "-1" -> -1/1
                    fracao = Fraction(entrada)

                if fracao < Fraction(0):
                    break
                self.sequencia_B.append(fracao)
            except ValueError:
                print("Entrada inválida. Por favor, insira uma fração no formato num/den ou um número inteiro.")
            except ZeroDivisionError: # Já tratado acima, mas por segurança.
                print("Denominador não pode ser zero. Tente novamente.")


    def comparar_e_imprimir(self):
        if not self.sequencia_A or not self.sequencia_B:
            print("Erro: Ambas as sequências A e B devem conter elementos para a comparação.")
            if not self.sequencia_A:
                print("A sequência A está vazia.")
            if not self.sequencia_B:
                print("A sequência B está vazia.")
            return

        metade_len_A = len(self.sequencia_A) / 2.0
        fracoes_resultado = []

        for fracao_b in self.sequencia_B:
            contador_maiores = 0
            for num_a in self.sequencia_A:
                if fracao_b > num_a: # Fraction objects can be compared directly with floats
                    contador_maiores += 1
            
            if contador_maiores >= metade_len_A:
                fracoes_resultado.append(fracao_b)

        if fracoes_resultado:
            print("\nFrações de B que são maiores que pelo menos metade dos números em A:")
            for fracao in fracoes_resultado:
                print(fracao)
        else:
            print("\nNenhuma fração em B atende ao critério.")

# --- Testes Unitários --- 
import builtins # Necessário para mockar input
# A classe ComparaSequenze e from fractions import Fraction já estão definidas acima no arquivo.

def testAcquisisciSequenzaRealiNotNull():
    import builtins
    original_input = builtins.input
    builtins.input = lambda: "0"  # Simula o usuário digitando apenas 0
    cs = ComparaSequenze()
    cs.ler_sequencia_A() # MODIFICADO: ler_sequencia_A não retorna valor, modifica cs.sequencia_A
    # MODIFICADO: Verifica o atributo da instância em vez de um valor de retorno.
    # Para entrada "0", a sequência A deve ficar vazia, mas não nula.
    assert cs.sequencia_A is not None, "cs.sequencia_A should not be null"
    assert cs.sequencia_A == [], "cs.sequencia_A should be empty for input '0'"
    builtins.input = original_input
    print("testAcquisisciSequenzaRealiNotNull passou!")

def testAcquisisciSequenzaRealiContents():
    import builtins
    original_input = builtins.input
    inputs = iter(["1.0", "2.0", "3.0", "4.0", "0"])
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    cs.ler_sequencia_A() # MODIFICADO: ler_sequencia_A não retorna valor, modifica cs.sequencia_A
    expected = [1.0, 2.0, 3.0, 4.0]
    # MODIFICADO: Compara o atributo da instância cs.sequencia_A
    assert cs.sequencia_A == expected, f"Esperado {expected}, mas obteve {cs.sequencia_A}"
    builtins.input = original_input
    print("testAcquisisciSequenzaRealiContents passou!")

def testAcquisisciSequenzaFrazioniNotNull():
    import builtins
    original_input = builtins.input
    inputs = iter(["-1/2"]) # Simula o usuário digitando uma fração negativa logo de início
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    cs.ler_sequencia_B() # MODIFICADO: ler_sequencia_B não retorna valor, modifica cs.sequencia_B
    # MODIFICADO: Verifica o atributo da instância em vez de um valor de retorno.
    # Para entrada "-1/2", a sequência B deve ficar vazia, mas não nula.
    assert cs.sequencia_B is not None, "cs.sequencia_B should not be null"
    assert cs.sequencia_B == [], "cs.sequencia_B should be empty for input '-1/2'"
    builtins.input = original_input
    print("testAcquisisciSequenzaFrazioniNotNull passou!")

def testAcquisisciSequenzaFrazioniContents():
    import builtins
    original_input = builtins.input
    inputs = iter(["1/10", "100/2", "100/100", "5/4", "-1/2"])
    builtins.input = lambda: next(inputs)
    cs = ComparaSequenze()
    cs.ler_sequencia_B() # MODIFICADO: ler_sequencia_B não retorna valor, modifica cs.sequencia_B
    expected = [Fraction(1, 10), Fraction(100, 2), Fraction(100, 100), Fraction(5, 4)]
    # MODIFICADO: Compara o atributo da instância cs.sequencia_B
    assert len(cs.sequencia_B) == len(expected), f"Esperado {len(expected)} frações, mas obteve {len(cs.sequencia_B)}"
    for r, e in zip(cs.sequencia_B, expected):
        # MODIFICADO: Usa .numerator e .denominator em vez de getNumerator() e getDenominator()
        assert r.numerator == e.numerator and r.denominator == e.denominator, \
            f"Esperado {e.numerator}/{e.denominator}, mas obteve {r.numerator}/{r.denominator}"
    builtins.input = original_input
    print("testAcquisisciSequenzaFrazioniContents passou!")

# Esta função não faz parte da classe ComparaSequenze, é uma função auxiliar para teste.
def calcola_meta_minore(sequenzaA):
    if not sequenzaA: # Adicionada verificação para lista vazia para evitar ZeroDivisionError se sum/len fosse usado
        return 0.0
    # A lógica original "Soma todos os elementos e divide por 2" é mantida.
    return sum(sequenzaA) / 2.0

def testCalcolaMetaMinore():
    sequenzaA = [2.0, 4.0, 6.0]
    expected = 6.0 # (2+4+6)/2 = 12/2 = 6
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
    assert frazione is not None, "Frazione object should not be null"
    # MODIFICADO: Usa .numerator e .denominator em vez de getNumerator() e getDenominator()
    assert frazione.numerator == 2, f"Esperado numerador 2, mas obteve {frazione.numerator}"
    assert frazione.denominator == 3, f"Esperado denominador 3, mas obteve {frazione.denominator}"
    print("testFrazione3Constructor passou!")

def testFrazione3IsMaggiore():
    frazione1 = Fraction(1, 2)
    frazione2 = Fraction(1, 3)
    # MODIFICADO: Usa o operador > em vez de isGreater()
    assert frazione1 > frazione2, "1/2 should be greater than 1/3"
    print("testFrazione3IsMaggiore passou!")

# Bloco para executar os testes (será adicionado ao final do arquivo)
# Se o arquivo já tiver um if __name__ == "__main__": para a lógica principal,
# este bloco também será executado se o script for chamado diretamente.

if __name__ == "__main__":
    print("\n--- Executando Testes Unitários ---")
    # cs = ComparaSequenze() # Instância local para testes, não interfere com a de cima se houver.
    # As funções de teste criam suas próprias instâncias de ComparaSequenze conforme necessário.
    
    testAcquisisciSequenzaRealiNotNull()
    testAcquisisciSequenzaRealiContents()
    testAcquisisciSequenzaFrazioniNotNull()
    testAcquisisciSequenzaFrazioniContents()
    testCalcolaMetaMinore()
    testCalcolaMetaMinoreEmptyList()
    testFrazione3Constructor()
    testFrazione3IsMaggiore()
    print("--- Testes Unitários Concluídos ---")
