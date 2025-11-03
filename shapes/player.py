import pygame
from pygame import Surface, Vector2
from pygame.sprite import Group

from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED
from shapes.circleshape import CircleShape


class Player(CircleShape):
    """Player spaceship.

    The player spaceship hitbox its a circle, but its shape will be drawn as
    a triangle.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    """

    containers: tuple[Group, ...]

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

    def rotate(self, delta_time: float) -> None:
        """Modify player rotation.

        Arguments:
            delta_time (float): time passed since last frame in seconds.
        """
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time: float) -> None:
        """Move player forward.

        Arguments:
            delta_time (float): time past since last frame in seconds.
        """
        # unit vector rotated to same player direction
        forward = Vector2(0, 1).rotate(self.rotation)

        self.position += forward * PLAYER_SPEED * delta_time

    def update(self, delta_time: float) -> None:
        """Update player state.

        Arguments:
            delta_time (float): time passed since last frame in seconds.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)

    def draw(self, screen: Surface) -> None:
        """Draw player shape.

        Arguments:
            screen (Surface): surface where the player will be drawn.
        """
        triangle = self.triangle()
        pygame.draw.polygon(screen, "white", triangle, width=2)
