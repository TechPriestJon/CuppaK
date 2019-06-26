import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from tkinter import *
from PIL import Image, ImageTk
from cuppak.component.abstract_frame import AbstractFrame

class ButtonFrame(AbstractFrame):
    def __init__(self, window, label='', command=None, image=None, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)

        self._create_button(label, image, command, **kw)
        self._button.grid(column=0, row=0, columnspan=1, sticky='nesw')

    def set_button(self, label, image=None, command=None, **kw):
        self._create_label(label, image, command, **kw)

    def _create_button(self, label, image=None, command=None, **kw):
        if image:
            self._button_image = Image.open(image)
            self._button_icon = ImageTk.PhotoImage(self._button_image)
            self._button = ttk.Button(self, text=label,
                command=command, image=self._button_icon, **kw)
        else:
            self._button = ttk.Button(self, text=label,
                command=command, **kw)

    def change_child_state(self, state):
        super().change_child_state(state)                