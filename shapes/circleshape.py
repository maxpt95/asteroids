from __future__ import annotations

import pygame
from pygame import Surface, Vector2
from pygame.sprite import Sprite


class CircleShape(Sprite):
    """A base class for circular game objects.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    Attributes:
        position (Vector2): position in the 2D space.
        velocity (Vector2): velocity vector.
        radius (float): distance between the center of the circle to its border.
    """

    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # type: ignore
        else:
            super().__init__()

        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: Surface):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width=2,
        )

    def update(self, delta_time: float):
        # sub-classes must override
        pass

    def collides_with(self, other: CircleShape):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
