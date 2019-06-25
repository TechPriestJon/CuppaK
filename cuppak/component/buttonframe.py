import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from tkinter import *
from cuppak.component.abstractframe import AbstractFrame

class ButtonFrame(AbstractFrame):
    def __init__(self, window, label='', onvalue='', offvalue='', command=None, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._button = ttk.Button(self, text=label,
            command=command, **kw)

        self._button.grid(column=0, row=0, columnspan=1, sticky='we')

