import pygame
import pygame.font
from pygame.sprite import Sprite

class BlackField(Sprite):
    """A class for black fields"""
    def __init__(self, sg_game):
        super().__init__()
        self.screen = sg_game.screen

        # load the black field image and set its rec attribute
        self.image = pygame.image.load('images/black.png')
        self.rect = self.image.get_rect()

        # start each new field in top right corner
        self.rect.x = 0
        self.rect.y = 0

        # store fields exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Apple(Sprite):
    """A class for the apple"""
    def __init__(self, sg_game):
        """Initialize apple attributes"""
        super().__init__()
        self.screen = sg_game.screen

        # load the apple image and set its rec attribute
        self.image = pygame.image.load('images/apple.png')
        self.rect = self.image.get_rect()

        # first apple starting position
        self.rect.x = 150
        self.rect.y = 360

        # store apples exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the apple at it's current location"""
        self.screen.blit(self.image, self.rect)

class Play:
    """A class for the play field"""
    def __init__(self, sg_game):
        """Initialize field attributes"""
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()

        # set dimentions and properties of the field
        self.width, self.height = 350, 250
        self.field_color = (250, 250, 250)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # build the field rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_txt()

    def _prep_txt(self):
        """Start-game message"""
        self.txt_image = self.font.render("p - play   Esc - quit", True,
            self.text_color, self.field_color)
        self.txt_image_rect = self.txt_image.get_rect()
        self.txt_image_rect.center = self.rect.center

    def draw_field(self):
        """Draw start-field"""
        self.screen.fill(self.field_color, self.rect)
        self.screen.blit(self.txt_image, self.txt_image_rect)
