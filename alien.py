import pygame


class Alien:
    """Класс пришельца врага."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение пришельца, и получает прямоугольник.
        self.image = pygame.image.load('images/mite.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует пришельца в текущей позиции."""
        self.screen.blit(self.image, self.rect)
