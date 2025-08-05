def ver_inventario(inventario):
    if not inventario:
        print("\n📦 Inventário: Vazio")
    else:
        print("\n📦 Inventário:")
        for item in inventario:
            print(f" - {item}")
        
def usar_item(inventario, vida_jogador):
    if not inventario:
        print("📭 O teu inventário está vazio.")
        return vida_jogador
    
    print("\nItens disponíveis:")
    for i, item in enumerate(inventario):
        print(f"{i + 1} - {item}")

    escolha = input("Escolhe o número do item a usar (ou Enter para cancelar): ")

    if escolha.isdigit():
        indice = int(escolha) - 1
        if  0 <= indice < len(inventario):
            if item == "poção de cura":
                vida_jogador += 10
                inventario.pop(indice)
                print("🧪 Usate uma poção de cura. +10 de vida!")
            else:
                print(f"ℹ️ O item '{item}' não pode ser usado agora.")
        else:
            print("❌ Número inválido.")
    else:
        print("🚫 Cancelado.")
    
    return vida_jogador