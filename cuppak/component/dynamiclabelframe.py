import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class DynamicLabelFrame(Frame):
    def __init__(self, window, text='', **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._create_label(text, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='nswe')

    def set_text(self, text, **kw):
        self._create_label(text, **kw)

    def _create_label(self, text, **kw):
        self._text = ttk.Label(self, text=text, **kw)


