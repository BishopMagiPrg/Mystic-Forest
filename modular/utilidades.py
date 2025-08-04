import random

def calcular_dano(min_dano=5, max_dano=10):
    """
    Gera um valor de dano aleatório entre min e max.
    """
    return random.randint(min_dano, max_dano)

def validar_input(opcoes_validas):
    """
    Garante que o input do utilizador está dentro das opções válidas.
    """
    escolha = input("Tua escolha: ").strip()
    while escolha not in opcoes_validas:
        print("❌ Escolha inválida. Tenta novamente.")
        escolha = input("Tua escolha: ").strip()
    return escolha

def mostrar_barra_vida(vida, vida_max=30):
    """
    Mostra uma barra de vida simples para visualização.
    """
    coracoes = "❤️" * (vida // 5)
    print(f"Vida: {vida} {coracoes}")
    