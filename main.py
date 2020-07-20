import sys
import random
import pygame
import time

from settings import Settings
from stats import GameStats
from fields import BlackField, Apple, Play
from snake import Head, Tail


body = []

class SnakeGame:
    """A class to manage the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.fields = pygame.sprite.Group()
        self.snake_tail = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        self.apple = Apple(self)
        self.head = Head(self)
        self.tail = Tail(self)

        self.play = Play(self)


    def run_game(self):
        """Start main loop for the game"""
        self._create_board()

        while True:
            self._check_events()
            if self.settings.game_active:
                self._tail_update()
                self._check_edges()
                self._snake_collision()

            self._screen_update()


    def _screen_update(self):
        self.screen.fill(self.settings.bg_color)

        # draws black fields in the window
        self.fields.draw(self.screen)
        FPS = 10
        clock = pygame.time.Clock()
        clock.tick(FPS)

        # draws apple and whole snake
        self.apple.blitme()
        self.snake_tail.draw(self.screen)
        self.head.blitme()

        if not self.settings.game_active:
            self.play.draw_field()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responses to key presses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_w:
            if self.settings.snake_dir == 2:
                self._end_game()
            else:
                self.settings.snake_dir = 0
        elif event.key == pygame.K_a:
            if self.settings.snake_dir == 3:
                self._end_game()
            else:
                self.settings.snake_dir = 1
        elif event.key == pygame.K_s:
            if self.settings.snake_dir == 0:
                self._end_game()
            else:
                self.settings.snake_dir = 2
        elif event.key == pygame.K_d:
            if self.settings.snake_dir == 1:
                self._end_game()
            else:
                self.settings.snake_dir = 3

    def _create_board(self):
        """Create grid board for the game"""
        field = BlackField(self)
        field_width, field_height = field.rect.size

        for row in range(20):
            for column in range(20):
                self._create_field(row, column)

    def _create_field(self, row, column):
        """Create single black filed"""
        field = BlackField(self)
        field_width, field_height = field.rect.size

        field.x = (field_width + 2) * column
        field.y = (field_height + 2) * row

        field.rect.x = field.x
        field.rect.y = field.y

        self.fields.add(field)

    def _snake_collision(self):
        """Check if snake hits apple or himself"""
        # collision with apple
        l = len(body)
        if self.apple.rect.x == self.head.rect.x and (
                self.apple.rect.y) == self.head.rect.y:
            tail = Tail(self)
            body.insert(0, [self.head.rect.x, self.head.rect.y])
            x = random.randint(0, 19)
            self.apple.rect.x = x * 30
            y = random.randint(0, 19)
            self.apple.rect.y = y * 30
            self.settings.snake_lenght += 1

            self.snake_tail.add(tail)

        for all in range(1, l):
            coord = body[all]
            tail_x = coord[0]
            tail_y = coord[1]
            if self.head.rect.x == tail_x and self.head.rect.y == tail_y:
                print("tail hit")
                self._end_game()


    def _tail_update(self):
        """Move the tail of the snake"""
        tail = Tail(self)
        head_x = self.head.rect.x
        head_y = self.head.rect.y
        z = self.settings.snake_lenght
        l = len(body)
        self._head_update()
        # puts an instance at the begining of the tail-list
        body.insert(0, [head_x, head_y])

        head_x = self.head.rect.x
        head_y = self.head.rect.y

        # redraw the tail
        self.snake_tail.empty()
        for all in range(l):
            coord = body[all]
            tail_x = coord[0]
            tail_y = coord[1]
            self._add_tail(tail_x, tail_y)

    def _add_tail(self, tail_x, tail_y):
        """Add tail parts during redrawing"""
        tail = Tail(self)
        tail.rect.x = tail_x
        tail.rect.y = tail_y
        self.snake_tail.add(tail)

    def _head_update(self):

        if len(body) > 0:
            self.head.update()
            del body[-1]
        else:
            self.head.update()

    def _check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.head.rect.right > screen_rect.right or (
        self.head.rect.left) < 0 or self.head.rect.top < 0 or (
        self.head.rect.bottom) > screen_rect.bottom:
            self._end_game()

    def _end_game(self):
        del body[:]
        self.snake_tail.empty()
        self.settings.snake_lenght = 0
        self.settings.snake_dir = 0
        self.apple.rect.x = 150
        self.apple.rect.y = 360
        self.head.set_up()
        self._screen_update()
        self.settings.game_active = False

    def _start_game(self):
        self.settings.game_active = True

if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
