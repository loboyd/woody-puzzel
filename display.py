#!/usr/bin/env python3

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
