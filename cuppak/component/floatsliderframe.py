import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class FloatSliderFrame(SliderFrame):
    def __init__(self, window, min=0, max=0, value=0, **kw):
        super().__init__(window, min, max, **kw)

    def _value_as_str(self, value):
        return str(float(value)).strip().lower()

    def _create_entry(self):
        return ttk.Entry(self, width=20, textvariable=self._text_store, validate='focus', validatecommand=self._entry_callback)

    