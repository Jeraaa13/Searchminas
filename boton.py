import pygame

class Boton():
    def __init__(self, imagen, pos, tamaño):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen, tamaño)
        self.rect = self.imagen.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def si_clickea(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False   
    
    def si_holdea(self, pantalla, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            pantalla.blit(self.imagen, self.rect)