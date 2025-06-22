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

def calcola_meta_minore(sequenzaA):
    if not sequenzaA:
        return 0.0
    return sum(sequenzaA) / 2.0
