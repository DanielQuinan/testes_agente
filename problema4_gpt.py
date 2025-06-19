import random

def cadastrar_premios():
    premios = []
    print("Cadastro de prêmios (mínimo 2):")
    while len(premios) < 2:
        premio = input(f"Digite o nome do prêmio #{len(premios)+1}: ").strip()
        if premio:
            premios.append(premio)
        else:
            print("Nome do prêmio não pode ser vazio.")
    return premios

def cadastrar_participantes():
    participantes = []
    print("\nCadastro de participantes (mínimo 5):")
    while len(participantes) < 5:
        participante = input(f"Digite o nome do participante #{len(participantes)+1}: ").strip()
        if participante:
            participantes.append(participante)
        else:
            print("Nome do participante não pode ser vazio.")
    return participantes

def realizar_sorteio(premios, participantes):
    sorteados = []
    participantes_restantes = participantes.copy()
    for i in range(2):
        premio = premios[i]
        ganhador = random.choice(participantes_restantes)
        sorteados.append((premio, ganhador))
        participantes_restantes.remove(ganhador)
    return sorteados

def main():
    print("=== SORTEIO DE PRÊMIOS ===")
    print("[LOGOTIPO GENÉRICO]\n")
    premios = cadastrar_premios()
    participantes = cadastrar_participantes()
    input("\nPressione Enter para iniciar o sorteio...")
    resultados = realizar_sorteio(premios, participantes)
    print("\n=== RESULTADOS DO SORTEIO ===")
    for premio, ganhador in resultados:
        print(f"Prêmio: {premio}  |  Ganhador: {ganhador}")

if __name__ == "__main__":
    main()
