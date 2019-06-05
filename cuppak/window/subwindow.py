import tkinter
from cuppak.window.screen import Screen
from cuppak.window.windowbase import WindowBase

class SubWindow(tkinter.Toplevel, WindowBase):
    def __init__(self, title, width, height, isresizable=True, **kw):
        tkinter.Toplevel.__init__(self, **kw)   
        WindowBase.__init__(self, width, height)   
        self.title(title)
        self.geometry(str(self._width) + 'x' + str(self._height))
        self.resizable(0, 0)
        print('subwindow')    


