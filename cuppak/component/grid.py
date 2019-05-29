import tkinter
from tkinter import ttk

class Grid(ttk.Frame):
    def __init__(self, root, style, padding):
        super().__init__(root, style = style, padding = padding)
        self.__components = []

    def add_component(self, factory):
        component = factory.build(self)
        component.grid(column=1, row=1)
        self.__components.append(component)