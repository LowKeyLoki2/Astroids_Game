import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity if velocity else pygame.math.Vector2(0, 0)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        
        rand_angle = random.uniform(20, 50)
        pos_angle = self.velocity.rotate(rand_angle)
        neg_angle = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS 
       
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        Asteroid(self.position.x, self.position.y, new_radius, (pos_angle * 1.2))
        Asteroid(self.position.x, self.position.y, new_radius, (neg_angle * 1.2))

        self.kill()
