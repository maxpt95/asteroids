import pygame


class CircleShape(pygame.sprite.Sprite):
    """A base class for circular game objects.

    Attributes:
        - x (float): position in the x axis.
        - y (float): position in the y axis.
        - radius (float): distance between the center of the circle to its border.
    """

    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
