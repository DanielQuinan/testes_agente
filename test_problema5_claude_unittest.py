import unittest
import io
import re
from unittest.mock import patch
from problema5_claude import sortear_premios

premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

class TestSorteio(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_saida_minima_valida(self, mock_stdout):
        """Verifica a saída com as entradas mínimas válidas."""
        sortear_premios(premios_base, participantes_base)
        saida = mock_stdout.getvalue()
        self.assertIn("[LOGO DO EVENTO]", saida)
        self.assertIn("🎁 SORTEIO 1: Viagem", saida)
        self.assertIn("🎁 SORTEIO 2: Notebook", saida)
        ganhadores = re.findall(r"🏆 GANHADOR: (.+)", saida)
        self.assertEqual(len(ganhadores), 2)
        self.assertNotEqual(ganhadores[0], ganhadores[1])
        for g in ganhadores:
            self.assertIn(g, participantes_base)

    def test_menos_de_2_premios(self):
        """Testa a validação de quantidade mínima de prêmios."""
        with self.assertRaises(ValueError) as context:
            sortear_premios(["Camisa"], participantes_base)
        self.assertIn("A lista de prêmios deve conter pelo menos 2 itens", str(context.exception))

    def test_menos_de_5_participantes(self):
        """Testa a validação de quantidade mínima de participantes."""
        with self.assertRaises(ValueError) as context:
            sortear_premios(premios_base, ["Ana", "Bruno", "Carlos", "Diana"])
        self.assertIn("A lista de participantes deve conter pelo menos 5 nomes", str(context.exception))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ordem_premios_preservada(self, mock_stdout):
        """Verifica se a ordem dos prêmios sorteados corresponde à da lista de entrada."""
        sortear_premios(premios_base, participantes_base)
        saida = mock_stdout.getvalue()
        premios_encontrados = re.findall(r"🎁 SORTEIO \d+: (.+)", saida)
        self.assertEqual(premios_encontrados, premios_base)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ganhadores_distintos_com_repetidos(self, mock_stdout):
        """Testa se os ganhadores são distintos mesmo com nomes repetidos na lista."""
        participantes = ["Lucas", "Lucas", "Bruno", "Ana", "Carlos"]
        sortear_premios(premios_base, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"🏆 GANHADOR: (.+)", saida)
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
            ganhadores = tuple(re.findall(r"🏆 GANHADOR: (.+)", saida))
            if len(ganhadores) == 2:
                resultados.add(ganhadores)
        self.assertGreater(len(resultados), 1, "O sorteio não parece aleatório.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_saida_formatada(self, mock_stdout):
        """Verifica se a formatação da saída está correta."""
        sortear_premios(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
        saida = mock_stdout.getvalue()
        self.assertIsNotNone(re.search(r"🎁 SORTEIO \d+: .+", saida))
        self.assertIsNotNone(re.search(r"🏆 GANHADOR: .+", saida))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_participantes_maiusculas_minusculas(self, mock_stdout):
        """Testa se o sorteio diferencia nomes com maiúsculas e minúsculas."""
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        sortear_premios(premios_base, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"🏆 GANHADOR: (.+)", saida)
        self.assertEqual(len(ganhadores), 2)
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_nome_igual_premio_participante(self, mock_stdout):
        """Testa o cenário onde um prêmio tem o mesmo nome de um participante."""
        premios = ["João", "Viagem"]
        participantes = ["João", "Ana", "Carlos", "Diana", "Bruno"]
        sortear_premios(premios, participantes)
        saida = mock_stdout.getvalue()
        ganhadores = re.findall(r"🏆 GANHADOR: (.+)", saida)
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
