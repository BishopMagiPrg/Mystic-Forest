def enigma_final(inventario, vida_jogador):
    """
    Mostra um enigma ao jogador.
    Se acertar, verifica se tem o mapa mágico.
    Retorna (final_alcancado, jogo_ativo, vida_jogador)
    """
    print("\n✨ Chegas a uma sala branca com um enigma na parede.")
    print("Enigma: Qual o resultado de 4 + 8 (8 / 2) * 2 ?")

    try:
        resposta = int(input("Tua resposta: "))
    except ValueError:
        print("❌ Resposta inválida. Final escuro.")
        return True, True, vida_jogador
    
    if resposta == 12:
        if "mapa mágico" in inventario:
            print("🗺️ Usas o mapa mágico e escapas pela saída secreta. Final lendário!")
        else:
            print("✨ Acertas o enigma e consegues sair. Final bom!")
        return True, True, vida_jogador
    else:
        print("☁️ Resposta errada. A sala escurece... Final escuro.")
        return True, True, vida_jogador