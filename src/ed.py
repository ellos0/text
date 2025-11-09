import curses

import window
from window import Window

def main(stdscr):
    stdscr.clear()
    curses.curs_set(1) # make cursor visible

    win = Window(10, 40, 2, 2)
    
    window.write(win, 1, 1, "hello, world!\n 2nd line")

    window.box(win)

    stdscr.refresh()
    window.refresh(win)

    stdscr.getch()

curses.wrapper(main)
