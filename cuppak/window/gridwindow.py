import tkinter

class GridWindow(tkinter.Tk):
    def __init__(self, width, height, title):
        super().__init__()        
        self.title(title)
        self.__width = width
        self.__height = height
        self.geometry(str(width) + 'x' + str(height))
        self.resizable(0, 0)
        print('window')        

    def add_grid(self, factory, rows, columns):
        grid = factory.build(self, rows, columns)
        grid.pack()
        self.__grid = grid

    def render(self):
        self.mainloop()

    def add_component(self, factory):
        self.__grid.add_component(factory)

    def get_components(self):
        return self.__grid.components   