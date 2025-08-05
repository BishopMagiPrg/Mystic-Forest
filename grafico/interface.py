import pygame
from config import janela, BRANCO, AZUL, VERMELHO, fonte, desenhar_texto, desenhar_botao

# Cena do Menu Principal
def menu():
    janela.fill(BRANCO)
    texto_rect = desenhar_texto("Floresta Misteriosa", 400, 100, AZUL, centralizar=True)

    proxima = desenhar_botao("Começar Jogo", 300, 250, AZUL, VERMELHO, "cena_inicio")
    if not proxima:
        proxima = desenhar_botao("Sair", 300, 330, AZUL, VERMELHO, "sair")
    
    return proxima

# Cena inicial com escolhas
def cena_inicio():
    janela.fill(BRANCO)
    desenhar_texto("Estás no início de uma trilha na Floresta Misteriosa.", 100, 100, AZUL)
    desenhar_texto("Três caminhos se abrem diante de ti...", 100, 140, AZUL)

    proxima = desenhar_botao("Explorar a trilha da esquerda", 250, 240, AZUL, VERMELHO, "cena_esquerda")
    if not proxima:
        proxima = desenhar_botao("Seguir pela trilha do meio", 250, 320, AZUL, VERMELHO, "cena_meio")
    if not proxima:
        proxima = desenhar_botao("Investigar a trilha da direita", 250, 400, AZUL, VERMELHO, "cena_direita")
    return proxima

# Cena secundárias
def cena_esquerda():
    return cena_placeholder("Encontras uma clareira com luz mágica...")

def cena_meio():
    return cena_placeholder("Encontras um monstro adormecido!")

def cena_direita():
    return cena_placeholder("Há um portão misterioso com símbolos estranhos.")

# Cena genérica
def cena_placeholder(mensagem):
    janela.fill(BRANCO)
    desenhar_texto(mensagem, 100, 200, AZUL)
    return desenhar_botao("Voltar ao início", 300, 400, AZUL, VERMELHO, "cena_inicio")
