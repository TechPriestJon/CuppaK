import tkinter
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class Multiline(Frame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._text = tkinter.Text(self, width=1, height=1, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='nswe')

    def get_text(self):
        return self._text.get('1.0','end').strip()

