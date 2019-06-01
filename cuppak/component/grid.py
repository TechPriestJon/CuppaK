import tkinter
from tkinter import ttk

class Grid(ttk.Frame):
    def __init__(self, root, style, padding):
        super().__init__(root, style = style, padding = padding)
        self.__components = []

    def add_component(self, factory, column, row):
        component = factory.build(self)
        component.grid(column=column, row=row)
        self.__components.append(component)