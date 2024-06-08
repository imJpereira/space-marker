import pygame
pygame.init()
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
branco = (255, 255, 255)

## IMAGENS
background = pygame.image.load("assets/background.jpg")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco)
    tela.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)