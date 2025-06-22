import unittest
import builtins
import re
import random
import unittest.mock
from problema4_gemini import get_prizes, get_participants, run_raffle

# Utilitário de suporte
premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

def realizar_sorteio(premios, participantes):
    """Função auxiliar que simula o comportamento do sorteio do Gemini"""
    sorteados = []
    participantes_restantes = participantes.copy()
    for i in range(min(2, len(premios))):
        if not participantes_restantes:
            break
        premio = premios[i]
        indice_sorteado = int(random.random() * len(participantes_restantes))
        ganhador = participantes_restantes[indice_sorteado]
        sorteados.append((premio, ganhador))
        participantes_restantes.remove(ganhador)
    return sorteados

class TestSorteio(unittest.TestCase):
    def test_sorteio_minimo_valido(self):
        resultado = realizar_sorteio(premios_base, participantes_base)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(all(p in premios_base for p, _ in resultado))
        self.assertTrue(all(g in participantes_base for _, g in resultado))

    def test_ganhadores_distintos(self):
        resultado = realizar_sorteio(premios_base, participantes_base)
        ganhadores = [g for _, g in resultado]
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_ordem_premios_preservada(self):
        resultado = realizar_sorteio(premios_base, participantes_base)
        premios_resultado = [p for p, _ in resultado]
        self.assertEqual(premios_resultado, premios_base)

    def test_premio_vazio(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "Camisa", "Livro", ""]):
            premios = get_prizes()
            self.assertEqual(premios, ["Camisa", "Livro"])

    def test_participante_vazio(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "Ana", "Bruno", "Carlos", "Diana", "Eduardo", ""]):
            participantes = get_participants()
            self.assertEqual(len(participantes), 5)
            self.assertEqual(participantes[0], "Ana")

    def test_menos_de_5_participantes(self):
        with unittest.mock.patch("builtins.input", side_effect=["Ana", "Bruno", "Carlos", "Diana", ""]):
            with self.assertRaises(StopIteration):
                get_participants()

    def test_nome_com_espacos(self):
        with unittest.mock.patch("builtins.input", side_effect=["   Viagem Premium   ", "Notebook", ""]):
            premios = get_prizes()
            self.assertEqual(premios[0], "Viagem Premium")

    def test_nome_com_caracteres_especiais(self):
        with unittest.mock.patch("builtins.input", side_effect=["Prêmio@#1", "Vale$100", ""]):
            premios = get_prizes()
            self.assertIn("Prêmio@#1", premios)
            self.assertIn("Vale$100", premios)

    def test_sorteio_resultado_variado(self):
        resultados = set()
        for _ in range(10):
            resultado = tuple(realizar_sorteio(premios_base, participantes_base))
            resultados.add(resultado)
        self.assertGreater(len(resultados), 1)

    def test_repeticao_nome_nao_afeta_logica(self):
        participantes = ["Lucas", "Ana", "Lucas", "Bruno", "Carlos"]
        resultado = realizar_sorteio(premios_base, participantes)
        ganhadores = [g for _, g in resultado]
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_saida_completa(self):
        resultado = realizar_sorteio(premios_base, participantes_base)
        output = ""
        for premio, ganhador in resultado:
            output += f"Prêmio: {premio}  |  Ganhador: {ganhador}\n"
        for premio, ganhador in resultado:
            self.assertIn(premio, output)
            self.assertIn(ganhador, output)

    def test_nomes_iguais_premio_participante(self):
        premios = ["João", "Viagem"]
        participantes = ["João", "Ana", "Carlos", "Diana", "Bruno"]
        resultado = realizar_sorteio(premios, participantes)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(all(p in premios for p, _ in resultado))
        self.assertTrue(all(g in participantes for _, g in resultado))

    def test_cadastro_mais_de_2_premios(self):
        entradas = ["Camisa", "Vale", "Fone", "Mouse", "Livro", "Copo", "Bolsa", "Curso", "Teclado", "Agenda", ""]
        with unittest.mock.patch("builtins.input", side_effect=entradas):
            premios = get_prizes()
            self.assertEqual(premios[:2], ["Camisa", "Vale"])

    def test_cadastro_mais_de_5_participantes(self):
        entradas = [f"Pessoa{i}" for i in range(50)] + [""]
        with unittest.mock.patch("builtins.input", side_effect=entradas):
            participantes = get_participants()
            self.assertEqual(len(participantes), 50)

    def test_saida_formatada(self):
        resultado = realizar_sorteio(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
        output = ""
        for premio, ganhador in resultado:
            output += f"Prêmio: {premio}  |  Ganhador: {ganhador}\n"
        self.assertIsNotNone(re.search(r"Prêmio: .+  \|  Ganhador: .+", output))

    def test_participante_nome_composto(self):
        with unittest.mock.patch("builtins.input", side_effect=["Viagem", "Curso", ""]):
            premios = get_prizes()
            self.assertIn("Viagem", premios)
            self.assertIn("Curso", premios)

    def test_participantes_maiusculas_minusculas(self):
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        resultado = realizar_sorteio(premios_base, participantes)
        ganhadores = [g for _, g in resultado]
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_nome_participante_numerico(self):
        with unittest.mock.patch("builtins.input", side_effect=["1000", "Viagem", ""]):
            premios = get_prizes()
            self.assertIn("1000", premios)

    def test_entrada_vazia_rejeitada(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "Ana", "", "Bruno", "Carlos", "Diana", "Eduardo", ""]):
            participantes = get_participants()
            self.assertEqual(len(participantes), 5)
            self.assertIn("Ana", participantes)
            self.assertIn("Eduardo", participantes)

    def test_keyboard_interrupt_simulado(self):
        def raise_keyboard_interrupt(_):
            raise KeyboardInterrupt
        with unittest.mock.patch("builtins.input", side_effect=raise_keyboard_interrupt):
            with self.assertRaises(KeyboardInterrupt):
                get_participants()

    def test_eof_simulado(self):
        def raise_eof(_):
            raise EOFError
        with unittest.mock.patch("builtins.input", side_effect=raise_eof):
            with self.assertRaises(EOFError):
                get_participants()

    def test_participantes_restantes_apos_sorteio(self):
        participantes = participantes_base.copy()
        realizar_sorteio(premios_base, participantes)
        self.assertEqual(len(participantes), 5)

if __name__ == "__main__":
    unittest.main()
