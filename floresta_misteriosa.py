print("🌲 Bem-vindo à Floresta Misteriosa 🌲")
print("Tu és um explorador corajoso que entra numa floresta cheia de segredos...")
print("De repente, chegas a uma bifurcação.")

print("\nEscolhes ir para:")
print("1 - Caminho da esquerda (mais escuro e silencioso)")
print("2 - Caminho da direita (claro com sons de água)")

escolha = input("Digite 1 ou 2 e pressione Enter: ")

if escolha == "1":
    print("\n🌑 Caminhas pelo trilho escuro...")
    print("O chão range e ouves passos atrás de ti. Algo se aproxima.")
    print("É um velho guardião da floresta que te entrega um mapa mágico!")
    print("Parabéns, encontraste um segredo antigo.")
elif escolha == "2":
    print("\n💧 Segues o som da água...")
    print("Encontras um lago cristalino e uma ponte dourada.")
    print("Mas ao atravessar a ponte... ela desaparece atrás de ti.")
    print("Estás preso... num novo mundo misteriorso!")
else:
    print("\n❌ Não entendi a tua escolha. O jogo termina aqui. Tenta novamente!")