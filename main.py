from typing import NamedTuple

import pygame
from pygame.sprite import Group
from pygame.time import Clock

from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shapes import Asteroid, Player


class SpriteGroups(NamedTuple):
    """Container for game sprite groups."""

    asteroids: Group = Group()
    drawables: Group = Group()
    updatables: Group = Group()


class Game:
    def __init__(self, groups: SpriteGroups):
        self.clock = Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.groups = groups

    def run(self):
        delta_time = 0
        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.groups.updatables.update(delta_time)

            # draw the game in the screen
            self.screen.fill("black")

            for obj in self.groups.drawables:
                obj.draw(self.screen)

            pygame.display.flip()
            delta_time = self.clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    groups = SpriteGroups()

    Player.containers = (groups.updatables, groups.drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (groups.asteroids, groups.updatables, groups.drawables)
    AsteroidField.containers = (groups.updatables,)
    asteroid_field = AsteroidField()

    game = Game(groups)
    game.run()


if __name__ == "__main__":
    main()
