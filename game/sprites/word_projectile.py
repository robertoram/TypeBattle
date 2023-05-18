import pygame
from game.config import *

class WordProjectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=position)
        self.speed = PROJECTILE_SPEED
        self.off_screen = False

    def update(self, delta_time):
        self.rect.y -= self.speed * delta_time
        if self.rect.y <= 0:
            self.off_screen = True  # Si el proyectil está fuera de la pantalla, seteamos off_screen en True

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)
    
