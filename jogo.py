from modular.menu import menu_principal

def iniciar_jogo():
    print("\n🌲 Bem-vindo à Floresta Misteriosa 🌲")
    print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...")

    inventario = []
    vida_jogador = 30
    jogo_ativo = True
    final_alcancado = False

    while jogo_ativo and not final_alcancado:
        final_alcancado, jogo_ativo, vida_jogador = menu_principal(inventario, vida_jogador)

if __name__ == "__main__":
    iniciar_jogo()