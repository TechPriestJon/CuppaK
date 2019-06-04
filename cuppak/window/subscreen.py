import tkinter
from tkinter import ttk

class SubScreen(ttk.Frame):
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

    def add_component(self, component, column, row):
        component.grid(column=column, row=row)
        self.__components.append(component)

    def add_component_type(self, component_type, column, row, **kw):
        component_inst = getattr(tkinter, component_type)
        component = component_inst(self, **kw)
        component.grid(column=column, row=row)
        self.__components.append(component)
    
    def add_menu(self, menu):
        self.master.config(menu=menu)

    def get_components(self):
        return self.__grid.components   

    #def render():
        #add_menu    
