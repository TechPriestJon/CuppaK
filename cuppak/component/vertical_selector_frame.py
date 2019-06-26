import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.component.selector_frame import SelectorFrame
from cuppak.dto import *

class VerticalSelectorFrame(SelectorFrame):
    def __init__(self, window, radio_buttons, **kw):
        columns = [ColumnDefinition(1)]
        rows = []
        for radio_button in range(len(radio_buttons) + 1):
            rows.append(RowDefinition(1))

        super().__init__(window, columns, rows, radio_buttons, **kw)

    def _position_radio_button(self, radio_button, position):
        radio_button.grid(column=0, row=position, columnspan=1, sticky='nswe')   


