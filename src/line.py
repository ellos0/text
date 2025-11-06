from typing import List

LineVector = List[str]
Cursor1D = int
Cursor = List[Cursor1D]

def set_cursor_x(x:Cursor1D, cursor: Cursor, buffer: LineVector):
  if x <= len(buffer[cursor[1]]):
    cursor[0] = x

def set_cursor_y(y:Cursor1D, cursor: Cursor, buffer: LineVector):
  if y <= len(buffer):
    cursor[1] = y


