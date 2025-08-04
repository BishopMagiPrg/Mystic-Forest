import random

# Inicialização
inventario = []
jogo_ativo = True
jogo_alcancado = False

print("🌲 Bem-vindo à Floresta Misteriosa 🌲")
print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...")

def combate():
    print("\n⚔️ Um monstro aparece! Prepara-te para o combate!")

    vida_jogador = 30
    vida_monstro = 25

    while vida_jogador > 0 and vida_monstro > 0:
        print(f"\n❤️ Tua Vida: {vida_jogador} | 👹 Vida do Monstro: {vida_monstro}")
        print("Escolhe tua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        acao = input("Tua escolha: ")

        if acao == "1":
            dano = random.randint(5, 10)
            vida_monstro -= dano
            print(f"\n💥 Atingiste o monstro com {dano} de dano!")
        elif acao == "2":
            print("\n🛡️ Defendeste-te. Reduzes o dano do próximo ataque.")
        else:
            print("❌ Escolha inválida. Perdes a tua vez.")
            continue

        if vida_monstro <= 0:
            break

        ataque_monstro = random.randint(4, 9)
        if acao == "2":
            ataque_monstro = ataque_monstro // 2
            print(f"👹 O monstro ataca, mas sofre redução! Levas {ataque_monstro} de dano.")
        else:
            print(f"👹 O monstro ataca e acerta-te com {ataque_monstro} de dano.")

        vida_jogador -= ataque_monstro

    if vida_jogador > 0:
        print("\n🏆 Venceste o monstro! És um verdadeiro herói!")
        return True # Venceu
    else:
        print("\n☠️ Foste derrotado... Final sombrio.")
        return False # Perdeu
    
# Loop principal
while jogo_ativo and not jogo_alcancado:
    print("\nChegas a uma bifurcação. Escolhes ir para:")
    print("1 - Caminho da esquerda (mais escuro e silencioso)")
    print("2 - Caminho da direita (claro com sons de água)")
    print("3 - Caminho em frente (interior da floresta)")
    print("4 - Ver inventário")
    print("0 - Sair do jogo")

    escolha1 = input ("Digite 1, 2, 3, 4 ou 0: ")

    if escolha1 == "0":
        print("👋 Obrigado por jogar! Até à próxima.")
        jogo_ativo = False

    elif escolha1 == "4":
        print(f"\n📦 Inventário: {inventario if inventario else 'Vazio'}")

    elif escolha1 == "1":
        print("\n🌑 Caminhas pelo trilho escuro...")
        print("Surge um velho guardião da floresta e oferece-te algo.")

        print("\nAceitas o objeto misterioso?")
        print("1 - Sim")
        print("2 - Não")
        escolha2 = input("Tua escolha: ")

        if escolha2 == "1":
            if "mapa mágico" not in inventario:
                print("\n🎁 Recebeste um mapa mágico!")
                inventario.append("mapa mágico")
            else:
                print("🗺️ Já tens o mapa mágico.")
        else:
            print("\n🚪 Recusas o objecto. O guardião desaparece.")

    elif escolha1 == "2":
        print("\n💧 Chegas a um lago com uma ponte dourada.")
        print("Uma criatura aquática propõe um desafio de lógica.")

        print("\nAceitas o desafio?")
        print("1 - Sim")
        print("2 - Não")
        escolha2 = input("Tua escolha: ")

        if escolha2 == "1":
            print("\n❓Qual é o número mágico entre 1 e 10?")
            numero = input("Tenta adivinhar: ")
            if numero == "7":
                print("\n🎯 Acertaste! A ponte leva-te à Cidade Submersa.")
                print("🏁 Final bom!")
                final_alcancado = True
            else:
                print("\n💥 Erro! A ponte desaparece. Final neutro.")
                final_alcancado = True
        else:
            print("\n🐍 A criatura desaparece. Final sombrio.")
            final_alcancado = True

    elif escolha1 == "3":
        print("\n🌲 Avanças fundo na floresta... Encontras um portal místico.")
        print("1 - Entras no portal")
        print("2 - Voltas atrás")
        porta = input("decisão: ")

        if porta == "1":
            venceu = combate()
            if venceu:
                print("\n🌟 Depois da batalha, chegas a uma sala branca com uma porta enigmática.")
                print("🧠 Enigma na parede: 4 + (8 / 2) * 2")
                try:
                    resposta = int(input("Qual o resultado? "))
                except ValueError:
                    print("❌ Resposta inválida. Final sombrio.")
                    final_alcancado = True
                else:
                    if resposta == 12:
                        if "mapa mágico" in inventario:
                            print("🗺️ Usas o mapa mágico para escapar pelo caminho secreto. Final lendário!")
                        else:
                            print("✨ Consegues sair com esforço. Final bom!")
                        final_alcancado = True
                    else:
                        print("❌ Resposta errada. A sala escurece. Final escuro.")
                        final_alcancado = True
            else:
                final_alcancado = True
        else:
            print("🔄 Voltas à bifurcação.")
    else:
        print("❌ Escolha inválida. Tenta novamente.")
