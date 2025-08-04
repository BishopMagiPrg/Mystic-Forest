# modular/cenas.py

from modular.combate import combate
from modular.enigma import enigma_final

def caminho_esquerdo(inventario):
    """
    Cena do caminho da esquerda: o jogador encontra um guardião.
    """
    print("\n🌑 Caminhas pelo trilho escuro... Surge um velho guardião.")
    print("Ele oferece-te um objeto misterioso.")
    print("1 - Aceitar\n2 - Recusar")
    escolha = input("Tua escolha: ")

    if escolha == "1":
        if "mapa mágico" not in inventario:
            print("🎁 Recebeste um mapa mágico e uma poção de cura!")
            inventario.append("mapa mágico")
            inventario.append("poção de cura")
        else:
            print("🗺️ Já tens o mapa mágico.")
    else:
        print("🚪 Recusas o objeto. O guardião desapareceu.")
    return False, True, None # nenhum final, jogo continua, sem alteração da vida

def caminho_direito():
    """
    Cena do caminho da direita: um desafio lógico.
    """
    print("\n💧 Encontras um lago e um a criatura propõe um desafio lógico.")
    print("1 - Aceitar\n2 - Recusar")
    escolha = input("Tua escolha: ")

    if escolha == "1":
        print("❓ Qual é o número mágico entre 1 e 10?")
        resposta = input("Tenta adivinhar: ")
        if resposta == "7":
            print("🎯 Acertaste! Final bom: chegas à Cidade Submersa!")
        else:
            print("💥 Erro! A ponte desaparece. Final neutro.")
        return True, True, None
    else:
        print("🐍 A criatura desaparece. Final sombrio.")
        return True, True, None
    
def caminho_frente(inventario, vida_jogador):
    """
    Cena do caminho da frente: inclui combate e enigma
    """
    print("\n🌲 Encontras um portal misterioso na floresta.")
    print("1 - Entrar\n2 - Voltar atrás")
    escolha = input("Decisão: ")

    if escolha == "1":
        venceu, vida_jogador = combate(vida_jogador)
        if venceu:
            return enigma_final(inventario, vida_jogador)
        else:
            return True, True, vida_jogador
    else:
        print("🔄 Voltas à bifurcação.")
        return False, True, vida_jogador