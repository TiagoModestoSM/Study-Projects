import pygame, sys, os, random
from PIL import Image

# Inicia o pygame
pygame.init()

# Ajustando FPS
clock = pygame.time.Clock()

# Resolução da tela do jogo
Largura = 480
Altura = 480

# Criação da tela
tela_principal = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('MAIN MENU')

# Tela de Fundo
tela_paisagem = pygame.image.load('C:/Users/labig/OneDrive/Documentos/GitHub/Study_Projects/Game/Assets/Images/teste_tiles.jpeg')
tela_paisagem = pygame.transform.scale(tela_paisagem,(Largura,Altura))
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche a tela de branco
    tela_principal.fill('white')
    tela_principal.blit(tela_paisagem, (0,0))
    # Atualiza a tela
    pygame.display.update()

    # Controla o FPS
    clock.tick(144)

pygame.quit()
sys.exit()
