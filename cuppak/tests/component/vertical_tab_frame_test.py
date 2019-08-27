import pytest
from cuppak.component import *

def test_vertical_tab_frame_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    floatsliderframe = VerticalTabFrame(None)
    assert str(type(floatsliderframe)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type