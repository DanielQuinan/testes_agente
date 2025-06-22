import random

def sortear_premios(premios: list[str], participantes: list[str]) -> None:
    """
    Simula um sorteador de prêmios para um evento.

    Args:
        premios: Uma lista com os prêmios a serem sorteados.
        participantes: Uma lista com os nomes dos participantes.
    """
    print("[LOGO DO EVENTO]")
    print("-" * 20)

    if len(premios) < 2:
        print("A lista de prêmios deve conter pelo menos dois itens.")
        return
    if len(participantes) < 5:
        print("A lista de participantes deve conter pelo menos cinco nomes.")
        return

    # Sorteio do primeiro prêmio
    premio1 = premios[0]
    ganhador1 = random.choice(participantes)
    print(f"Sorteio do prêmio: {premio1}")
    print(f"Ganhador(a): {ganhador1}")
    print("-" * 20)

    # Garante que o ganhador do primeiro prêmio seja excluído do segundo sorteio
    participantes_restantes = list(participantes)
    participantes_restantes.remove(ganhador1)

    # Sorteio do segundo prêmio
    premio2 = premios[1]
    ganhador2 = random.choice(participantes_restantes)
    print(f"Sorteio do prêmio: {premio2}")
    print(f"Ganhador(a): {ganhador2}")
    print("-" * 20)
