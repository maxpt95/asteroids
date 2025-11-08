import random

import pygame
from pygame.sprite import Group, Sprite
from pygame import Vector2
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from shapes.asteroids import Asteroid
from typing import Callable

Direction = Vector2
Position = Vector2


class AsteroidField(Sprite):
    """Asteroid field shape.

    Arguments:
        spawn_timer (float): timer to control asteroid spawning.
    """

    edges: list[list[Direction | Callable[[float], Position]]] = [
        [
            Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
    containers: tuple[Group, ...]

    def __init__(self):
        super().__init__(self.containers)  # type: ignore
        self.spawn_timer = 0.0

    def spawn(self, radius: float, position: Vector2, velocity: Vector2):
        """Spawn a new asteroid.

        Arguments:
            radius (float): distance from the center of the asteroids to its border.
            position (Vector2): position in the 2D space.
            velocity (Vector2): asteroid's speed.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, delta_time: float):
        """Update asteroid field state."""
        self.spawn_timer += delta_time
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed  # type: ignore
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))  # type: ignore
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
