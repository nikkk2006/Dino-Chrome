import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        surface = pygame.display.get_surface()
        self.GREY = (83, 83, 83)
        self.step = 0     # номер текущего шага
        self.points = 0   # количество очков

        # загружаю шрифт в проект
        self.font = pygame.font.Font(r'assets\fonts\gamefont.ttf', 20)
        self.image = self.font.render(f'HI {self.points}', True, self.GREY)
        self.rect = self.image.get_rect()

        # расположение надписи на экране
        self.rect.right = surface.get_width()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f'HI {self.points}', True, self.GREY)
        self.rect.right = surface.get_width() - 20 * len(str(self.points))

    def update(self):
        self.step += 1
        # на каждый 10-ый шаг очки увеличиваются
        if self.step % 10 == 0:
            self.points += 1
