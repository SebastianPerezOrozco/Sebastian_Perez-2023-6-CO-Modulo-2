import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET

class Bullet(Sprite):

    SPEED = 20

    def __init__(self, spaceship):

     self.imagen = pygame.transform.scale(BULLET,(9, 32))
     self.rect = self.imagen.get_rect()
     self.rect.center = spaceship.rect.center

    def update (self, bullet):
        self.rect.y -= self.SPEED
        if self.rect.y <= 0:
           bullet.remove(self)

    def draw(self, screen):
       screen.blit(self.imagen, (self.rect.x, self.rect.y))