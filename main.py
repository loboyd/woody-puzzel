#!/usr/bin/env python3

from random import randint
from asciimatics.screen import Screen


class Board():
    """
    The game board. Takes a `Board.screen` object to draw on. The board is a
    ten by ten square.
    """

    def __init__(self, screen):
        self.screen = screen
        """The asciimatics screen object that the Board draws characters on"""
        self.data = [[False] * 10 for _ in range(10)]
        self.pieces = [None] * 3

    def draw(self):
        # print board "infrastructure"
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.screen.print_at('\u2502', 2 * i - 1, j)

        # print each board location
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                block = 'x' if self.data[i][j] else ' '
                self.screen.print_at(block, 2 * i, j)


def demo(screen):
    """
    A simple game loop that doesn't do much of anything except display a board.

    Controls:

    - press Enter to show the board
    - press 'q' or 'Q' to quit
    """
    # set up board
    board = Board(screen)

    # for testing
    board.data[0][0] = True
    board.data[2][2] = True

    while True:
        ev = screen.get_key()

        # press Enter to show the board
        if ev == 10:
            board.draw()

        # press q to quit
        elif ev in (ord('Q'), ord('q')):
            return

        screen.refresh()

if __name__ == "__main__":
    Screen.wrapper(demo)
