import pygame
from tkinter import simpledialog
from modules.functions import salvarDados, carregarDados, deletarDados

pygame.init()
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
branco = (255, 255, 255)
icone  = pygame.image.load("assets/icon.jpg")
pygame.display.set_icon(icone)
fonte = pygame.font.SysFont("sans serif", 20)
background = pygame.image.load("assets/background.jpg")

estrelas = {}
while True:

    tela.fill(branco)
    tela.blit(background, (0, 0))

    posicoes = list(estrelas.keys())

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvarDados(estrelas)
            quit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F10:
                salvarDados(estrelas)
            elif evento.key == pygame.K_F11:
                estrelas = carregarDados()
            elif evento.key == pygame.K_F12:
                deletarDados()
                estrelas = {}

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            nomeDaEstrela = simpledialog.askstring("Space", "Nome da Estrela: ")
            if nomeDaEstrela == None:
                continue
            estrelas[posicao] = nomeDaEstrela

    f10 = fonte.render("Pressione F10 para salvar os pontos", True, branco)
    tela.blit(f10, (10, 10))
    f11 = fonte.render("Pressione F11 para carregar os pontos", True, branco)
    tela.blit(f11, (10, 35))
    f12 = fonte.render("Pressione F12 para deletar os pontos", True, branco)
    tela.blit(f12, (10, 60))

    for coordenada, nome in estrelas.items():
        pygame.draw.circle(tela, branco, coordenada, 2, 0)
        if nome == '':
            texto = fonte.render(f"Desconhecido{coordenada}", True, branco)
        else:
            texto = fonte.render(nome, True, branco)
        tela.blit(texto, coordenada)
    
    if len(estrelas) > 1:
        for i in range(len(posicoes) - 1):
            pygame.draw.line(tela, branco, posicoes[i], posicoes[i + 1], 1)

    pygame.display.update()
    clock.tick(60)