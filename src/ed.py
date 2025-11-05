import curses

from window import Window

def main(stdscr):
    stdscr.clear()
    win = Window(10, 40, 2, 2)

    win.write(1, 1, "hello")
    win.box()

    stdscr.refresh()
    win.refresh()

    stdscr.getch()

curses.wrapper(main)
