# modular/combate.py

import random

def combate(vida_jogador):
    """
    Sistema de combate entre o jogador e o monstro.
    Retorna (venceu, nova_vida_jogador).
    """
    print("\n⚔️ Um monstro aparece! Prepara-te para o combate!")

    vida_monstro = 25

    while vida_jogador > 0 and vida_monstro > 0:
        print(f"\n❤️ Tua Vida: {vida_jogador} | 👹 Vida do Monstro: {vida_monstro}")
        print("1 - Atacar\n2 - Defender")
        acao = input("Tua ação: ")

        if acao == "1":
            dano = random.randint(5, 10)
            vida_monstro -= dano
            print(f"💥 Atingiste o monstro com {dano} de dado!")
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
            print(f"👹 O monstro ataca com {ataque} de dadno!")
        vida_jogador -= ataque

    if vida_jogador > 0:
        print("🏆 Venceste o monstro!")
        return True, vida_jogador
    else:
        print("☠️ Foste derrotado... Final sombrio.")
        return False, vida_jogador