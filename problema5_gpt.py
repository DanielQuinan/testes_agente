import random

def sortear_premios(premios: list[str], participantes: list[str]) -> None:
    # Exibe o logotipo do evento
    print("[LOGO DO EVENTO]\n")

    if len(premios) < 2:
        print("É necessário pelo menos dois prêmios.")
        return
    if len(participantes) < 5:
        print("É necessário pelo menos cinco participantes.")
        return

    # Sorteio do primeiro prêmio
    ganhador1 = random.choice(participantes)
    print(f"Prêmio: {premios[0]}")
    print(f"Ganhador: {ganhador1}\n")

    # Remove o ganhador do primeiro prêmio
    participantes_restantes = [p for p in participantes if p != ganhador1]

    # Sorteio do segundo prêmio
    ganhador2 = random.choice(participantes_restantes)
    print(f"Prêmio: {premios[1]}")
    print(f"Ganhador: {ganhador2}\n")
