import tkinter
from tkinter import ttk
import sys, inspect
from cuppak.component.tab_frame import TabFrame
from cuppak.dto import *

class VerticalTabFrame(TabFrame):
    def __init__(self, window, **kw):
        columns = [ColumnDefinition(1), ColumnDefinition(99)]
        rows = [RowDefinition(1)]

        super().__init__(window, columns, rows)