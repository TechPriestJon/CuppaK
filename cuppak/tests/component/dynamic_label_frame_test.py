import pytest
from cuppak.component import *

def test_dynamic_label_frame_type():
    component_type = "<class 'cuppak.component.dynamic_label_frame.DynamicLabelFrame'>"
    inner_component_type = "<class 'tkinter.ttk.Button'>"
    label = DynamicLabelFrame(None, 'abc')
    assert str(type(label)) == component_type
    assert str(type(checkbox._checkbox)) == inner_component_type