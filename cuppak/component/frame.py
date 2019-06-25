import tkinter
from tkinter import ttk
import sys, inspect
import cuppak
import cuppak.component
from cuppak.component.abstractframe import AbstractFrame

class Frame(AbstractFrame):
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, columns, rows, **kw)  

    def add_component(self, component_type, column, row, component_module='tkinter', fill_frame=False, **kw): 
        if column >= self._columns:
            raise ValueError('Column is outside range of screen columns')
            
        if row >= self._rows:
            raise ValueError('Row is outside range of screen rows')    
        
        classes = inspect.getmembers(sys.modules['cuppak.component'], inspect.isclass)
        classes.extend(inspect.getmembers(sys.modules['tkinter'], inspect.isclass))
        classes.extend(inspect.getmembers(sys.modules['tkinter.ttk'], inspect.isclass))

        class_is_present = [x[0] for x in classes].index(component_type) > -1

        if not class_is_present:
            raise ValueError('Invalid component type to construct')

        if not isinstance(component_type, str):
            raise ValueError('Invalid component type to construct')

        if component_module == 'tkinter':
            component_inst = getattr(tkinter, component_type)
        elif component_module == 'ttk':
            component_inst = getattr(tkinter.ttk, component_type)
        else:
            component_inst = getattr(cuppak.component, component_type)

        component = component_inst(self, **kw)

        if fill_frame:
            component.grid(column=column, row=row, columnspan=1, sticky='nswe')
        else:
            component.grid(column=column, row=row)

        self._components.append(component)  
        return component

    def alter_dimensions(self, columns, rows):
        self._alter_dimensions(columns, rows)

    def change_child_state(self, state):
        super().change_child_state(state)

