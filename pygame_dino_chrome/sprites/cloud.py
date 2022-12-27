import pygame
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'assets\images\cloud.png')
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()

        # начальное положение спрайта
        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, surface.get_height() // 3)

        # шаг движения
        self.step_x = random.randint(3, 6)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.step_x

        if self.rect.right < 0:
            self.kill()








