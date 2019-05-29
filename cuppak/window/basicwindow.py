#from tkinter import ttk
import tkinter

class BasicWindow(tkinter.Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.__components = []
        self.title(title)
        self.__width = width
        self.__height = height
        self.geometry(str(width) + 'x' + str(height))
        self.resizable(0, 0)
        print('window')        

    def add_component(self, factory):
        self.__components.append(factory.build(self))

    def render(self):
        self.mainloop()

    def get_components(self):
        return self.__components    