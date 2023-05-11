import pygame
import random
from game.config import *
from game.sprites.word_projectile import WordProjectile


class Word(pygame.sprite.Sprite):
    def __init__(self, word_data):
        super().__init__()
        self.id = word_data["id"]
        self.text = word_data["text"]
        self.x = word_data["x"]
        self.y = word_data["y"]
        self.speed = word_data["speed"] if "speed" in word_data else LETTER_SPEED
        self.attacked = word_data["attacked"] if "attacked" in word_data else 0
        self.font = pygame.font.Font(FONT_NAME, 30)
        self.image = self.font.render(self.text, True, WHITE)
        self.rect = self.image.get_rect() #center=(self.x, self.y)
        self.x = random.randint(10+(self.rect.width / 2), WIDTH -  (self.rect.width / 2) - 10)#- (self.rect.width / 2) 
       
        self.projectile = None
        

    def update(self, delta_time):
        self.y += self.speed * delta_time
        self.rect.center = (self.x, self.y)

        if self.attacked and not self.projectile:
            self.projectile = WordProjectile((WIDTH / 2, HEIGHT - 100))
            target_x = self.rect.centerx
            target_y = self.rect.centery
            speed = 500 # Pixels per second
            distance = ((target_x - self.projectile.rect.centerx) ** 2 + (target_y - self.projectile.rect.centery) ** 2) ** 0.5
            time = distance / speed
            self.projectile.speed_x = (target_x - self.projectile.rect.centerx) / time
            self.projectile.speed_y = (target_y - self.projectile.rect.centery) / time

        if self.projectile:
            self.projectile.update(delta_time)
            if self.projectile.off_screen:
                self.projectile = None
        
       
       
        
       
    def attack(self):
        self.attacked = 1
        self.image = self.font.render(self.text, True, (255, 0, 0))

    def render_word(self):
            self.text = self.font.render(self.word, True, WHITE)
            self.image.blit(self.text, (0, 0))
