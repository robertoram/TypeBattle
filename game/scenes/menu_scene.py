import pygame
import os
from game.config import *
from game.sprites import *

class MenuScene:
    def __init__(self, screen):
        self.screen = screen
        #self.background = pygame.image.load("assets/images/menu_bg.jpg").convert()
        bg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'menu_bg.jpg')
        
        self.background = pygame.transform.scale(pygame.image.load(bg_path), (WIDTH, HEIGHT))

        self.title_font = pygame.font.Font(FONT_NAME, 64)
        self.title_text = self.title_font.render("TypeBattle", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(WIDTH/2, HEIGHT/5))

        self.start_font = pygame.font.Font(FONT_NAME, 32)
        self.start_text = self.start_font.render("Press SPACE to start/continue", True, WHITE)
        self.start_rect = self.start_text.get_rect(center=(WIDTH/2, HEIGHT/3))

        self.restart_font = pygame.font.Font(FONT_NAME, 32)
        self.restart_text = self.restart_font.render("Press R to restart", True, WHITE)
        self.restart_rect = self.restart_text.get_rect(center=(WIDTH/2, HEIGHT/2))

        self.quit_font = pygame.font.Font(FONT_NAME, 32)
        self.quit_text = self.quit_font.render("Press Q to quit", True, WHITE)
        self.quit_rect = self.quit_text.get_rect(center=(WIDTH/2, HEIGHT*2/3))

        self.done = False

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = 'game'
                    self.done = True
                if event.key == pygame.K_r:
                    self.next_scene = 'game_reset'
                    self.done = True
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    def update(self,delta_time):
       self.process_input()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_text, self.title_rect)
        self.screen.blit(self.start_text, self.start_rect)
        self.screen.blit(self.restart_text, self.restart_rect)
        self.screen.blit(self.quit_text, self.quit_rect)
