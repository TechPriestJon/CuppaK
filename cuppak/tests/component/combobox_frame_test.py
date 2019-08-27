import pytest
from cuppak.component import *

def test_combobox_frame_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    combobox = ComboboxFrame(None)
    assert str(type(combobox)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type