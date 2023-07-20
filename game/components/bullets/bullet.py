import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET

class Bullet(Sprite):

    SPEED = 20

    def __init__(self, spaceship , ship_type):

        self.imagen = pygame.transform.scale(BULLET,(9, 32))
        self.rect = self.imagen.get_rect()
        self.rect.center = spaceship.rect.center
        self.ship_type = ship_type

    def update (self):
        if self.ship_type == "player":
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED

    def draw(self, screen):
       screen.blit(self.imagen, (self.rect.x, self.rect.y))