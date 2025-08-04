import random

# Função principal do jogo
def inicial_jogo():
    print("\n🌲 Bem-vindo à Floresta Misteriosa 🌲")
    print("Tu és um explorador corajoso que entra numa floresta cheia de segredo...")

    inventario = []
    jogo_ativo = True
    final_alcancado = False

    while jogo_ativo and not final_alcancado:
        final_alcancado, jogo_ativo = menu_principal(inventario)

# Menu de escolhas principais

def menu_principal(inventario):
    print("\nChegas a uma bifurcação. Escolhes ir para:")
    print("1 - Caminho da esquerda (mais escuro e silencioso)")
    print("2 - Caminho da direita (claro com sons de água)")
    print("3 - Caminho em frente (interior da floresta)")
    print("4 - Ver inventário")
    print("0 - Sair do jogo")

    escolha = input("Digite 1, 2, 3, 4 ou 0: ")

    if escolha == "0":
        print("👋 Obrigado por jogar! Até à próxima.")
        return False, False
    elif escolha == "4":
        print(f"\n📦 Inventário: {inventario if inventario else 'Vazio'}")
        return False, True
    elif escolha == "1":
        return caminho_esquerdo(inventario), True
    elif escolha == "2":
        return caminho_direito(), True
    elif escolha == "3":
        return caminho_frente(inventario), True
    else:
        print("❌ Escolha inválida. Tenta novamente.")
        return False, True

# Caminho da esquerda - encontro com o guardião

def caminho_esquerdo(inventario):
    print("\n🌑 Caminhas pelo trilho escuro... Surge um velho guardião.")
    print("Ele oferece-te um objecto misterioso.")
    print("1 - Aceitar\n2 - Recusar")
    escolha = input("Tua escolha: ")

    if escolha == "1":
        if "mapa mágico" not in inventario:
            print("🎁 Recebeste um mapa mágico!")
            inventario.append("mapa mágico")
        else:
            print("🗺️ Já tens o mapa mágico.")
    else:
        print("🚪 Recusas o objecto. O guardião desaparece.")
    return False

# Caminho da direita - desafio Lógico com criatura aquática

def caminho_direito():
    print("\n💧 Encontras um lago e uma criatura propõe um desafio lógico.")
    print("1 - Aceitar\n2 - Recusar")
    escolha = input("Tua escolha: ")

    if escolha == "1":
        print("❓ Qual é o número mágico entre 1 e 10?")
        resposta = input("Tenta adivinhar: ")
        if resposta == "7":
            print("🎯 Acertaste! Final bom: chegas à Cidade Submersa!")
        else:
            print("💥 Erro! A ponte desaparece. Final neutro.")
        return True
    else:
        print("🐍 A criatura desaparece. Final sombrio.")
        return True

# Caminho da frente - inclui combate + enigma

def caminho_frente(inventario):
    print("\n🌲 Encontras um portal misterioso na floresta.")
    print("1 - Entrar\n2 - Voltar atrás")
    escolha = input("Decisão: ")

    if escolha == "1":
        venceu = combate()
        if venceu:
            return enigma_final(inventario)
        else:
            return True
    else:
        print("🔄 Voltas à bifurcação.")
        return False

# Função de combate entre jogador e monstro

def combate():
    print("\n⚔️ Um monstro aparece! Prepara-te para o combate!")

    vida_jogador = 30
    vida_monstro = 25

    while vida_jogador > 0 and vida_monstro > 0:
        print(f"\n❤️ Tua Vida: {vida_jogador} | 👹 Vida do Monstro: {vida_monstro}")
        print("1 - Atacar\n2 - Defender")
        acao = input("Tua ação: ")

        if acao == "1":
            dano = random.randint(5, 10)
            vida_monstro -= dano
            print(f"💥 Atingiste o monstro com {dano} de dano!")
        elif acao == "2":
            print("🛡️ Defendeste-te. Reduzes o dano do próximo ataque.")
        else:
            print("❌ Ação inválida. Perdes a vez.")
            continue

        if vida_monstro <= 0:
            break

        ataque = random.randint(4, 9)
        if acao == "2":
            ataque //= 2
            print(f"👹 O monstro ataca com dano reduzido: {ataque}!")
        else:
            print(f"👹 O monstro ataca com {ataque} de dano!")
        vida_jogador -= ataque

    if vida_jogador > 0:
        print("🏆 Venceste o monstro!")
        return True
    else:
        print("☠️ Foste derrotado... Final sombrio.")
        return False

# Enigma final após vencer o combate

def enigma_final(inventario):
    print("\n✨ Chegas a uma sala branca com um enigma na parede.")
    print("Enigma: Qual o resultado de 4 + (8 / 2) * 2")

    try:
        resposta = int(input("Tua resposta: "))
    except ValueError:
        print("❌ Resposta inválida. Final escuro.")
        return True
    
    if resposta == 12:
        if "mapa mágico" in inventario:
            print("🗺️ Usas o mapa mágico e escapas pela saída secreta. Final lendário!")
        else:
            print("✨ Acertas o enigma e consegues sair. Final bom!")
        return True
    else:
        print("☁️ Resposta errada. A sala escurece... Final escuro.")
        return True

# Executar o jogo
if __name__ == "__main__":
    inicial_jogo()
