import pygame
from game.utils.constants import  FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message = "||Press any key [ ] to start||", text_size = 30):

        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.font_credit = pygame.font.Font(FONT_STYLE , 15)
        self.font_title = pygame.font.Font(FONT_STYLE , 80)

        self.icon = pygame.transform.scale(ICON, (116, 106))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT )
        
        self.title = self.font_title.render("GALAXY WAR", True, (0, 0, 0))
        self.font_title_rect = self.title.get_rect()
        self.font_title_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        
        self.credit_message = self.font_credit.render("Created by: Sebastián Pérez Orozco", True, (0, 0, 0))
        self.credit_message_rect = self.credit_message.get_rect()
        self.credit_message_rect.bottomright = (280, SCREEN_HEIGHT-10)
        
        self.update_message(message)

    def event(self, on_close, on_start, user_input):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or user_input[pygame.K_ESCAPE]:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw (self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.credit_message, self.credit_message_rect)
        screen.blit(self.title, self.font_title_rect)
        pygame.display.update()

    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center= (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)