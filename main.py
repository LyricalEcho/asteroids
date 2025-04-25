import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        
        # Makes the window 'close' button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Game window display
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()