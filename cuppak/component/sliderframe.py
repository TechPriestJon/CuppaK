import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *

class SliderFrame(Frame):
    def __init__(self, window, **kw):
        column = [ColumnDefinition(1), ColumnDefinition(1), ColumnDefinition(1)]
        row = [RowDefinition(4), RowDefinition(1), RowDefinition(4)]
        super().__init__(window, column, row)
        self.kwargs = kw
        self._scale = None
        self._text = None
        self._fromLabel = None
        self._toLabel = None
        self._from = 0
        self._to = 0
        self._create_scale()


    #def get_value(self):
    #    return self._text.get('1.0','end').strip()

    def set_from(self, from_value):
        self._from = from_value
        self._create_scale()

    def set_to(self, to_value):
        self._to = to_value
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

        self.sv = StringVar()

        self._text = ttk.Entry(self, width=5, textvariable=self.sv, validate='key', validatecommand=self._entry_callback)
        self._text.insert(0,str(self._from))

        self._text.grid(column=1, row=0, columnspan=1, sticky='s')
        self._fromLabel = ttk.Label(self, text=str(self._from))
        self._fromLabel.grid(column=0, row=2, columnspan=1, sticky='nw')
        self._toLabel = ttk.Label(self, text=str(self._to))
        self._toLabel.grid(column=2, row=2, columnspan=1, sticky='ne')

    def _get_slider_set_entry(self, val):
        self._text.delete(0,'end')
        self._text.insert(0,str(int(float(val))))

    
    def _entry_callback(self):
        print(self.sv.get())
        return True

