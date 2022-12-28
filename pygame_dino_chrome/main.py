from sprites.road import Road
from sprites.cloud import Cloud
from sprites.dino import Dino
from sprites.obstackles import Cactus
from sprites.score import Score
from sprites.game import GameOver
import pygame
pygame.init()


def main():
    global RUNNING, GAMEOVER, end

    # создание констант
    WIDTH = 700
    HEIGHT = 500
    FPS = 60
    RUNNING = True
    GAMEOVER = False
    WHITE = (255, 255, 255)

    # создание главного экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dino chrome')
    pygame.display.set_icon(pygame.image.load(r'assets\images\joystick_game.png'))
    clock = pygame.time.Clock()

    # создание спрайтов
    score = Score()
    road = Road()
    dino = Dino()
    clouds = pygame.sprite.Group()
    obstackles = pygame.sprite.Group()

    # главный цикл
    while RUNNING:
        clock.tick(FPS)

        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and GAMEOVER:
                    main()

        # проверка на столкновение с кактусами
        for obstackle in obstackles:
            if pygame.sprite.collide_mask(dino, obstackle) and not GAMEOVER:
                sound_game_over = pygame.mixer.Sound(r'assets\sounds\die.wav')
                sound_game_over.play()
                GAMEOVER = True
                end = GameOver()

                # записываю очки в high-score.txt
                with open('high-score.txt', 'w') as file:
                    file.write(str(score.points))

        # рендеринг
        screen.fill(WHITE)
        score.draw(screen)
        road.draw(screen)
        clouds.draw(screen)
        dino.draw(screen)
        obstackles.draw(screen)

        if GAMEOVER:
            end.draw(screen)

        # обновление спрайтов
        if not GAMEOVER:
            score.update()
            if len(clouds) < 3:
                cloud = Cloud()
                clouds.add(cloud)
            clouds.update()
            road.update()
            dino.update()
            if len(obstackles) < 1:
                obstackle = Cactus()
                obstackles.add(obstackle)
            obstackles.update()

        # обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()