import tkinter
from tkinter import ttk

class Screen(ttk.Frame):
    def __init__(self, window, columns, rows):
        super().__init__(window)   
        self.__components = []     
        print('window')        
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)

    #def add_grid(self, factory, rows, columns):
    #    grid = factory.build(self, rows, columns)
    #    grid.pack()
    #    self.__grid = grid



    #def add_component(self, factory, column, row):
    #    self.__grid.add_component(factory, column=column, row=row)

    def add_component(self, factory, column, row):
        component = factory.build(self)
        component.grid(column=column, row=row)
        self.__components.append(component)

    def get_components(self):
        return self.__grid.components   