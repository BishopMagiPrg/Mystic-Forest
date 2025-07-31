print("🌲 Bem-vindo à Floresta Misteriosa 🌲")
print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...")
print("De repente, chegas a uma bifurcação.")

# Criamos a variável inventário - lista vazia para guardar objetos que o jogador encontra
inventario = []

print("\nEscolhes ir para:")
print("1 - Caminho da esquerda (mais escuro e silencioso)")
print("2 - Caminho da direita (claro com sons de água)")
print("3 - Caminho em frente (interior da floresta)")

escolha1 = input("Digite 1,2 ou 3 e pressione Enter: ")

if escolha1 == "1":
    print("\n🌑 Caminhas pelo trilho escuro...")
    print("O chão range e ouves passos atrás de ti.")
    print("Surge um velho guardião da floresta e oferece-te algo.")

    print("\nAceitas o objeto misterioso?")
    print("1 - Sim")
    print("2 - Não")
    escolha2 = input("Tua escolha: ")

    if escolha2 == "1":
        print("\n🎁Recebeste um mapa mágico! Ele brilha e mostra um caminho oculto.")
        # Adicionamos o mapa mágico ao inventário
        inventario.append("mapa mágico")
        print("Guardas o mapa no teu inventário.")
        print("Segues o mapa até uma caverna secreta...")
        print("Lá dentro encontras um portal para o Reino Esquecido. Final Secreto! ✨")
    else:
        print("\n🚪Recusas o objecto. O guardião desaparece.")
        print("Sem ajuda, perdes-te na escuridão. Final triste.")

elif escolha1 == "2":
    print("\n💧 Segues o som da água e chegas a um lago com uma ponte dourada.")
    print("Uma criatura aquática bloqueia a ponte e propõe um desafio.")

    print("\nAceitas o desafio de lógica?")
    print("1 - Sim")
    print("2 - Não")
    escolha2 = input("Tua escolha: ")

    if escolha2 == "1":
        print("\n❓A criatura pergunta: Qual é o número mágico entre 1 e 10?")
        numero = input("Tenta adivinhar: \n")
        if numero == "7":
            print("\n🎯Acertaste! A ponte revela o caminho para a Cidade Submersa. Final bom!")
        else:
            print("\n💥Erro! A ponte desaparece. Ficas preso à margem. Final neutro.")
    else:
        print("\n🐍 A criatura desaparece, mas a ponte também.")
        print("Sem ponte, tens de voltar... e a floresta já não é a mesma. Final sombrio.")

elif escolha1 == "3":
    print("\n🌲🌲🌲Após caminhada pela densa floresta bastante densa deparas-te por algo que brilha entre as árvores.🌲🌲🌲")
    print("🌀 É Um portal escondido, que decides fazer?")
    print("1 - Passas pelo portal.")
    print("2 - Voltas para trás.")
    portalescolha = input("Qual a tua decisão?")

    if portalescolha == "1":
        print("Ao passares pelo portal reparas que encontras-te numa sala branco pérola e com um veado à tua frente parado.")
        print("🦌O veado olha para ti e diz.")
        print("🏠Tens coragem de entrar nesta casa? (no momento aparece uma casa assombrada)")
        print("1 - Entras dentro da casa.")
        print("2 - Não entras na casa.")
        veadoescolha = input("Que vais decidir?")

        if veadoescolha == "1":
            print("Ficas espantado, o lado de dentro nada tem a haver com o lado de fora.")
            print("Uma sala redonda toda em madeira, estremamente bem cuidada.")
            print("No centro uma escadaria que leva para o patamar acima, em frente à escadaria tem uma porta.")
            print("Tem uma placa grande e um terminal, como os de multibanco:")
            print("4 + 8 / 2 * 2 (quadro mais oito a dividir por dois vezes dois)")
            try:
                escolhacalculo = int(input("Qual o resultado?"))
            except ValueError:
                print("❌ Resposta inválida. Ficaste perdido para sempre...")
            else:
                if escolhacalculo == 12:
                    print("🌞 Conseguiste escapar do labirinto.")
                    # Verifica se tens o mapa mágico para um final extra
                    if "mapa mágico" in inventario:
                        print("🗺️ Usas o mapa mágico para encontrar uma saída secreta. Final lendário!")
                    else:
                        print("Parabéns pelo final bom!")
                else:
                    print("❌ Ficaste perdido para sempre...")
        else:
            print("\nA sala branca começa a escurecer cada vez mais. quando dás por ti. Final Escuro")
    else:
        print("❓Não consegues encontrar o teu rumo, nem de onde vieste nem sabes para onde vais, perdes-te de cansaço. Final doloroso!")
else:
    print("\n❌ Escolha inválida. Fim imediato.\n")