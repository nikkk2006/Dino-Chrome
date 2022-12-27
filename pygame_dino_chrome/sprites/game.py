import pygame


class GameOver(pygame.sprite.Sprite):
    """Этот спрайт отображает конец игры"""
    def __init__(self):
        super().__init__()
        surface = pygame.display.get_surface()

        self.image = pygame.image.load(r'assets\images\reset.png')
        self.rect = self.image.get_rect()

        # отображение значка reset по центру
        self.rect.center = (surface.get_width() // 2, surface.get_height() // 3)

        # работа со шрифтом
        self.GREY = (83, 83, 83)
        self.font = pygame.font.Font(r'assets\fonts\gamefont.ttf', 20)
        self.font_image = self.font.render('GAME OVER', True, self.GREY)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.center = (surface.get_width() // 2, surface.get_height() // 4)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.font_image, self.font_rect)
