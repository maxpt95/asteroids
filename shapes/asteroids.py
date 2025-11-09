import random

from pygame import Vector2
from pygame.sprite import Group

from constants import ASTEROID_MIN_RADIUS
from logger import log_event
from shapes.circleshape import CircleShape


class Asteroid(CircleShape):
    """Asteroid shape.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    Attributes:
        position (Vector2): position in the 2D space.
        velocity (Vector2): velocity vector.
        radius (float): distance between the center of the player hitbox (circle) to its border.
    """

    containers: tuple[Group, ...]

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def update(self, delta_time: float):
        """Update asteroid state.

        Arguments:
            delta_time (float): time passed since last frame in seconds.
        """
        self.position += self.velocity * delta_time

    def split(self) -> None:
        """Split asteroid into two smaller asteroids."""
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        fragments_radius = self.radius - ASTEROID_MIN_RADIUS

        position: Vector2 = self.position
        fragments_parameters = (position.x, position.y, fragments_radius)
        fragment_1, fragment_2 = (
            Asteroid(*fragments_parameters),
            Asteroid(*fragments_parameters),
        )

        # Fragments velocities, each one with an angle oposite to the other
        fragment_angle = random.uniform(20, 50)
        fragment_1_velocity = self.velocity.rotate(fragment_angle)
        fragment_2_velocity = self.velocity.rotate(-fragment_angle)
        fragment_1.velocity = fragment_1_velocity
        fragment_2.velocity = fragment_2_velocity
