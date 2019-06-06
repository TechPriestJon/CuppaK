import tkinter
import cuppak.component
from cuppak.component import *

class Multiline(Frame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._text = tkinter.Text(self, width=1, height=1, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='nswe')

    def get_text():
        return self._text
