import tkinter
from tkinter import ttk
import sys, inspect
from cuppak.component.frame import Frame

class Screen(Frame):
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, columns, rows, **kw)  
        self._subwindows = [] 
        print('screen')        
        
    def add_menu(self, menu):
        self._menu = menu
        self.master.config(menu=menu)

    def spawn_subwindow(self, title, width, height, isresizable=True, lockscreen=False, onclosing=False):
        subwindow = self.master.spawn_subwindow(title, width, height, isresizable)
        if lockscreen:
            for child in self.winfo_children():
                if not str(type(child)).endswith('Frame\'>'):
                    child.configure(state='disable')  
                    ##need to loop through children                  
            
            #if self.__menu:
            #    self.__menu.entryconfig(state='disable')

            def on_closing():
                if onclosing:
                    if onclosing():
                        for child in self.winfo_children():
                            if not str(type(child)).endswith('Frame\'>'): 
                                child.configure(state='normal')
                        subwindow.destroy()

                    else:
                        subwindow.lift()
                
                else: 
                    for child in self.winfo_children():
                        if not str(type(child)).endswith('Frame\'>'): 
                            child.configure(state='normal')

                    #if self.__menu:                        
                    #    self.__menu.entryconfig(state='normal')  

            subwindow.protocol("WM_DELETE_WINDOW", on_closing)       

        subwindow.lift()
        self._subwindows.append(subwindow)
        return subwindow

    def close_subwindows(self):
        for subwindow in self._subwindows:
            subwindow.destroy()  
