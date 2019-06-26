import pytest
from cuppak.component import *

def test_check_dynamic_label_frame_type():
    label = DynamicLabelFrame(None, 'abc')
    assert str(type(label)) == "<class 'cuppak.component.dynamic_label_frame.DynamicLabelFrame'>"