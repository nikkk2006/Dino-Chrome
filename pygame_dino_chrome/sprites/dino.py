import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_1 = pygame.image.load(r'assets\images\dinorun1.png')
        self.image_2 = pygame.image.load(r'assets\images\dinorun2.png')
        self.image = self.image_1
        # загружаю звук прыжка
        self.jump_sound = pygame.mixer.Sound(r'assets\sounds\jump.wav')

        self.rect = self.image.get_rect()
        self.step = 0

        screen = pygame.display.get_surface()
        self.rect.x = screen.get_width() // 8
        self.rect.bottom = screen.get_height() // 2

        # высота прыжка
        self.height = 15
        # состояние прыжка
        self.jumping = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        # после каждого седьмого шага dino меняет изображение
        if self.step % 7 == 0:
            if self.image == self.image_1:
                self.image = self.image_2
            elif self.image == self.image_2:
                self.image = self.image_1

        # получаю кортеж из состояний нажатых кнопок(True, False)
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.jumping:
            self.jumping = True
            self.jump_sound.play()

        if self.jumping:
            self.jump()


    def jump(self):
        self.rect.y -= self.height
        self.height -= 1
        if self.height < -15:
            self.height = 15
            self.jumping = False

