import pygame
import os

# Inicializar pygame
pygame.init()

# Dimensões da Janela
LARGURA, ALTURA = 1000, 600

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 100, 200)
VERMELHO = (200, 50, 50)

# Criar janela
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Floresta Misteriosa")

# Fonte
fonte = pygame.font.SysFont("arial", 36)

# Imagem decorativa
CAMINHO_IMAGEM = os.path.join("assets", "arvore.png")
try:
    imagem_arvore = pygame.image.load(CAMINHO_IMAGEM)
    imagem_arvore = pygame.transform.scale(imagem_arvore, (50, 50))
except:
    imagem_arvore = None
    print("⚠️ Imagem da árvore não encontrada!")

# Função utilitária para texto
def desenhar_texto(texto, x, y, cor=PRETO, centralizar=False):
    render = fonte.render(texto, True, cor)
    if centralizar:
        x -= render.get_width() // 2
    janela.blit(render, (x, y))
    return render.get_rect(topleft=(x, y))

# Função genérica para desenhar botão
def desenhar_botao(texto, x, y, cor_fundo, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    render = fonte.render(texto, True, PRETO)
    largura = render.get_width() + 40
    altura = render.get_height() + 20

    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(janela, cor_hover, (x, y, largura, altura))
        if clique[0] == 1 and acao:
            pygame.time.delay(200)
            return acao
    else:
        pygame.draw.rect(janela, cor_fundo, (x, y, largura, altura))
    
    janela.blit(render, (x + 20, y + 10))
    return None