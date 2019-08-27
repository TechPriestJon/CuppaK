import pytest
from cuppak.component import *

def test_treeview_item_definition_type():
    component_type = "<class 'cuppak.component.button_frame.ButtonFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    floatsliderframe = SliderFrame(None)
    assert str(type(floatsliderframe)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type