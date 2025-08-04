from modular.cenas import menu_principal
from modular.inventario import inicializar_jogador
import os

def iniciar_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n🌲 Bem-vindo à Floresta Misteriosa 🌲")
    print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...\n")

    inventario, vida = inicializar_jogador()
    jogo_ativo = True
    final_alcancado = False

    while jogo_ativo and not final_alcancado:
        final_alcancado, jogo_ativo, vida = menu_principal(inventario, vida)

    print("\n👋 Obrigado por jogar!")

if __name__ == "__main__":
    iniciar_jogo()
