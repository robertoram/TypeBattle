import pygame
from game.config import *

class WordProjectile(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=position)
        self.speed_x = 0
        self.speed_y = 0
        self.off_screen = False

    def update(self, delta_time):
        self.rect.x += self.speed_x * delta_time
        self.rect.y += self.speed_y * delta_time
        if self.rect.y < 0 or self.rect.y > HEIGHT or self.rect.x < 0 or self.rect.x > WIDTH:
            self.off_screen = True
