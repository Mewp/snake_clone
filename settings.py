class Settings:
    """A class to store all settings of Snake game"""
    def __init__(self):
        """Initialize game settings"""

        # screen settings
        self.screen_width = 598
        self.screen_height = 598
        self.bg_color = (230, 230, 230)

        self.game_active = False

        # snake settings
        self.snake_speed = 30
        self.starting_x = 300
        self.starting_y = 300
        # snakes movement direction
        # 0 = up
        # 1 = left
        # 2 = down
        # 3 = right
        self.snake_dir = 0
        self.snake_lenght = 0
