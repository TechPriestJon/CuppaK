import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from tkinter import *
from cuppak.component.abstractframe import AbstractFrame

class CheckboxFrame(AbstractFrame):
    def __init__(self, window, label='', onvalue='', offvalue='', command=None, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._checkbox_value = StringVar()
        self._checkbox_value.set(str(offvalue))
        if command:
            self._checkbox = ttk.Checkbutton(self, text=label, variable=self._checkbox_value,
                onvalue=onvalue, offvalue=offvalue, command=command, **kw)
        else:
            self._checkbox = ttk.Checkbutton(self, text=label, variable=self._checkbox_value,
                onvalue=onvalue, offvalue=offvalue, **kw)
        self._checkbox.grid(column=0, row=0, columnspan=1, sticky='we')

    def get_value(self):
        return self._checkbox_value.get().strip()
