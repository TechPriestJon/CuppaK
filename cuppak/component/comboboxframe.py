import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class ComboboxFrame(Frame):
    def __init__(self, window, choices=None, default_index=0, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._choices = []
        self._create_combobox(choices, **kw)
        self._combobox.grid(column=0, row=0, columnspan=1, sticky='we')

    def set_values(self, choices=None, default_index=0, **kw):
        self._create_combobox(choices, **kw)

    def _create_combobox(self, choices=None, default_index=0, **kw):
        self._combobox = ttk.Combobox(self, **kw)
        self._combobox['values'] = choices
        if default_index or default_index == 0:
            self._combobox.set(choices[default_index])

    def get_value(self):
        return self._combobox.get().strip()
