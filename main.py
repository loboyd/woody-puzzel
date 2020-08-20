#!/usr/bin/env python3

from random import randint
from asciimatics.screen import Screen

class Board():
    def __init__(self, screen):
        self.screen = screen
        self.data = [[False]*10 for _ in range(10)]
        self.pieces = [None]*3

    def pprint(self):
        # print board "infrastructure"
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.screen.print_at('\u2502', 2*i-1, j)

        # print each board location
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                block = 'x' if self.data[i][j] else ' '
                self.screen.print_at(block, 2*i, j)

        """
        for row in self.data:
            print('|'.join(['x' if x else ' ' for x in row]))
        """


def demo(screen):
    # set up board
    board = Board(screen)

    board.data[0][0] = True
    board.data[2][2] = True

    while True:
        ev = screen.get_key()

        if ev == 10:
            board.pprint()

        elif ev in (ord('Q'), ord('q')):
            return

        screen.refresh()

Screen.wrapper(demo)




"""
screen.print_at('x',
    randint(0, screen.width), randint(0, screen.height))
"""

