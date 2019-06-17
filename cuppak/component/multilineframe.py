import tkinter
import tkinter.scrolledtext as tkscr
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class MultilineFrame(Frame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._text = tkscr.ScrolledText(self, width=1, height=1, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='nswe')
        self.set_text('Some default')

    def get_text(self):
        return self._text.get('1.0','end').strip()

    def set_text(self, text):
        self._text.insert('1.0', text)

