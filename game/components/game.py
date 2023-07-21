import random
import pygame
from game.components.bullets.bullet import Bullet
from game.components.enemies.enemy import Enemy
from game.components.enemies.pause import Pause
from game.components.final_menu import FinalMenu
from game.components.menu import Menu
from game.components.spaceship import Spaceship
from game.utils.constants import BG, ENEMY_1, ENEMY_2, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
class Game:

    ENEMIES = [ENEMY_1, ENEMY_2]

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.paused = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        
        
        self.player = Spaceship("Sebas")
        self.final_menu = FinalMenu()
        self.menu = Menu()
        self.pause = Pause()
    #Enemy
        self.enemies = []
        self.num_enemies = 2
    #Levels
        self.level = 1
    
        self.player.deaths_count = 0 
        
    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.playing = True
        self.level = 1
        self.player.score = 0
        self.player.deaths_count = 0 
        self.player.kills = 0
        while self.playing:
            self.handle_events()
            if not self.paused:
                self.update()
            self.draw()
            if self.paused:
                self.pause.draw(self.screen)
                self.pause.event(self.on_close, self.off_paused)
            if self.player.deaths_count > 1:
                self.playing = False 
                

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT : 
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_p:
                    self.paused = True

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.advance_level()
        self.create_enemies()
        self.enemy_handler()
        self.increase_enemies()
        self.enemy_shoot()


    def draw(self):
        self.clock.tick(FPS) 
        self.screen.fill((255, 255, 255)) 
        if self.paused:
            self.pause.draw(self.screen)
        else:  
            self.draw_background()
            self.player.draw(self.screen, self)
            #Enemy
            for enemy in self.enemies:
                enemy.draw(self.screen)   
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):

        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        user_input = pygame.key.get_pressed()
        if self.player.deaths_count > 0:
            self.final_menu.update(self)
            self.final_menu.draw(self.screen)
            self.final_menu.event(self.on_close, self)
            #self.reset
        else:
            self.menu.draw(self.screen)
            self.menu.event(self.on_close, self.play, user_input)

    def on_close(self):
        self.playing = False
        self.running = False
        self.paused = False

    def off_paused(self):
        self.paused = False
        
    def advance_level(self):
        if self.player.score == 10:
            self.level += 1
            self.player.score = 0
            self.player.kills = 0
    
    #Enemy
    def create_enemies(self):
        if len(self.enemies) < self.num_enemies:
            new_enemy = Enemy( random.choice(self.ENEMIES))
            self.enemies.append(new_enemy)
    
    def enemy_handler(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.y >= SCREEN_HEIGHT:
                self.enemies.remove(enemy)
            if self.player.rect.colliderect(enemy.rect) and not self.player.kills >= 5:
                pygame.time.delay(500)
                self.player.reset()
                self.enemies.remove(enemy)
            elif self.player.kills >= 5 and self.player.rect.colliderect(enemy.rect):
                self.enemies.remove(enemy)
                self.player.score += 1
                self.player.kills += 1

    def increase_enemies(self):
        if self.level == 2:
            self.num_enemies = 3
        elif self.level == 3:
            self.num_enemies = 4
        elif self.level == 4:
            self.num_enemies = 5 
    
    def enemy_shoot(self):
        for enemy in self.enemies:
            if len(enemy.bullets) < 0:
                bullet = Bullet(enemy,"enemy")
                enemy.bullet.append(bullet)
