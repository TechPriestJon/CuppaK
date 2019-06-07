import tkinter
from tkinter import ttk
import sys, inspect
from cuppak.component.tabframe import TabFrame
from cuppak.dto import *

class HorizontalTabFrame(TabFrame):
    def __init__(self, window, **kw):
        columns = [ColumnDefinition(1)]
        rows = [RowDefinition(1), RowDefinition(99)]

        super().__init__(window, columns, rows)
