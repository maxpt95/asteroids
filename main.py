import pygame
from pygame import Surface
from pygame.time import Clock
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def run_game_loop(screen: Surface, clock: Clock):
    delta_time = 0
    # game loop
    while True:
        # check for inputs
        for event in pygame.event.get():
            # update the game world
            if event.type == pygame.QUIT:
                return

        # draw the game in the screen
        screen.fill("black")
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


def main():
    pygame.init()
    clock = pygame.time.Clock()

    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode()

    run_game_loop(screen, clock)


if __name__ == "__main__":
    main()
