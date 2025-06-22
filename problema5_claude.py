import random

def sortear_premios(premios: list[str], participantes: list[str]) -> None:
    """
    Simula um sorteador de prêmios para eventos.
    
    Args:
        premios: Lista com pelo menos dois prêmios
        participantes: Lista com pelo menos cinco participantes
    
    Raises:
        ValueError: Se não houver prêmios ou participantes suficientes
    """
    # Validação das entradas
    if len(premios) < 2:
        raise ValueError("A lista de prêmios deve conter pelo menos 2 itens")
    
    if len(participantes) < 5:
        raise ValueError("A lista de participantes deve conter pelo menos 5 nomes")
    
    if len(participantes) < len(premios):
        raise ValueError("Não há participantes suficientes para todos os prêmios")
    
    # Exibir logotipo do evento
    print("=" * 50)
    print("          [LOGO DO EVENTO]")
    print("        SORTEIO DE PRÊMIOS")
    print("=" * 50)
    print()
    
    # Criar uma cópia da lista de participantes para não modificar a original
    participantes_disponiveis = participantes.copy()
    
    # Realizar os sorteios
    for i, premio in enumerate(premios, 1):
        print(f"🎁 SORTEIO {i}: {premio}")
        print("-" * 30)
        
        # Sortear um ganhador aleatoriamente
        ganhador = random.choice(participantes_disponiveis)
        
        # Exibir o resultado
        print(f"🏆 GANHADOR: {ganhador}")
        print()
        
        # Remover o ganhador da lista para evitar ganhar novamente
        participantes_disponiveis.remove(ganhador)
    
    print("=" * 50)
    print("     SORTEIO FINALIZADO!")
    print("   Parabéns aos ganhadores!")
    print("=" * 50)


# Exemplo de uso
if __name__ == "__main__":
    # Listas de exemplo
    premios_exemplo = ["Camisa", "Caneca", "Voucher R$ 50", "Fone de Ouvido"]
    participantes_exemplo = [
        "Ana Silva", "Bruno Costa", "Carla Santos", "Diego Oliveira", 
        "Elena Rodrigues", "Fernando Lima", "Gabriela Souza", "Hugo Pereira"
    ]
    
    # Executar o sorteio
    sortear_premios(premios_exemplo, participantes_exemplo)