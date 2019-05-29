#from tkinter import ttk
import tkinter
from tkinter import ttk
from cuppak.component.grid import Grid

class WeightGridFactory():
    def __init__(self):
        print('factory')
        

    def build(self, root, columns, rows):
        self.grid_style = ttk.Style()
        self.grid_style.configure('My.TFrame', background='#334353')
        grid = Grid(root, style='My.TFrame', padding=(3, 3, 12, 12))  # added padding

        for column in columns:
            grid.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            grid.rowconfigure(rows.index(row), weight=row.weight)

        return grid

