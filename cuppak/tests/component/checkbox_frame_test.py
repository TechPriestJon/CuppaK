import pytest
from cuppak.component import *

def test_checkbox_frame_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    checkbox = CheckboxFrame(None)
    assert str(type(checkbox)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type