import pytest
from cuppak.component import *

def test_integer_slider_frame_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    floatsliderframe = IntegerSliderFrame(None)
    assert str(type(floatsliderframe)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type