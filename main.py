from typing import NamedTuple

import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.time import Clock

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shapes import Player


class SpriteGroups(NamedTuple):
    """Container for game sprite groups."""

    updatables: Group = Group()
    drawables: Group = Group()


class Game:
    def __init__(self, groups: SpriteGroups):
        self.clock = pygame.time.Clock()
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

    asteroids = Game(groups)
    asteroids.run()


if __name__ == "__main__":
    main()
