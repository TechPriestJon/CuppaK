import tkinter
from cuppak.window.screen import Screen

class WindowBase():
    def __init__(self, width, height):
        self._screens = []  
        self._screen_titles = []    
        self._current_screen = 0 
        self._width = width
        self._height = height
        print('windowbase')        

    def add_screen(self, columns, rows, title=None):
        screen = Screen(self, columns,rows)
        self._screens.append(screen)

        ##if null, set to index
        if title == None:
            title = str(len(self._screens))

        self._screen_titles.append(str(title))
        
        if len(self._screens) == 1:
            self.load_screen(0)

        return screen

    def load_screen(self, index=None, title=None):
        if index == None and title == None:
            raise ValueError('No Index or Title Reference given')

        if index == None and title != None:
            index = self._screen_titles.index(str(title))
            if index < 0:
                raise ValueError('Title Reference given invalid')

        previous_screen = self._screens[self._current_screen]
        previous_screen.close_subwindows()
        previous_screen.pack_forget()

        screen = self._screens[index]
        screen.pack(expand=1, fill='both')

        self._current_screen = index


    def get_screen_function(self, index=None, title=None):
        if index == None and title == None:
            raise ValueError('No Index or Title Reference given')

        if index == None and title != None:
            index = self._screen_titles.index(str(title))
            if index < 0:
                raise ValueError('Title Reference given invalid')

        return lambda: self.load_screen(index=index)

    def get_screen(self):
        return self._screens[self._current_screen]

