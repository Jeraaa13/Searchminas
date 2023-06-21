import pygame, sys

pygame.init()

pantalla = pygame.display.set_mode((500,500))

chichis = pygame.image.load("chichis.png")
chichis = pygame.transform.scale(chichis, (500,500))

pygame.display.set_caption("Fabri juego")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.blit(chichis, (0,0))

    pygame.display.flip()

pygame.exit()