import tkinter
from tkinter import ttk
import sys, inspect
from cuppak.component.frame import Frame
from cuppak.dto import *

class TabFrame(Frame):
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, columns, rows)
        self._tabs = []
        self._views = []
        self._tfcolumns = columns
        self._tfrows = rows

        tabcolumns = [ColumnDefinition(1)]
        tabrows = [RowDefinition(1)]

        self._tabframe = self.add_component('Frame', 0, 0, component_module='this', \
            fill_frame=True, columns=tabcolumns, rows=tabrows)

        if len(columns) > len(rows):
            viewcolumn = 1
            viewrow = 0
        else:
            viewcolumn = 0
            viewrow = 1           

        viewcolumns = [ColumnDefinition(1)]
        viewrows = [RowDefinition(1)]

        self._viewframe = self.add_component('Frame', viewcolumn, viewrow, component_module='this', \
            fill_frame=True, columns=viewcolumns, rows=viewrows)
        print('tabframe')        


    def add_tab(self, text):
        if len(self._tfcolumns) > len(self._tfrows):
            tabcolumns = [ColumnDefinition(1)]
            tabrows = []
            for rows in range(len(self._tabs) + 1):
                tabrows.append(RowDefinition(1))
        else:
            tabcolumns = []
            for columns in range(len(self._tabs) + 1):
                tabcolumns.append(ColumnDefinition(1))
            tabrows = [RowDefinition(1)]   

        self._tabframe.alter_dimensions(tabcolumns, tabrows)
        tab = self._tabframe.add_component('Button', (len(tabcolumns) - 1), (len(tabrows) - 1), component_module='ttk', \
                text=text, command=self._get_switch_tab_command(len(self._tabs)), fill_frame=True)

        self._tabs.append(tab)
        
        viewcolumns = [ColumnDefinition(1)]
        viewrows = [RowDefinition(1)]

        view = self._viewframe.add_component('Frame', 0, 0, component_module='this', fill_frame=True, \
                    columns=viewcolumns, rows=viewrows)

        self._views.append(view)

        print(len(self._views))

        if len(self._views) > 1:
            view.grid_remove()
        else:
            self._currentview = view
            #tab.config(relief='flat')
            tab.state(['pressed'])

        return view

    def _get_switch_tab_command(self, index):
        return lambda: self._switch_tab(index)

    def _switch_tab(self, index):
        self._currentview.grid_remove()
        tab = self._tabs[self._views.index(self._currentview)]
        tab.state(['!pressed'])

        self._currentview = self._views[index]
        self._currentview.grid(column=0, row=0, columnspan=1, sticky='nswe')
        self._tabs[index].state(['pressed'])

        ##switchtab
    def get_tab_frame(self, index):
        return self._views.index(index)

    def get_tabs():
        return self._tabframe

    def get_view():
        return self._tabframe


