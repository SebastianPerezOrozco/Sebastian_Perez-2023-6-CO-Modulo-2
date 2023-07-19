import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET

class Bullet(Sprite):

    SPEED = 20

    def __init__(self, spaceship):

     self.imagen = pygame.transform.scale(BULLET,(9, 32))
     self.rect = self.imagen.get_rect()
     self.rect.center = spaceship.rect.center

    def update (self):
        self.rect.y -= self.SPEED

    def draw(self, screen):
       screen.blit(self.imagen, (self.rect.x, self.rect.y))