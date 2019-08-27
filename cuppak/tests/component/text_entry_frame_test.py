import pytest
from cuppak.component import *

def test_text_entry_frame_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    floatsliderframe = TextEntryFrame(None)
    assert str(type(floatsliderframe)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type