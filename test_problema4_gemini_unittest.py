import unittest
from unittest.mock import patch, call
import io
import re
from problema4_gemini import get_prizes, get_participants, run_raffle

# Prêmios e participantes base para os testes
premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

class TestSorteioAdaptado(unittest.TestCase):
    """ Testes adaptados do GPT para o programa Gemini. """

    def capture_raffle_output(self, prizes, participants):
        """Captura a saída de run_raffle para análise."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with patch('problema4_gemini.clear_screen', return_value=None): # Evita limpar a tela durante os testes
                run_raffle(prizes, participants)
                return mock_stdout.getvalue()

    def test_sorteio_minimo_valido(self):
        output = self.capture_raffle_output(premios_base, participantes_base)
        winners = re.findall(r"Ganhador\(a\): (.*)", output)
        drawn_prizes = re.findall(r"Prêmio: (.*)", output)
        self.assertEqual(len(winners), 2)
        self.assertTrue(all(p in premios_base for p in drawn_prizes))
        self.assertTrue(all(g in participantes_base for g in winners))

    def test_ganhadores_distintos(self):
        output = self.capture_raffle_output(premios_base, participantes_base)
        ganhadores = re.findall(r"Ganhador\(a\): (.*)", output)
        self.assertEqual(len(ganhadores), 2)
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_premios_sorteados_distintos(self):
        """Verifica se os prêmios sorteados são distintos."""
        output = self.capture_raffle_output(premios_base, participantes_base)
        premios_resultado = re.findall(r"Prêmio: (.*)", output)
        self.assertEqual(len(premios_resultado), 2)
        self.assertNotEqual(premios_resultado[0], premios_resultado[1])

    def test_premio_vazio(self):
        """Testa se a entrada de prêmio vazio é ignorada até o mínimo ser atingido."""
        with patch('builtins.input', side_effect=["", "Camisa", "Livro", ""]):
            with patch('sys.stdout', new_callable=io.StringIO): # Suprime prints de aviso
                premios = get_prizes()
                self.assertEqual(premios, ["Camisa", "Livro"])

    def test_participante_vazio(self):
        """Testa se a entrada de participante vazio é ignorada até o mínimo ser atingido."""
        with patch('builtins.input', side_effect=["", "Ana", "Bruno", "Carlos", "Diana", "Eduardo", ""]):
            with patch('sys.stdout', new_callable=io.StringIO): # Suprime prints de aviso
                participantes = get_participants()
                self.assertEqual(len(participantes), 5)
                self.assertEqual(participantes[0], "Ana")

    def test_participantes_repetidos(self):
        participantes = ["Lucas", "Lucas", "Bruno", "Ana", "Carlos"]
        output = self.capture_raffle_output(premios_base, participantes)
        ganhadores = re.findall(r"Ganhador\(a\): (.*)", output)
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_menos_de_5_participantes_forca_minimo(self):
        """Verifica se o programa insiste no mínimo de 5 participantes."""
        inputs = ["Ana", "Bruno", "Carlos", "Diana", "", "Eduardo", ""]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                participantes = get_participants()
                self.assertEqual(len(participantes), 5)
                self.assertIn("Você precisa cadastrar pelo menos 5 participantes.", mock_stdout.getvalue())

    def test_nome_com_espacos(self):
        """Verifica se o .strip() está funcionando."""
        with patch('builtins.input', side_effect=["   Viagem Premium   ", "Notebook", ""]):
            premios = get_prizes()
            self.assertEqual(premios[0], "Viagem Premium")

    def test_nome_com_caracteres_especiais(self):
        with patch('builtins.input', side_effect=["Prêmio@#1", "Vale$100", ""]):
            premios = get_prizes()
            self.assertIn("Prêmio@#1", premios)
            self.assertIn("Vale$100", premios)

    def test_ordem_premios_nao_garantida(self):
        """Verifica se os prêmios sorteados estão na lista original, já que a ordem não é preservada."""
        output = self.capture_raffle_output(premios_base, participantes_base)
        premios_resultado = re.findall(r"Prêmio: (.*)", output)
        # A ordem não é garantida, então verificamos se todos os prêmios sorteados estavam na lista original
        self.assertTrue(all(p in premios_base for p in premios_resultado))

    def test_entrada_vazia_rejeitada(self):
        """Testa se entradas vazias são rejeitadas até o mínimo ser atingido."""
        inputs = ["", "Ana", "", "Bruno", "Carlos", "Diana", "Eduardo", ""]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO): # Suprime prints de aviso
                participantes = get_participants()
                self.assertEqual(len(participantes), 5)
                self.assertNotIn("", participantes)
                self.assertEqual(participantes, ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"])

    def test_sorteio_resultado_variado(self):
        """Garante que o sorteio não produz sempre o mesmo resultado."""
        resultados = set()
        for _ in range(10): # Roda o sorteio várias vezes para garantir aleatoriedade
            output = self.capture_raffle_output(premios_base, participantes_base)
            resultados.add(output)
        self.assertGreater(len(resultados), 1, "O sorteio produziu o mesmo resultado repetidamente.")

    def test_saida_completa(self):
        output = self.capture_raffle_output(premios_base, participantes_base)
        drawn_prizes = re.findall(r"Prêmio: (.*)", output)
        winners = re.findall(r"Ganhador\(a\): (.*)", output)
        self.assertIn(drawn_prizes[0], output)
        self.assertIn(winners[0], output)
        self.assertIn(drawn_prizes[1], output)
        self.assertIn(winners[1], output)

    def test_nomes_iguais_premio_participante(self):
        premios = ["João", "Viagem"]
        participantes = ["João", "Ana", "Carlos", "Diana", "Bruno"]
        output = self.capture_raffle_output(premios, participantes)
        self.assertEqual(len(re.findall(r"Ganhador\(a\): .*", output)), 2)

    def test_cadastro_mais_de_2_premios(self):
        entradas = ["Camisa", "Vale", "Fone", ""]
        with patch('builtins.input', side_effect=entradas):
            premios = get_prizes()
            self.assertEqual(len(premios), 3)
            self.assertEqual(premios, ["Camisa", "Vale", "Fone"])

    def test_cadastro_mais_de_5_participantes(self):
        entradas = [f"Pessoa{i}" for i in range(10)] + [""]
        with patch('builtins.input', side_effect=entradas):
            participantes = get_participants()
            self.assertEqual(len(participantes), 10)

    def test_saida_formatada(self):
        output = self.capture_raffle_output(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
        # Verifica o formato de cada sorteio
        self.assertIn("🏆 1º Sorteio 🏆", output)
        self.assertIn("🏆 2º Sorteio 🏆", output)
        self.assertEqual(output.count("Prêmio:"), 2)
        self.assertEqual(output.count("Ganhador(a):"), 2)

    def test_participante_nome_composto(self):
        with patch('builtins.input', side_effect=["Ana Maria", "Bruno Silva", "Carlos Souza", "Diana Costa", "Eduardo Lima", ""]):
            participantes = get_participants()
            self.assertIn("Ana Maria", participantes)
            self.assertIn("Eduardo Lima", participantes)

    def test_participantes_maiusculas_minusculas(self):
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        output = self.capture_raffle_output(premios_base, participantes)
        ganhadores = [g.lower() for g in re.findall(r"Ganhador\(a\): (.*)", output)]
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_nome_premio_numerico(self):
        with patch('builtins.input', side_effect=["1000", "Viagem", ""]):
            premios = get_prizes()
            self.assertIn("1000", premios)

    def test_keyboard_interrupt_simulado(self):
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                get_participants()

    def test_eof_simulado(self):
        with patch('builtins.input', side_effect=EOFError):
            with self.assertRaises(EOFError):
                get_prizes()

    def test_participantes_restantes_apos_sorteio(self):
        """Verifica se a lista original de participantes não é modificada."""
        participantes_originais = participantes_base.copy()
        self.capture_raffle_output(premios_base, participantes_originais)
        self.assertEqual(len(participantes_originais), 5)
        self.assertEqual(participantes_originais, participantes_base)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
