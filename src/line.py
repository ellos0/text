from typing import List
import window

#line editor

LineVector = List[str]
Cursor1D = int
Cursor = List[Cursor1D]

class Edit:
  def __init__(self,buffer: LineVector, cursor:Cursor):
    self.buffer = buffer
    self.cursor = cursor
  

def set_cursor_x(w, x:Cursor1D) -> None:
  if x <= len(edit.buffer[edit.cursor[1]]):
    w.edit.cursor[0] = x

def set_cursor_y(w, y:Cursor1D) -> None:
  if y <= len(edit.buffer):
    w.edit.cursor[1] = y

def set_cursor_x_n(w,x:Cursor1D) -> None:
  w.edit.cursor[0] = x

def set_cursor_y_n(w,y:Cursor1D) -> None:
  w.edit.cursor[1] = y

def set_cursor(w, cursor: Cursor) -> None:
  set_cursor_x(w,cursor[0])
  set_cursor_y(w,cursor[1])
  w.edit.cursor = cursor
  window.cursor(w)

def set_cursor_n(w,cursor:Cursor) -> None:
  set_cursor_x_n(w,cursor[0])
  set_cursor_x_n(w,cursor[1])
  w.edit.cursor = cursor
  window.cursor(w)

def get_current_line_number(w) -> int:
  if w.edit.cursor[1] > (len(w.edit.buffer)) - 1:
    return len(w.edit.buffer) - 1
  else:
    return w.edit.cursor[1]

def get_current_line(w) -> str:
  return w.edit.buffer[get_current_line_number(w)]

def insert_text(w, x:str) -> None:
  before = get_current_line(w)[:w.edit.cursor[0]]
  after = get_current_line(w)[w.edit.cursor[0]:]

  w.edit.buffer[get_current_line_number(w)] = before + x + after
  window.write(w, w.edit.cursor[1],w.edit.cursor[0], x + after)

def compile_line_vector(w) -> str:
  out = ""
  for line in w.edit.buffer:
    out += (line + '\n')
  return out

