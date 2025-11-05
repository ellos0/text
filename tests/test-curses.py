import curses
from curses import wrapper

def main(stdscr):
  stdscr.clear()
  
  stdscr.addstr(0,0,"main stdout window")
  
  win = curses.newwin(10,40,2,2)
  win.addstr(3,1, "press any key to exit")
  win.box()

  stdscr.refresh()
  win.refresh()

  stdscr.getch()

wrapper(main)
