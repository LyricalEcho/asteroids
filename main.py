import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    # Window/Screen display size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # FPS stuff
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Instantiate player
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Asteroid Field object
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        
        # Makes the window 'close' button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Game window display
        pygame.Surface.fill(screen, (0,0,0))

        # Update and Draw groups of player and objects on screen
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        # FPS
        # Pause game loop until 1/60th of a second has passed
        # and turn miliseconds into seconds
        dt = clock.tick(60) / 1000

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()