from shapes.circleshape import CircleShape
from pygame.sprite import Group


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
