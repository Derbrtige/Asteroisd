import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            # generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20, 50)

            # create two velocity vectors rotated in opposite directions
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)

            # compute new smaller radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # create two new asteroids at the same position
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)

            # set their velocities and scale them up slightly
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2

            return [a1, a2]