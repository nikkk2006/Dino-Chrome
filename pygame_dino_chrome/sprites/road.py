import pygame


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'assets\images\road.png')
        self.rectangle = self.image.get_rect()

        surface = pygame.display.get_surface()
        self.rectangle.midleft = surface.get_rect().midleft

        self.image_1 = pygame.image.load(r'assets\images\road.png')
        self.rectangle_1 = self.image_1.get_rect()
        self.rectangle_1.midleft = self.rectangle.midright


    def draw(self, surface):
        surface.blit(self.image, self.rectangle)
        surface.blit(self.image_1, self.rectangle_1)

    def update(self):
        self.rectangle.x -= 5
        self.rectangle_1.x -= 5

        if self.rectangle.right < 0:
            self.rectangle.left = self.rectangle_1.right
        elif self.rectangle_1.right < 0:
            self.rectangle_1.left = self.rectangle.right
