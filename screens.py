import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Screens():
    def __init__(self):
        pass

    def pause(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render("Paused", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)