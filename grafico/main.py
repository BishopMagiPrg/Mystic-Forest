import pygame
import sys
import os

# Inicializar pygame
pygame.init()

# Caminho da imagem da árvore
CAMINHO_IMAGEM = os.path.join("assets", "arvore.png")

# Constantes
LARGURA, ALTURA = 800, 600
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 100, 200)
VERMELHO = (200, 50, 50)

# Janela
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Floresta Misteriosa")

# Fonte
fonte = pygame.font.SysFont("arial", 36)

# Carregar imagem da árvore
try:
    imagem_arvore = pygame.image.load(CAMINHO_IMAGEM)
    imagem_arvore = pygame.transform.scale(imagem_arvore, (50, 50))
except:
    imagem_arvore = None
    print("⚠️ Imagem da árvore não encontrada!")

# Função para desenhar texto
def desenhar_texto(texto, x, y, cor=PRETO, centralizar=False):
    render = fonte.render(texto, True, cor)
    if centralizar:
        x -= render.get_width() // 2
    janela.blit(render, (x, y))
    return render.get_rect(topleft=(x, y))

# Função para criar botão adaptável ao texto
def desenhar_botao(texto, x, y, cor_fundo, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    render = fonte.render(texto, True, PRETO)
    largura = render.get_width() + 40
    altura = render.get_height() + 20

    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(janela, cor_hover, (x, y, largura, altura))
        if clique[0] == 1 and acao:
            acao()
    
    else:
        pygame.draw.rect(janela, cor_fundo, (x, y, largura, altura))
    
    janela.blit(render, (x + 20, y + 10))

# Ações dos botões
def iniciar_jogo():
    print("➡️ Jogo iniciado! (a lógica virá para aqui depois)")

def sair_jogo():
    pygame.quit()
    sys.exit()

# Loop principal
def menu_principal():
    while True:
        janela.fill(BRANCO)

        # Título centralizado
        texto_rect = desenhar_texto("Floresta Misteriosa", LARGURA // 2, 100, AZUL, centralizar=True)

        # Árvores decorativa ao lado do título
        if imagem_arvore:
            janela.blit(imagem_arvore, (texto_rect.left - 60, 100))
            janela.blit(imagem_arvore, (texto_rect.right + 10, 100))
        
        # Botões centralizados
        desenhar_botao("Começar Jogo", LARGURA // 2 - 100, 250, AZUL, VERMELHO, iniciar_jogo)
        desenhar_botao("Sair", LARGURA // 2 - 100, 330, AZUL, VERMELHO, sair_jogo)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair_jogo()

        pygame.display.update()

if __name__ == "__main__":
    menu_principal()
