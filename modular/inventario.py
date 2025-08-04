# modular/inventario.py

def inicializar_jogador():
    """
    Inicializa o estado do jogador com um inventário vazio e vida inicial.
    """
    inventario = []
    vida = 30
    return inventario, vida

def ver_inventario(inventario):
    """
    Mostra os itens atuais do jogador.
    """
    if not inventario:
        print("\n📦 O teu inventário está vazio.")
    else:
        print("\n📦 Inventário:")
        for item in inventario:
            print(f" - {item}")

def usar_item(inventario, vida):
    """
    Permite ao jogador usar um item, como a poção de cura.
    """
    if not inventario:
        print("📭 O teu inventário está vazio,")
        return vida
    
    print("\nItens disponíveis:")
    for i, item in enumerate(inventario):
        print(f"{i + 1} - {item}")

    escolha = input("Escolhe o número do item a usar (ou Enter para cancelar): ")

    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(inventario):
            item = inventario[indice]
            if item == "poção de cura":
                vida += 10
                inventario.pop(indice)
                print("🧪 Usate uma poção de cura. +10 de vida!")
            else:
                print(f"ℹ️ O item '{item}' não pode ser usado agora.")
        else:
            print("❌ Número inválido.")
    else:
        print("🚫 Cancelado.")
    
    return vida