class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 130, 180)

        # Настройка корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 433
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # Как быстро ускоряется игра
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        # Стандартная сложность
        self.difficulty_level = 'medium'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        # Сложности игры, easy, medium, difficult
        if self.difficulty_level == 'easy':
            self.ship_limit = 5
            self.ship_speed = 0.75
            self.bullet_speed = 3.0
            self.alien_speed =0.5
            self.ship_bullets_allowed = 10

        elif self.difficulty_level == 'medium':
            self.ship_limit = 3
            self.bullets_allowed = 3
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0

        elif self.difficulty_level == 'difficult':
            self.ship_limit = 2
            self.bullets_allowed = 3
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 20

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


    def set_difficulty(self, diff_setting):
        if diff_setting == 'easy':
            print('easy')
        elif diff_setting == 'medium':
            print('medium')
        elif diff_setting == 'difficult':
            print('difficult')