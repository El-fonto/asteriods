import pygame, sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")

    # static groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)

    # Object creation
    field = AsteroidField()
    player = Player (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()


    while True:
        # quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # paint screen
        screen.fill("black")

        # object iterations
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                sys.exit("Game over!")

        for draw in drawable:
            draw.draw(screen)


        # display_updater
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
