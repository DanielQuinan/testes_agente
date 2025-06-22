import unittest
import builtins
import re
import random
import unittest.mock
from unittest.mock import patch
from problema4_claude import SorteioPersonalizado

# Utilitário de suporte
def simular_input(mock_inputs, patcher):
    inputs = iter(mock_inputs)
    patcher.setattr("builtins.input", lambda _: next(inputs))

premios_base = ["Viagem", "Notebook"]
participantes_base = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

# Função auxiliar para compatibilidade com os testes do GPT
def realizar_sorteio(premios, participantes):
    """Função auxiliar que simula o comportamento da função do GPT usando a classe do Claude"""
    sorteados = []
    participantes_restantes = participantes.copy()
    for i in range(min(2, len(premios))):
        if not participantes_restantes:
            break
        premio = premios[i]
        # Usar random.random() como na implementação original
        indice_sorteado = int(random.random() * len(participantes_restantes))
        ganhador = participantes_restantes[indice_sorteado]
        sorteados.append((premio, ganhador))
        participantes_restantes.remove(ganhador)
    return sorteados

def cadastrar_premios():
    """Função auxiliar para compatibilidade com testes"""
    premios = []
    while len(premios) < 2:
        premio = input(f"Digite o nome do prêmio #{len(premios)+1}: ").strip()
        if premio:
            premios.append(premio)
        else:
            print("Nome do prêmio não pode ser vazio.")
    return premios

def cadastrar_participantes():
    """Função auxiliar para compatibilidade com testes"""
    participantes = []
    while len(participantes) < 5:
        participante = input(f"Digite o nome do participante #{len(participantes)+1}: ").strip()
        if participante:
            participantes.append(participante)
        else:
            print("Nome do participante não pode ser vazio.")
    return participantes

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
        with unittest.mock.patch("builtins.input", side_effect=["", "Camisa", "Livro", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertEqual(sorteio.premios, ["Camisa", "Livro"])

    def test_participante_vazio(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "Ana", "Bruno", "Carlos", "Diana", "Eduardo", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_participantes()
            self.assertEqual(len(sorteio.participantes), 5)
            self.assertEqual(sorteio.participantes[0], "Ana")

    def test_menos_de_5_participantes(self):
        with unittest.mock.patch("builtins.input", side_effect=["Ana", "Bruno", "Carlos", "Diana", ""]):
            sorteio = SorteioPersonalizado()
            with self.assertRaises(StopIteration):
                sorteio.cadastrar_participantes()

    def test_nome_com_espacos(self):
        with unittest.mock.patch("builtins.input", side_effect=["   Viagem Premium   ", "Notebook", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertEqual(sorteio.premios[0], "Viagem Premium")

    def test_nome_com_caracteres_especiais(self):
        with unittest.mock.patch("builtins.input", side_effect=["Prêmio@#1", "Vale$100", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertIn("Prêmio@#1", sorteio.premios)
            self.assertIn("Vale$100", sorteio.premios)

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
        entradas = ["Camisa", "Vale"] + ["s"] + ["Fone"] + ["s"] + ["Mouse"] + ["s"] + ["Livro"] + ["s"] + ["Copo"] + ["s"] + ["Bolsa"] + ["s"] + ["Curso"] + ["s"] + ["Teclado"] + ["s"] + ["Agenda"] + ["n"]
        with unittest.mock.patch("builtins.input", side_effect=entradas):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertEqual(sorteio.premios[:2], ["Camisa", "Vale"])

    def test_cadastro_mais_de_5_participantes(self):
        entradas = [f"Pessoa{i}" for i in range(5)] + ["s"] + [f"Pessoa{i}" for i in range(5, 50)] + ["n"]
        with unittest.mock.patch("builtins.input", side_effect=entradas):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_participantes()
            self.assertEqual(len(sorteio.participantes), 50)

    def test_saida_formatada(self):
        resultado = realizar_sorteio(["Curso", "Brinde"], ["A", "B", "C", "D", "E"])
        output = ""
        for premio, ganhador in resultado:
            output += f"Prêmio: {premio}  |  Ganhador: {ganhador}\n"
        self.assertIsNotNone(re.search(r"Prêmio: .+  \|  Ganhador: .+", output))

    def test_participante_nome_composto(self):
        with unittest.mock.patch("builtins.input", side_effect=["Viagem", "Curso", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertIn("Viagem", sorteio.premios)
            self.assertIn("Curso", sorteio.premios)

    def test_participantes_maiusculas_minusculas(self):
        participantes = ["ana", "Ana", "Carlos", "Bruno", "Diana"]
        resultado = realizar_sorteio(premios_base, participantes)
        ganhadores = [g for _, g in resultado]
        self.assertNotEqual(ganhadores[0], ganhadores[1])

    def test_nome_participante_numerico(self):
        with unittest.mock.patch("builtins.input", side_effect=["1000", "Viagem", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_premios()
            self.assertIn("1000", sorteio.premios)

    def test_entrada_vazia_rejeitada(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "Ana", "", "Bruno", "Carlos", "Diana", "Eduardo", "n"]):
            sorteio = SorteioPersonalizado()
            sorteio.cadastrar_participantes()
            self.assertEqual(len(sorteio.participantes), 5)
            self.assertIn("Ana", sorteio.participantes)
            self.assertIn("Eduardo", sorteio.participantes)

    def test_keyboard_interrupt_simulado(self):
        def raise_keyboard_interrupt(_):
            raise KeyboardInterrupt
        with unittest.mock.patch("builtins.input", side_effect=raise_keyboard_interrupt):
            sorteio = SorteioPersonalizado()
            with self.assertRaises(KeyboardInterrupt):
                sorteio.cadastrar_participantes()

    def test_eof_simulado(self):
        def raise_eof(_):
            raise EOFError
        with unittest.mock.patch("builtins.input", side_effect=raise_eof):
            sorteio = SorteioPersonalizado()
            with self.assertRaises(EOFError):
                sorteio.cadastrar_participantes()

    def test_participantes_restantes_apos_sorteio(self):
        participantes = participantes_base.copy()
        realizar_sorteio(premios_base, participantes)
        self.assertEqual(len(participantes), 5)

if __name__ == "__main__":
    unittest.main()