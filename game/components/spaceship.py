import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_WIDTH, SPACESHIP, SCREEN_HEIGHT

class Spaceship(Sprite):

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (58, 53)) # Tome las dimenciones de la image que eran 577X529 y las dividí por 10 y las aproximé.
        self.rect = self.image.get_rect() # Con este metodo vamos hacer que la imagen de Space se convierta en un rectangulo.

        # Tanto en x como en y asignamos un valor teniendo en cuenta el tamaño del Screen. Esta será la posición inicial del Spaceship
        self.rect.x = SCREEN_WIDTH//2
        self.rect.y = 500
    
# Vamos a definir los metodos de movimientos en la pantalla. Vamos a generar una limitacion en la coordenada.
    
    def move_left(self):
        self.rect.x -= 9 # Será el movimiento que se le restará a la nave cuando se ejecute la acción.
        if self.rect.right < 0: # Esta es la condición cuando la nave se salga de los limites de Screen
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        self.rect.x += 9 # Será el movimiento que se le sumará a la nave cuando se ejecute la acción.
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0 
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT//2:#Este será el limite maximo en el que la nave podrá subir.
            self.rect.y -= 9
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT-60: # Le ponemos el menos 50 dado a que si lo dejamos solo no se vería la nave
            self.rect.y += 9
    
    def update (self, user_input):
        #El user_input será una variable en la clase game la cual almacenará la funcion para determinar cual tecla ha sido presionada.
        #Vamos a emplear varias opciones para el movimiento, tanto las flechas como las letras que comúnmente se emplean en los videojuegos.
        #Empleamos en todos los casos con if para que podamos hacer movimientos combinados en el eje "y" y "x"

        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()

        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
    
    def draw(self, screen):
        #Vamos a dibujar a Spaceship en las coordenadas previamente asiganadas en nuestro metodo constructor
        screen.blit(self.image, (self.rect.x, self.rect.y))
