import pygame
from pygame.sprite import Sprite


class Head(Sprite):
    """A class for head of the snake"""
    def __init__(self, sg_game):
        """Initialize the snake and set its starting position"""
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings

        # load the head image and set its retc attribute
        self.image = pygame.image.load('images/head.png')
        self.rect = self.image.get_rect()

        # create snake at the starting position
        self.rect.x = self.settings.starting_x
        self.rect.y = self.settings.starting_y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the head in 4 directions"""
        if self.settings.snake_dir == 0:
            self.y -= self.settings.snake_speed
            self.rect.y = self.y
        elif self.settings.snake_dir == 1:
            self.x -= self.settings.snake_speed
            self.rect.x = self.x
        elif self.settings.snake_dir == 2:
            self.y += self.settings.snake_speed
            self.rect.y = self.y
        elif self.settings.snake_dir == 3:
            self.x += self.settings.snake_speed
            self.rect.x = self.x

    def set_up(self):
        """Set up snake at the starting position"""
        self.rect.x = self.settings.starting_x
        self.rect.y = self.settings.starting_y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the head at its current location"""
        self.screen.blit(self.image, self.rect)


class Tail(Sprite):
    """A class for tail of the snake"""
    def __init__(self, sg_game):
        """Initialize the tail and sets it starting position"""
        super().__init__()
        self.screen = sg_game.screen
        self.head = sg_game.head
        self.settings = sg_game.settings
        self.snake_tail = sg_game.snake_tail

        # load the image and set its rect attribute
        self.image = pygame.image.load('images/tail.png')
        self.rect = self.image.get_rect()

        # starts tail at the back of the snake
        self.rect.x = self.head.rect.x
        self.rect.y = self.head.rect.y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """update the tail of the snake"""
        self.rect.x = self.head.rect.x
        self.rect.y = self.head.rect.y
