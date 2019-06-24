import tkinter
from tkinter import *
from tkinter import ttk
import cuppak.component
from cuppak.component import *
from cuppak.dto import *
from abc import ABC, abstractmethod

class SelectorFrame(Frame, ABC):
    @abstractmethod
    def __init__(self, window, columns, rows, radio_buttons, **kw):
        super().__init__(window, columns, rows)
        self._radio_buttons = []
        self._selector_value = StringVar()
        self._create_radio_buttons(radio_buttons, **kw)
        self._selector_value.set(radio_buttons[0].value)

    def _create_radio_buttons(self, radio_buttons, **kw):
        for button in radio_buttons:
            radio_button = self._create_radio_button(button.text, button.value, **kw)
            self._radio_buttons.append(radio_button)
            self._position_radio_button(radio_button, self._radio_buttons.index(radio_button))

    @abstractmethod
    def _position_radio_button(self, radio_button, position):
        pass    
    
    def _create_radio_button(self, text, value, **kw):
        return ttk.Radiobutton(self, text=text, variable=self._selector_value, value=value, **kw)


