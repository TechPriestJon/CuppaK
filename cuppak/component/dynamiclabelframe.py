import tkinter
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from PIL import Image, ImageTk
from cuppak.component.abstractframe import AbstractFrame

class DynamicLabelFrame(AbstractFrame):
    def __init__(self, window, text='', image=None, **kw):
        column = [ColumnDefinition(1)]
        row = [RowDefinition(1)]
        super().__init__(window, column, row)
        self._create_label(text, image, **kw)
        self._text.grid(column=0, row=0, columnspan=1, sticky='nswe')

    def set_label(self, text, image=None, **kw):
        self._create_label(text, image, **kw)

    def _create_label(self, text, image=None, **kw):
        if image:
            self._label_image = Image.open(image)
            self._label_icon = ImageTk.PhotoImage(self._label_image)
            self._text = ttk.Label(self, text=text, image=self._label_icon, **kw)
        else:
            self._text = ttk.Label(self, text=text, **kw)       

    def change_child_state(self, state):
        super().change_child_state(state)
