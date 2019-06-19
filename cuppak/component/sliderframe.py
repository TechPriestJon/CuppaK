import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class SliderFrame(Frame):
    def __init__(self, window, min=0, max=0, value=0, **kw):
        column = [ColumnDefinition(1), ColumnDefinition(1), ColumnDefinition(1)]
        row = [RowDefinition(10), RowDefinition(1), RowDefinition(10)]
        super().__init__(window, column, row)
        self.kwargs = kw
        self._scale = None
        self._text = None
        self._fromLabel = None
        self._toLabel = None
        self._from = min
        self._to = max
        self._create_scale()
        self.set_value(float(value))

    def set_min(self, min):
        self._validate_float(min)
        self._from = min
        self._create_scale()
        self.set_value(float(self._from))

    def set_max(self, max):
        self._validate_float(max)
        self._to = max
        self._create_scale()

    def _create_scale(self):
        if self._scale:
            self._scale.destroy()
        if self._text:
            self._text.destroy()
        if self._fromLabel:
           self._fromLabel.destroy()
        if self._toLabel:
            self._toLabel.destroy()
        self._scale = ttk.Scale(self, from_=self._from, to=self._to, command=self._get_slider_set_entry)
        self._scale.grid(column=0, row=1, columnspan=3, sticky='we')

        self._text_store = StringVar()

        self._text = ttk.Entry(self, width=5, textvariable=self._text_store, validate='focus', validatecommand=self._entry_callback)
        self._text.bind('<Return>',self._entry_callback)
        self._text_store.set(str(self._from))

        self._text.grid(column=1, row=0, columnspan=1, sticky='s')
        self._fromLabel = ttk.Label(self, text=str(self._from))
        self._fromLabel.grid(column=0, row=2, columnspan=1, sticky='nw')
        self._toLabel = ttk.Label(self, text=str(self._to))
        self._toLabel.grid(column=2, row=2, columnspan=1, sticky='ne')

    def _get_slider_set_entry(self, value):
        flt_value = float(value)
        self.set_value(flt_value)
    
    def _entry_callback(self, *args, **kwargs):
        text = self._text_store.get().strip().lower()

        try:
            value = float(text)
            self.set_value(value)

        except ValueError:
            print('Value not in range')

        return True

    def get_value(self):
        return self._text_store.get()

    def set_value(self, value):
        self._validate_float(value)
        str_value = self._flt_as_str(value)

        if str_value != self._text_store.get():
            self._text_store.set(self._flt_as_str(value))
        
        if str_value != self._flt_as_str(self._scale.get()):
            if value <= float(self._to) and value >= float(self._from):
                self._scale.set(value)

    def _flt_as_str(self, value):
        return str(int(float(value))).strip().lower()

    def _validate_float(self, value):
        str_value = self._flt_as_str(value)

        if str_value == 'NaN' or str_value == '-inf' or str_value == 'inf' \
            or str_value == 'infinity' or str_value == '-infinity':
            raise ValueError('Invalid number for scale')

