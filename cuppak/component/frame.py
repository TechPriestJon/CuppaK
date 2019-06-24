import tkinter
from tkinter import ttk
import sys, inspect
import cuppak
import cuppak.component

class Frame(tkinter.Frame):
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, **kw)  
        self._components = []    
        print('frame')       
        self.alter_dimensions(columns, rows) 

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

    def get_components(self):
        return self._grid.components

    def change_child_state(self, state):
        for child in self.winfo_children():
            print(child)
            print(str(type(child)))
            if str(type(child)).endswith('Scale\'>') or str(type(child)).endswith('tkinter.Frame\'>') \
                or str(type(child)).endswith('ttk.Treeview\'>'):
                return

            if not str(type(child)).endswith('Frame\'>'):
                child.configure(state=state)
            else:
                child.change_child_state(state)

    def alter_dimensions(self, columns, rows):
        self._columns = len(columns) 
        self._rows = len(rows)           
        for column in columns:
            self.columnconfigure(columns.index(column), weight=column.weight)

        for row in rows:
            self.rowconfigure(rows.index(row), weight=row.weight)


