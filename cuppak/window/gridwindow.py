import tkinter

class GridWindow(tkinter.Tk):
    def __init__(self, width, height, title, columns, rows):
        super().__init__()   
        self.__components = []     
        self.title(title)
        self.__width = width
        self.__height = height
        self.geometry(str(width) + 'x' + str(height))
        self.resizable(0, 0)
        print('window')        
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)

    def add_grid(self, factory, rows, columns):
        grid = factory.build(self, rows, columns)
        grid.pack()
        self.__grid = grid

    def render(self):
        self.mainloop()

    #def add_component(self, factory, column, row):
    #    self.__grid.add_component(factory, column=column, row=row)

    def add_component(self, factory, column, row):
        component = factory.build(self)
        component.grid(column=column, row=row)
        self.__components.append(component)

    def get_components(self):
        return self.__grid.components   