from pygame.sprite import Group

from constants import SHOT_RADIUS
from shapes.circleshape import CircleShape


class Shot(CircleShape):
    """Shot shape.

    Arguments:
        x (float): position in the x axis.
        y (float): position in the y axis.
    """

    containers: tuple[Group, ...]

    def __init__(self, x: float, y: float):
        super().__init__(x, y, radius=SHOT_RADIUS)

    def update(self, delta_time: float):
        """Update shot state.

        Arguments:
            delta_time (float): time passed since last frame in seconds.
        """
        self.position += self.velocity * delta_time
