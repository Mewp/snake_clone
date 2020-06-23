class GameStats:
    """Track statistics of Snake"""

    def __init__(self, sg_game):
        """Initialize statistics."""
        self.settings = sg_game.settings
        self.head = sg_game.head
        self.reset_stats()

    def reset_stats(self):
        self.head.rect.x = self.settings.starting_x
        self.head.rect.y = self.settings.starting_y
        self.snake_dir = self.settings.snake_dir
        self.snake_lenght = self.settings.snake_lenght
