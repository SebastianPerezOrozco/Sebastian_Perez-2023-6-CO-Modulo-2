import random
from typing import Any
import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT, RIGHT = 'left', 'right'

class Enemy(Sprite):

    X_POS_LIST = [20, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1070]
    MOVEMENTS = [LEFT, RIGHT]

    def __init__(self, enemy):

        self.image = pygame.transform.scale(enemy , (58, 53))
        self.rect = self.image.get_rect()
        self.enemy = enemy # Una forma de instancear indirectamente.
        # Posición de inicio
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = -5

        # Factor de Movimiento
        self.movement = random.choice(self.MOVEMENTS)
        self.mov_x = 5
        self.mov_y = 1

        self.amplitude = 1  # Amplitud del movimiento
        self.frequency = 50

        if self.enemy == ENEMY_1:
            self.name = "dv1"
        else:
            self.name = "dv2"

        #Vamos agregar un label para cada nave.
        self.font = pygame.font.Font(FONT_STYLE, 10) # Establecemos el tamaño y el tipo de fuente a emplear
        self.label = self.font.render(f"Enemy: {self.name}", True, (255, 255, 255))
        self.label_rect = self.label.get_rect()
        self.label_rect.center = (self.rect.x, self.rect.y) 

    def update(self, ship): #Llamamos ship para crear un camino para eliminar enemy de la lista de EnemyManager
        
        if self.movement == LEFT:
            self.rect.x -= self.mov_x
            self.rect.y += self.mov_y
        else:
            self.rect.x += self.mov_x
            self.rect.y += self.mov_y

        self.update_movement()

        if self.rect.y >= SCREEN_HEIGHT:
            ship.remove(self)

    def update_movement(self):
        if self.rect.x > SCREEN_WIDTH -60:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.label, (self.rect.x , self.rect.y - 10))