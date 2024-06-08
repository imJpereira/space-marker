import pygame
from tkinter import simpledialog

pygame.init()
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
branco = (255, 255, 255)

# IMAGENS
background = pygame.image.load("assets/background.jpg")

marcacoes = []

while True:

    # FUNDO
    tela.fill(branco)
    tela.blit(background, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            marcacoes.append(posicao)

    for marcacao in marcacoes:
            pygame.draw.circle(tela, branco, marcacao, 2, 0)

    if len(marcacoes) > 1:
        for i in range(len(marcacoes) - 1):
            pygame.draw.line(tela, branco, marcacoes[i], marcacoes[i + 1], 1)
        

    pygame.display.update()
    clock.tick(60)