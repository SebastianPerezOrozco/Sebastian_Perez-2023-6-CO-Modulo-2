import random
import pygame
from game.components.enemies.enemy import Enemy
from game.components.final_menu import FinalMenu
from game.components.spaceship import Spaceship

# game.utils.constants -> es un modulo donde tengo "objetos" en memoria como el BG (background)...etc
#   tambien tenemos valores constantes como el title, etc
from game.utils.constants import BG, ENEMY_1, ENEMY_2, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE

# Game es la definicion de la clase (plantilla o molde para sacar objetos)
# self es una referencia que indica que el metodo o el atributo es de cada "objeto" de la clase Game
class Game:

    ENEMIES = [ENEMY_1, ENEMY_2]

    def __init__(self):
        pygame.init() # este es el enlace con la libreria pygame para poder mostrar la pantalla del juego
        pygame.display.set_caption(TITLE) # Sele pone el titulo del juego en la ventana
        pygame.display.set_icon(ICON)# se le pone el icono de la nave en la descripción de la ventana del juego
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        
    #Vamos a instancear Spaceship para poder traerla a la Clase Game()
        self.player = Spaceship("xwing")

        self.final_menu = FinalMenu()
    #Enemy
        self.enemies = []
        self.num_enemies = 2

    # este es el "game loop"
    # Game loop: events - update - draw
    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
            self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # esta expression es la llamada a un metodo pygame.event.get() que devuelve un "iterable"
        for event in pygame.event.get(): # con el for sacamos cada evento del "iterable"
            if event.type == pygame.QUIT : # pygame.QUIT representa la X de la ventana
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False

    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los updates de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "update" method que llamamos desde aqui
    def update(self):
        #Primero definimos la variable de user_input la cual nos almacenará la funcion para identificar las teclas que se presionan.
        user_input = pygame.key.get_pressed()
        #Vamos a llamar a la clase Spaceship y que active la calse de update.
        self.player.update(user_input, self)
        
        #Enemy
        for enemy in self.enemies:
            enemy.update()

            if enemy.rect.y >= SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            
            if self.player.rect.colliderect(enemy.rect):
                self.player.reset()
                self.enemies.remove(enemy)


        if len(self.enemies) < self.num_enemies:
            enemy_name = f"Enemy: {len(self.enemies) + 1}"
            new_enemy = Enemy(enemy_name, random.choice(self.ENEMIES))
            self.enemies.append(new_enemy)
            
    # este metodo "dibuja o renderiza o refresca mis cambios en la pantalla del juego"
    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los metodos "draw" de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "draw" method que llamamos desde aqui
    def draw(self):
        self.clock.tick(FPS) # configuramos cuantos frames dibujaremos por segundo
        self.screen.fill((255, 255, 255)) # esta tupla (255, 255, 255) representa un codigo de color: blanco
        self.draw_background()
        #Ahora haremos lo mismo con el metodo update pero ahora con el metodo draw de Spaceship
        self.player.draw(self.screen)
        #Enemy
        for enemy in self.enemies:
            enemy.draw(self.screen)      

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):

        # le indicamos a pygame que transforme el objeto BG (que es una imagen en memoria, no es un archivo)
        # y le pedimos que ajuste el ancho y alto de esa imagen
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # obtenemos el alto de la imagen
        image_height = image.get_height()

        ## DIBUJAMOS dos veces para dar la impresion de que nos movemos en el spacio
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))

        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        # Controlamos que en el eje Y (vertical) si me sali del screen height (alto de pantalla)
        if self.y_pos_bg >= SCREEN_HEIGHT:
            # dibujo la imagen
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            # reseteo la posicion en y
            self.y_pos_bg = 0
        # No hay una velocidad de juego como tal, el "game_speed" simplemente me indica
        # cuanto me voy a mover (cuantos pixeles hacia arriba o abajo) cen el eje Y
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        if self.player.deaths_count == 1:
            pygame.time.delay(1000)
            self.final_menu.update(self.player)
            self.final_menu.draw(self.screen)
            self.final_menu.event(self.on_close, self.run)
            #self.reset()

    def on_close(self):
        self.playing = False
