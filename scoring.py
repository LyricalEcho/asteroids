import pygame

class Score():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.white = (255,255,255)
        self.count = 0
        self.size = 40
        self.font = pygame.font.SysFont("Arial", self.size, True, True)
        self.text = self.font.render("Score: "+str(self.count), True, self.white)

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))

    def score_up(self):
        self.count += 10
        self.text = self.font.render("Score: "+str(self.count),True ,self.white)

