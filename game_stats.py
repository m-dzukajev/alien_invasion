import json


class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """Gets high score from file, if it exists."""
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
