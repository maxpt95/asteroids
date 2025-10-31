import pygame
from pygame import Surface, Vector2

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    """Player spaceship.

    The player spaceship hitbox its a circle, but its shape will be drawn as
    a triangle.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    """

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[Vector2]:
        """Calculate the 3 vertices of the triangle representing the player."""
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen: Surface):
        """Draw player shape.

        Arguments:
            screen (Surface): surface where the player will be drawn.
        """
        triangle = self.triangle()
        pygame.draw.polygon(screen, "white", triangle, width=2)
