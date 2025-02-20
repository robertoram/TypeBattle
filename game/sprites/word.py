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
        self.font = pygame.font.Font(FONT_NAME, 15)
        self.image = self.font.render(self.text, True, WHITE)
        self.rect = self.image.get_rect()  # center=(self.x, self.y)
        self.x = random.randint(10 + int(self.rect.width / 2), WIDTH - int(self.rect.width / 2) - 10)

        # Inicialización del proyectil
        self.projectile = None
        self.projectile_sprites = pygame.sprite.Group()

    def update(self, delta_time):
        # Actualiza la posición de la palabra (cae hacia abajo)
        self.y += self.speed * delta_time
        self.rect.center = (self.x, self.y)

        # Si la palabra ha sido atacada y no tiene proyectiles activos, crea uno
        if self.attacked and len(self.projectile_sprites) == 0:
            # Crear un proyectil desde la parte inferior de la pantalla hacia la palabra
            self.projectile = WordProjectile((WIDTH / 2, HEIGHT - 100))
            target_x = self.rect.centerx
            target_y = self.rect.centery
            speed = 100  # Pixels por segundo
            distance = ((target_x - self.projectile.rect.centerx) ** 2 + (target_y - self.projectile.rect.centery) ** 2) ** 0.5
            time = distance / speed
            self.projectile.speed_x = (target_x - self.projectile.rect.centerx) / time
            self.projectile.speed_y = (target_y - self.projectile.rect.centery) / time

            # Añadir el proyectil al grupo
            self.projectile_sprites.add(self.projectile)

        # Actualizar los proyectiles
        for projectile in self.projectile_sprites:
            projectile.update(delta_time)
            #if projectile.off_screen:
            #    self.projectile_sprites.remove(projectile)
            #    self.projectile = None

    def attack(self):
        # Cuando la palabra es atacada, cambia su color a verde
        self.attacked = 1
        self.font = pygame.font.Font(FONT_NAME, 15)
        self.image = self.font.render(self.text, True, GREEN)
