import pygame
from pygame import Surface
from pygame.time import Clock

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


class Game:
    def __init__(self, player: Player):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = player

    def run(self):
        delta_time = 0
        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.player.update(delta_time)

            # draw the game in the screen
            self.screen.fill("black")
            self.player.draw(self.screen)
            pygame.display.flip()
            delta_time = self.clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = Game(player)
    asteroids.run()


if __name__ == "__main__":
    main()
