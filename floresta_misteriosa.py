# Inicialização do jogo
inventario = []
jogo_ativo = True
final_alcancado = False
print("🌲Bem-vindo à Floresta Misteriosa 🌲")
print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...")

while jogo_ativo and not final_alcancado:
    print("\nChegas a uma bifurcação. Escolhes ir para:")
    print("1 - Caminho da esquerda (mais escuro e silencioso)")
    print("2 - Caminho da direita (claro com sons de água)")
    print("3 - Caminho em frente (interior da floresta)")
    print("4 - Ver inventário")
    print("0 - Sair do jogo")

    escolha1 = input("Digite 1, 2, 3, 4 ou 0: ")

    if escolha1 == "0":
        print("👋 Obrigado por jogar! Até à próxima.")
        jogo_ativo = False
    
    elif escolha1 == "4":
        print(f"\n📦 Inventário: {inventario if inventario else 'Vazio'}")

    elif escolha1 == "1":
        print("\n🌑 Caminhas pelo trilho escuro...")
        print("O chão range e ouves passos atrás de ti.")
        print("Surge um velho guardião da floresta e oferece-te algo.")

        print("\nAceitas o objeto misterioso?")
        print("1 - Sim")
        print("2 - Não")
        escolha2 = input("Tua escolha: ")

        if escolha2 == "1":
            if "mapa mágico" not in inventario:
                print("\n🎁 Recebeste um mapa mágico! Ele brilha e mostra um caminho oculto.")
                inventario.append("mapa mágico")
            else:
                print("🗺️ Já tens o mapa mágico.")
        else:
            print("\n🚪 Recusas o objeto. O guardião desaparece.")
    
    elif escolha1 == "2":
        print("\n💧 Segues o som da água e chegas a um lago com uma ponte dourada.")
        print("Uma criatura aquática bloqueia a ponte e propõe um desafio de lógica.")

        print("\nAceitas o desafio?")
        print("1 - Sim")
        print("2 - Não")
        escolha2 = input("Tua escolha: ")

        if escolha2 == "1":
            print("\n❓ A criatura pergunta: Qual é o número mágico entre 1 e 10?")
            numero = input("Tenta adivinhar: ")
            if numero == "7":
                print("\n🎯 Acertaste! A ponte revela o caminho para a Cidade Submersa.")
                print("🏁 Final bom!")
                final_alcancado = True
            else:
                print("\n💥 Erro! A ponte desaparece. Ficas preso à margem. Final neutro.")
                final_alcancado = True

    elif escolha1 == "3":
        print("\n🌲🌲🌲Caminhas fundo na floresta e vês algo a brilhar entre as árvores.")
        print("🌀 É um portal escondido. Que decides fazer?")
        print("1 - Passas pelo portal")
        print("2 - Voltas para trás")
        portalescolha = input("Decisão: ")

        if portalescolha == "1":
            print("\n🌟 Atravessas o portal e estás numa sala branca com um veado místico.")
            print("🦌 O veado pergunta se tens coragem de entrar numa casa assombrada.")
            print("1 - Entras na casa")
            print("2 - Não entras")
            veadoescolha = input("Tua escolha: ")

            if veadoescolha == "1":
                print("\n🏚️ A casa por dentro é de madeira e tem uma escadaria.")
                print("Há uma porta com um terminal e um enigma:")
                print("🧠 Enigma: 4 + 8 / 2 * 2")

                try:
                    resposta = int(input("Qual o resultado? "))
                except ValueError:
                    print("❌ Resposta inválida. Ficaste perdido para sempre...")
                    final_alcancado = True
                else:
                    if resposta == 12:
                        print("🌞 Conseguiste escapar do laboratorio.")
                        if "mapa mágico" in inventario:
                            print("🗺️ Usas o mapa mágico para encontrar a saída secreta. Final lendário!")
                        else:
                            print("Final bom.")
                        final_alcancado = True
                    else:
                        print("❌ Resposta errada. Final sombrio.")
                        final_alcancado = True
            else:
                print("🌑 A sala escurece e desapareces no vazio. Final escuro.")
                final_alcancado = True
        else:
            print("🔄 Voltas à bifurcação.")

    else:
        print("❌ Escolha inválida. Tenta novamente.")

