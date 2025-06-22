import random
import os

def clear_screen():
    """Limpa o terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_prizes():
    """Coleta os prêmios do usuário."""
    prizes = []
    print("--- Cadastro de Prêmios (mínimo 2) ---")
    while True:
        prize = input(f"Digite o nome do {len(prizes) + 1}º prêmio (ou pressione Enter para finalizar): ").strip()
        if not prize and len(prizes) >= 2:
            break
        elif not prize:
            print("Você precisa cadastrar pelo menos 2 prêmios.")
            continue
        prizes.append(prize)
    return prizes

def get_participants():
    """Coleta os participantes do usuário."""
    participants = []
    print("\n--- Cadastro de Participantes (mínimo 5) ---")
    while True:
        participant = input(f"Digite o nome do {len(participants) + 1}º participante (ou pressione Enter para finalizar): ").strip()
        if not participant and len(participants) >= 5:
            break
        elif not participant:
            print("Você precisa cadastrar pelo menos 5 participantes.")
            continue
        participants.append(participant)
    return participants

def run_raffle(prizes, participants):
    """Executa o sorteio e exibe os resultados."""
    clear_screen()
    print("========================================")
    print("🎉 INICIANDO O SORTEIO! 🎉")
    print("========================================")

    # Copiando as listas para não modificar as originais diretamente
    remaining_participants = list(participants)
    remaining_prizes = list(prizes)

    # --- Primeiro Sorteio ---
    if not remaining_prizes or not remaining_participants:
        print("\nNão há prêmios ou participantes suficientes para o primeiro sorteio.")
        return

    prize1 = random.choice(remaining_prizes)
    remaining_prizes.remove(prize1)

    winner1 = random.choice(remaining_participants)
    remaining_participants.remove(winner1)

    print(f"\n🏆 1º Sorteio 🏆")
    print(f"Prêmio: {prize1}")
    print(f"Ganhador(a): {winner1}")
    print("----------------------------------------")


    # --- Segundo Sorteio ---
    if not remaining_prizes or not remaining_participants:
        print("\nNão há prêmios ou participantes suficientes para o segundo sorteio.")
        return

    prize2 = random.choice(remaining_prizes)
    remaining_prizes.remove(prize2)

    winner2 = random.choice(remaining_participants)
    remaining_participants.remove(winner2)

    print(f"\n🏆 2º Sorteio 🏆")
    print(f"Prêmio: {prize2}")
    print(f"Ganhador(a): {winner2}")
    print("========================================")


def main():
    """Função principal da aplicação."""
    clear_screen()
    print("========================================")
    print("   APLICATIVO DE SORTEIO PERSONALIZADO  ")
    print("========================================")
    print("Bem-vindo! Vamos começar cadastrando os prêmios e participantes.")
    print()

    prizes = get_prizes()
    participants = get_participants()

    print("\n--- Dados Cadastrados ---")
    print("Prêmios:", ", ".join(prizes))
    print("Participantes:", ", ".join(participants))
    print("--------------------------")

    input("\nPressione Enter para iniciar o sorteio...")

    run_raffle(prizes, participants)

if __name__ == "__main__":
    main()
