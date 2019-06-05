import tkinter
from tkinter import ttk
import sys, inspect

class Screen(ttk.Frame):
    def __init__(self, window, columns, rows):
        super().__init__(window)   
        self.__components = []    
        self.__subwindows = []     
        print('screen')        
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)

    def add_component(self, component_type, column, row, component_module='tkinter', **kw):
        #classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        #classes.extend(inspect.getmembers(sys.modules['tkinter'], inspect.isclass))
        #classes.extend(inspect.getmembers(sys.modules['tkinter.ttk'], inspect.isclass))

        #if classes.index(component_type) == None or classes.index(component_type) < 0:
        #    raise ValueError('Invalid component type to construct')

        if not isinstance(component_type, str):
            raise ValueError('Invalid component type to construct')

        if component_module == 'tkinter':
            component_inst = getattr(tkinter, component_type)
        elif component_module == 'tkinter.ttk':
            component_inst = getattr(tkinter.ttk, component_type)
        else:
            component_inst = getattr(cuppak.component, component_type)

        component = component_inst(self, **kw)
        component.grid(column=column, row=row)
        self.__components.append(component)
    
    def add_menu(self, menu):
        self.__menu = menu
        self.master.config(menu=menu)

    def get_components(self):
        return self.__grid.components   

    def spawn_subwindow(self, title, width, height, isresizable=True, lockscreen=False, onclosing=False):
        subwindow = self.master.spawn_subwindow(title, width, height, isresizable)
        if lockscreen:
            for child in self.winfo_children():
                child.configure(state='disable')
            
            #if self.__menu:
            #    self.__menu.entryconfig(state='disable')

            def on_closing():
                if onclosing:
                    if onclosing():
                        for child in self.winfo_children():
                            child.configure(state='normal')
                        subwindow.destroy()

                    else:
                        subwindow.lift()
                
                else: 
                    for child in self.winfo_children():
                        child.configure(state='normal') 

                    #if self.__menu:                        
                    #    self.__menu.entryconfig(state='normal')  

            subwindow.protocol("WM_DELETE_WINDOW", on_closing)       

        subwindow.lift()
        self.__subwindows.append(subwindow)
        return subwindow

    def close_subwindows(self):
        for subwindow in self.__subwindows:
            subwindow.destroy()  
