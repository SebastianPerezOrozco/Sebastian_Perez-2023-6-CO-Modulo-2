import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class FinalMenu:

    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
 
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 100)
        self.game_over = self.font.render("GAME OVER", True, (255, 0, 0))
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        
        self.decision_font = pygame.font.Font(FONT_STYLE, 15)
        self.decision  = self.decision_font.render("|  Press  [Any key]  to Reset Game  | ", True, (255, 255, 0))
        self.decision_rect = self.decision.get_rect()
        self.decision_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        
        self.max_level = 0

    def event(self,on_close, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                on_close()
            elif event.type == pygame.KEYDOWN:
                game.play()

    def update(self, game):
    
        if game.level > self.max_level:
            self.max_level = game.level
        self.font_1 = pygame.font.Font(FONT_STYLE, 60)    
        self.max_score_message = self.font_1.render(f"The highest level is: {self.max_level} ", True, (255, 255, 255))
        self.max_score_message_rect = self.max_score_message.get_rect()
        self.max_score_message_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

    def draw(self, screen):
         screen.fill((0, 0, 0))
         screen.blit(self.max_score_message,  self.max_score_message_rect)
         screen.blit(self.game_over, self.game_over_rect)
         screen.blit(self.decision, self.decision_rect)
         pygame.display.update()

