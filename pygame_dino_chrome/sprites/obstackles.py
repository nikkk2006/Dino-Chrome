import pygame
import random
import os


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        surface = pygame.display.get_surface()
        images = ['largecactus1.png', 'largecactus2.png', 'largecactus3.png',
                  'smallcactus1.png', 'smallcactus2.png', 'smallcactus3.png']
        # путь рандомного кактуса
        random_image = os.path.join(r'assets\images', random.choice(images))

        # загружаю в проект этот спрайт
        self.image = pygame.image.load(random_image)
        self.rect = self.image.get_rect()

        # координаты кактуса
        self.rect.bottomleft = (surface.get_width(), surface.get_height() // 2)   # по у

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= 5

        if self.rect.right < 0:
            self.kill()