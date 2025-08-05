import pygame
import sys
from config import janela
import interface
import combate # Novo ficheiro

# Dicionário de cenas
cenas = {
    "menu": interface.menu,
    "cena_inicio": interface.cena_inicio,
    "cena_esquerda": interface.cena_esquerda,
    "cena_meio": interface.cena_meio,
    "cena_direita": interface.cena_direita,
    "cena_combate": combate.cena_combate # nova entrada
}

def main():
    cena_atual = "menu"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Executa a função da cena atual
        if cena_atual == "sair":
            pygame.quit()
            sys.exit()

        proxima = cenas[cena_atual]() # Desenha a cena

        if proxima:
            cena_atual = proxima
        
        pygame.display.update()

if __name__ == "__main__":
    main()
