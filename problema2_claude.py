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


# Executa o programa principal
if __name__ == "__main__":
    print("\n--- Executando ComparaSequenze ---")
    print("Digite os números reais para a sequência A (termine com 0):")
    cs = ComparaSequenze()
    print("Digite as frações para a sequência B no formato num/den (termine com fração < 0):")
    cs.processar()