import tkinter

class Window(tkinter.Tk):
    def __init__(self, width, height, title):
        super().__init__()   
        self.__screens = []  
        self.__screen_titles = []    
        self.__current_screen = 0 
        self.title(title)
        self.__width = width
        self.__height = height
        self.geometry(str(width) + 'x' + str(height))
        self.resizable(0, 0)
        print('window')        

    #def add_grid(self, factory, rows, columns):
    #    grid = factory.build(self, rows, columns)
    #    grid.pack()
    #    self.__grid = grid

    #def add_component(self, factory, column, row):
    #    self.__grid.add_component(factory, column=column, row=row)

    def add_screen(self, screen, title):
        self.__screens.append(screen)

        ##if null, set to index
        self.__screen_titles.append(title)

    def load_screen(self, index=None, title=None):
        previous_screen = self.__screens[self.__current_screen]
        previous_screen.pack_forget()
        ##
        screen = self.__screens[index]
        screen.pack(expand=1, fill='both')

        self.__current_screen = index

        ##or search using title

    def render(self):
        self.mainloop()    

    def get_screen_function(self, index):
        return lambda: self.load_screen(index=index)
