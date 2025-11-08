import sys


import pygame

from pygame.time import Clock

from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shapes import Asteroid, Player, Shot
from logger import log_state


def main():
    pygame.init()
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    clock = Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta_time = 0
    # game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(delta_time)

        for ast in asteroids:
            if ast.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
