import curses

#window logic and functions

class Window:
  def __init__(self,height,width,y=1,x=1,buffer=[""], cursor=[0,0]):
    self.height = height
    self.width = width
    self.y = y
    self.x = x
    self.win = curses.newwin(height,width,y,x)

def box(w):
  w.win.box()

def refresh(w):
  w.win.refresh()

def write_cursor(w,text):
  w.win.addstr(w.edit.cursor[1], w.edit.cursor[0], text)

def write(w,y,x,text):
  w.win.addstr(y,x,text)

def cursor(w):
  w.win.move(w.edit.cursor[0],w.edit.cursor[1])
