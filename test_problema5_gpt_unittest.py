import unittest
import builtins
import re
import random
import unittest.mock
from problema5_gpt import sortear_premios
from io import StringIO

premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

class TestSorteio(unittest.TestCase):
    def test_saida_minima_valida(self):
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios_base, participantes_base)
            saida = mock_stdout.getvalue()
            self.assertIn("[LOGO DO EVENTO]", saida)
            self.assertIn("Prêmio: Viagem", saida)
            self.assertIn("Prêmio: Notebook", saida)
            ganhadores = re.findall(r"Ganhador: (.+)", saida)
            self.assertEqual(len(ganhadores), 2)
            self.assertNotEqual(ganhadores[0], ganhadores[1])
            for g in ganhadores:
                self.assertIn(g, participantes_base)

    def test_menos_de_2_premios(self):
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(["Camisa"], participantes_base)
            saida = mock_stdout.getvalue()
            self.assertIn("É necessário pelo menos dois prêmios.", saida)

    def test_menos_de_5_participantes(self):
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios_base, ["Ana", "Bruno", "Carlos", "Diana"])
            saida = mock_stdout.getvalue()
            self.assertIn("É necessário pelo menos cinco participantes.", saida)

    def test_ordem_premios_preservada(self):
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios_base, participantes_base)
            saida = mock_stdout.getvalue()
            premios_encontrados = re.findall(r"Prêmio: (.+)", saida)
            self.assertEqual(premios_encontrados[:2], premios_base)

    def test_ganhadores_distintos_com_repetidos(self):
        participantes = ["Lucas", "Lucas", "Bruno", "Ana", "Carlos"]
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios_base, participantes)
            saida = mock_stdout.getvalue()
            ganhadores = re.findall(r"Ganhador: (.+)", saida)
            self.assertEqual(len(ganhadores), 2)
            self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_resultado_variado(self):
        resultados = set()
        for _ in range(10):
            with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                sortear_premios(premios_base, participantes_base)
                saida = mock_stdout.getvalue()
                ganhadores = tuple(re.findall(r"Ganhador: (.+)", saida))
                resultados.add(ganhadores)
        self.assertGreater(len(resultados), 1)

    def test_saida_formatada(self):
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
            saida = mock_stdout.getvalue()
            self.assertIsNotNone(re.search(r"Prêmio: .+\nGanhador: .+", saida))

    def test_participantes_maiusculas_minusculas(self):
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios_base, participantes)
            saida = mock_stdout.getvalue()
            ganhadores = re.findall(r"Ganhador: (.+)", saida)
            self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_nome_igual_premio_participante(self):
        premios = ["João", "Viagem"]
        participantes = ["João", "Ana", "Carlos", "Diana", "Bruno"]
        with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            sortear_premios(premios, participantes)
            saida = mock_stdout.getvalue()
            ganhadores = re.findall(r"Ganhador: (.+)", saida)
            self.assertEqual(len(ganhadores), 2)
            for g in ganhadores:
                self.assertIn(g, participantes)

    def test_participantes_restantes_nao_alterados(self):
        participantes = participantes_base.copy()
        with unittest.mock.patch("sys.stdout", new_callable=StringIO):
            sortear_premios(premios_base, participantes)
        self.assertEqual(len(participantes), 5)

if __name__ == "__main__":
    unittest.main()
