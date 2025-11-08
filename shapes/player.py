import pygame
from pygame import Surface, Vector2
from pygame.sprite import Group

from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)
from shapes.circleshape import CircleShape
from shapes.shot import Shot


class Player(CircleShape):
    """Player spaceship.

    The player spaceship hitbox its a circle, but its shape will be drawn as
    a triangle.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    Attributes:
        position (Vector2): position in the 2D space.
        velocity (Vector2): velocity vector.
        radius (float): distance between the center of the player hitbox (circle) to its border.
        rotation (float): rotation angle.
    """

    containers: tuple[Group, ...]

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

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

    def shoot(self) -> None:
        """Shoot from the player position."""
        if self.shoot_cooldown > 0:
            return

        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        position: Vector2 = self.position
        shot = Shot(position.x, position.y)
        shot.velocity = Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED

    def update(self, delta_time: float) -> None:
        """Update player state.

        Arguments:
            delta_time (float): time passed since last frame in seconds.
        """
        self.shoot_cooldown -= delta_time

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self, screen: Surface) -> None:
        """Draw player shape.

        Arguments:
            screen (Surface): surface where the player will be drawn.
        """
        triangle = self.triangle()
        pygame.draw.polygon(screen, "white", triangle, width=2)
