import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from cuppak.component.abstractframe import AbstractFrame

class TextEntryFrame(AbstractFrame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._text = ttk.Entry(self, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='we')

    def get_text(self):
        return self._text.get('1.0','end').strip()

