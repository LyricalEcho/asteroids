import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoring import Score


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Score(50, 50)

    dt = 0

    game_paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = not game_paused

        if not game_paused:

            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    print("Game over!")
                    print("Final Score:", score.count)
                    
                    sys.exit()
                for shot in shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        score.score_up()


            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)
            
            score.draw(screen)
        
        else:
            # Display pause screen
            font = pygame.font.Font(None, 36)
            text = font.render("Paused", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
