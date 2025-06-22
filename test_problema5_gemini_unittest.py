import unittest
import io
import re
from unittest.mock import patch
from problema5_gemini import sortear_premios

premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

class TestSorteio(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_saida_minima_valida(self, mock_stdout):
        """Verifica a saída com as entradas mínimas válidas."""
        sortear_premios(premios_base, participantes_base)
        saida = mock_stdout.getvalue()
        self.assertIn("[LOGO DO EVENTO]", saida)
        self.assertIn("Sorteio do prêmio: Viagem", saida)
        self.assertIn("Sorteio do prêmio: Notebook", saida)
        ganhadores = re.findall(r"Ganhador\(a\): (.+)", saida)
        self.assertEqual(len(ganhadores), 2)
        self.assertNotEqual(ganhadores[0], ganhadores[1])
        for g in ganhadores:
            self.assertIn(g, participantes_base)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menos_de_2_premios(self, mock_stdout):
        """Testa a validação de quantidade mínima de prêmios."""
        sortear_premios(["Camisa"], participantes_base)
        saida = mock_stdout.getvalue()
        self.assertIn("A lista de prêmios deve conter pelo menos dois itens.", saida)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menos_de_5_participantes(self, mock_stdout):
        """Testa a validação de quantidade mínima de participantes."""
        sortear_premios(premios_base, ["Ana", "Bruno", "Carlos", "Diana"])
        saida = mock_stdout.getvalue()
        self.assertIn("A lista de participantes deve conter pelo menos cinco nomes.", saida)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ordem_premios_preservada(self, mock_stdout):
        """Verifica se a ordem dos prêmios sorteados corresponde à da lista de entrada."""
        sortear_premios(premios_base, participantes_base)
        saida = mock_stdout.getvalue()
        premios_encontrados = re.findall(r"Sorteio do prêmio: (.+)", saida)
        self.assertEqual(premios_encontrados, premios_base)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ganhadores_distintos_com_repetidos(self, mock_stdout):
        """Testa se os ganhadores são distintos mesmo com nomes repetidos na lista."""
        participantes = ["Lucas", "Lucas", "Bruno", "Ana", "Carlos"]
        sortear_premios(premios_base, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"Ganhador\(a\): (.+)", saida)
        self.assertEqual(len(ganhadores), 2)
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_resultado_variado(self, mock_stdout):
        """Executa o sorteio várias vezes para verificar a aleatoriedade."""
        resultados = set()
        for _ in range(10):
            mock_stdout.seek(0)
            mock_stdout.truncate(0)
            sortear_premios(premios_base, participantes_base)
            saida = mock_stdout.getvalue()
            ganhadores = tuple(re.findall(r"Ganhador\(a\): (.+)", saida))
            if len(ganhadores) == 2:
                resultados.add(ganhadores)
        self.assertGreater(len(resultados), 1, "O sorteio não parece aleatório.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_saida_formatada(self, mock_stdout):
        """Verifica se a formatação da saída está correta."""
        sortear_premios(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
        saida = mock_stdout.getvalue()
        self.assertIsNotNone(re.search(r"Sorteio do prêmio: .+\nGanhador\(a\): .+", saida))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_participantes_maiusculas_minusculas(self, mock_stdout):
        """Testa se o sorteio diferencia nomes com maiúsculas e minúsculas."""
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        sortear_premios(premios_base, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"Ganhador\(a\): (.+)", saida)
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nome_igual_premio_participante(self, mock_stdout):
        """Testa o cenário onde um prêmio tem o mesmo nome de um participante."""
        premios = ["João", "Viagem"]
        participantes = ["João", "Ana", "Carlos", "Diana", "Bruno"]
        sortear_premios(premios, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"Ganhador\(a\): (.+)", saida)
        self.assertEqual(len(ganhadores), 2)
        for g in ganhadores:
            self.assertIn(g, participantes)

    def test_lista_participantes_nao_modificada(self):
        """Verifica se a lista original de participantes não é alterada."""
        participantes = participantes_base.copy()
        with patch('sys.stdout', new_callable=io.StringIO):
            sortear_premios(premios_base, participantes)
        self.assertEqual(participantes, participantes_base)

if __name__ == "__main__":
    unittest.main()
