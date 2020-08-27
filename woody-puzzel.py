#!/usr/bin/env python3

from display import Screen, Board


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


def main():
    Screen.wrapper(demo)


if __name__ == "__main__":
    main()
