import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class TreeviewFrame(Frame):
    def __init__(self, window, columns=[], **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._items = []
        self._item_definitions = []
        self._columns = columns
        self._create_treeview(**kw)

    def _create_treeview(self, **kw):
        self._treeview = ttk.Treeview(self)
        columns = []

        for column in self._columns:
            columns.append(column.name)

        self._treeview["columns"]=columns

        for column in self._columns:
            self._treeview.column(column.name, width=column.width)
            self._treeview.heading(column.name, text=column.title) 

        self._treeview.grid(column=0, row=0, columnspan=1, sticky='nswe')  

    def _add_directory(self, directory_definition):
        directory = self._treeview.insert(directory_definition.parent, \
             len(self._items), directory_definition.name, text=directory_definition.title, open=directory_definition.open)
        self._items.append(directory)

        for item in directory_definition.items:
            self._add_item(item)

    def _add_item(self, item_definition):
        self._item_definitions.append(item_definition)
        item = self._treeview.insert(item_definition.parent, len(self._items), \
            str(len(self._items)), text=item_definition.title, \
            values=item_definition.get_values(self._columns))
        self._items.append(item)
        if item_definition.get_command():
            self._treeview.bind("<Double-1>", self._item_command)

    def _item_command(self, event):
        selected_item = self._treeview.selection()[0]
        title = self._treeview.item(selected_item,"text")
        for definition in self._item_definitions:
            if definition.title == title:
                command = definition.get_command()
                if command:
                    command()
                break





