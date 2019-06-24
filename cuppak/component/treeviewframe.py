import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class TreeviewFrame(Frame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._create_treeview(**kw)

    def _create_treeview(self, **kw):
        self._treeview = ttk.Treeview(self)

        self._treeview["columns"]=("one","two")
        self._treeview.column("one", width=100 )
        self._treeview.column("two", width=100)
        self._treeview.heading("one", text="coulmn A")
        self._treeview.heading("two", text="column B")

        self._treeview.insert("" , 0,    text="Line 1", values=("1A","1b"))

        id2 = self._treeview.insert("", 1, "dir2", text="Dir 2")
        self._treeview.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
        self._treeview.grid(column=0, row=0, columnspan=1, sticky='nswe')  


