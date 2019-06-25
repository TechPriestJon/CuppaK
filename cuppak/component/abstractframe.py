import tkinter
from tkinter import ttk
import sys, inspect
import cuppak
import cuppak.component
from abc import ABC, abstractmethod

class AbstractFrame(tkinter.Frame, ABC):
    @abstractmethod
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, **kw)  
        self._components = []    
        print('frame')       
        self._alter_dimensions(columns, rows) 

    def get_components(self):
        return self._grid.components

    @abstractmethod
    def change_child_state(self, state):
        for child in self.winfo_children():

            if str(type(child)).endswith('Scale\'>') or str(type(child)).endswith('tkinter.Frame\'>') \
                or str(type(child)).endswith('ttk.Treeview\'>'):
                return

            if not str(type(child)).endswith('Frame\'>'):
                print('child:' + str(type(child)))
                child.configure(state=state)
            else:
                print(child)
                print(str(type(child)))
                child.change_child_state(state)

    def _alter_dimensions(self, columns, rows):
        self._columns = len(columns) 
        self._rows = len(rows)           
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)


