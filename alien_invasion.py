import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()  # настройки для игры, импортируем с файла settings

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        # Назначение цвета фона.
        self.bg_color = self.settings.bg_color

        # Инициализация корабля игрока
        self.ship = Ship(self)

        # Инициализация пришельца
        self.alien = Alien(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль вправо.
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # Переместить корабль вправо.
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.alien.blitme()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
