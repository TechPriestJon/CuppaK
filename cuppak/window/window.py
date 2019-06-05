import tkinter
from cuppak.window.screen import Screen
from cuppak.window.subwindow import SubWindow
from cuppak.window.windowbase import WindowBase

class Window(tkinter.Tk, WindowBase):
    def __init__(self, title, width, height, isresizable=True, **kw):
        tkinter.Tk.__init__(self, **kw)   
        WindowBase.__init__(self, width, height)   
        self.title(title)
        self.geometry(str(self._width) + 'x' + str(self._height))
        if isresizable == False:
            self.resizable(0, 0)
        print('window')        

    def render(self):
        self.mainloop()    

    def spawn_subwindow(self, title, width, height, isresizable=True):
        return SubWindow(title, width, height, isresizable)
        
