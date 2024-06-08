import pygame
from tkinter import simpledialog

pygame.init()
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
branco = (255, 255, 255)
fonte = pygame.font.SysFont("arial", 20)

# IMAGENS
background = pygame.image.load("assets/background.jpg")

estrelas = {}

while True:

    # FUNDO
    tela.fill(branco)
    tela.blit(background, (0, 0))

    posicoes = list(estrelas.keys())

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            nomeDaEstrela = simpledialog.askstring("Space", "Nome da Estrela: ")
            if nomeDaEstrela == '':
                 nomeDaEstrela = "Desconhecido"
            estrelas[posicao] = nomeDaEstrela
            print(estrelas)

    # MARCAÇÕES
    for coordenada, nome in estrelas.items():
            pygame.draw.circle(tela, branco, coordenada, 2, 0)
            texto = fonte.render(nome, True, branco)
            tela.blit(texto, coordenada)

    # LINHAS
    if len(estrelas) > 1:
        for i in range(len(posicoes) - 1):
            pygame.draw.line(tela, branco, posicoes[i], posicoes[i + 1], 1)
        

    pygame.display.update()
    clock.tick(60)