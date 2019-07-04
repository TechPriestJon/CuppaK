import tkinter
import sys, inspect
from array import array
from abc import ABC, abstractmethod

class AbstractFrame(tkinter.Frame, ABC):
    @abstractmethod
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, **kw)  

        if not type(columns) in [list, tuple]:
            raise TypeError('columns must be a list')

        if not type(rows) in [list, tuple]:
            raise TypeError('rows must be a list')

        self._components = []    
        self._alter_dimensions(columns, rows) 

    @abstractmethod
    def change_child_state(self, state):
        for child in self.winfo_children():

            if str(type(child)).endswith('Scale\'>') or str(type(child)).endswith('tkinter.Frame\'>') \
                or str(type(child)).endswith('ttk.Treeview\'>'):
                return

            if not str(type(child)).endswith('Frame\'>'):
                child.configure(state=state)
            else:
                child.change_child_state(state)

    def _alter_dimensions(self, columns, rows):
        self._columns = len(columns) 
        self._rows = len(rows)           
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)
