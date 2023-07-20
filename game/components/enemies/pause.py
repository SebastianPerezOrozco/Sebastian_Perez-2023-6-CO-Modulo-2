import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Pause:

    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
 
    def __init__(self):
        self.font_title = pygame.font.Font(FONT_STYLE , 80)
        self.title = self.font_title.render("PAUSE", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT )
       
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.options  = self.font.render("|  Press  [Any key]  to Continue the Game  |  ", True, (255, 255, 0))
        self.options_rect = self.options.get_rect()
        self.options_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
    
    def event(self, on_close, off_paused):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                on_close()
            if event.type == pygame.KEYDOWN :
                off_paused()
                

    def draw (self, screen):
         screen.fill((0, 0, 0))
         screen.blit(self.title,  self.title_rect)
         screen.blit(self.options, self.options_rect)
         pygame.display.update()