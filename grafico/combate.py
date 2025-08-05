import pygame
from config import janela, BRANCO, AZUL, VERMELHO, desenhar_texto, desenhar_botao

mensagem = "" # Mensagem global para feedback do combate

def cena_combate():
    global mensagem

    janela.fill(BRANCO)

    desenhar_texto("Um Lobo Sombrio aparece!", 200, 100, AZUL)
    desenhar_texto("O que queres fazer?", 200, 150, AZUL)

    proxima = desenhar_botao("Atacar", 300, 250, AZUL, VERMELHO, "atacar")
    if not proxima:
        proxima = desenhar_botao("Fugir", 300, 330, AZUL, VERMELHO, "fugir")

    # Mensagem de feedback
    if proxima == "atacar":
        mensagem = "Acertaste o inimigo! Mas ele ainda está de pé..."
        proxima = None # Mantém-se nesta cena

    elif proxima == "fugir":
        mensagem = ""
        return "cena_inicio" # Volta à floresta
    
    return None