import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.component.selector_frame import SelectorFrame
from cuppak.dto import *

class HorizontalSelectorFrame(SelectorFrame):
    def __init__(self, window, radio_buttons, **kw):
        columns = []
        rows = [RowDefinition(1)]
        for radio_button in range(len(radio_buttons) + 1):
            columns.append(ColumnDefinition(1))

        super().__init__(window, columns, rows, radio_buttons, **kw)

    def _position_radio_button(self, radio_button, position):
        radio_button.grid(column=position, row=0, columnspan=1, sticky='nswe')   


