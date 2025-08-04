# modular/menu.py

from modular.cenas import caminho_esquerdo, caminho_direito, caminho_frente
from modular.inventario import ver_inventario, usar_item

def menu_principal(inventario, vida_jogador):
    """
    Mostra o menu de navegação principal do jogador.
    """
    print("\nChegas a uma bifurcação. Escolhes ir para:")
    print("1 - Caminho da esquerda (mais escuro e silencioso)")
    print("2 - Caminho da direita (claro com sons de água)")
    print("3 - Caminho em frente (interior da floresta)")
    print("4 - Ver inventário")
    print("5 - Usar item do inventário")
    print("0 - Sair do jogo")

    escolha = input("Digite 1, 2, 3, 4, 5 ou 0: ")

    if escolha == "0":
        print("👋 Obrigado por jogar! Até à próxima.")
        return False, False, vida_jogador
    elif escolha == "4":
        ver_inventario(inventario)
        return False, True, vida_jogador
    elif escolha == "5":
        vida_jogador = usar_item(inventario, vida_jogador)
        return False, True, vida_jogador
    elif escolha == "1":
        return caminho_esquerdo(inventario), True, vida_jogador
    elif escolha == "2":
        return caminho_direito(), True, vida_jogador
    elif escolha == "3":
        return caminho_frente(inventario, vida_jogador)
    else:
        print("❌ Escolha inválida. Tenta novamente.")
        return False, True, vida_jogador