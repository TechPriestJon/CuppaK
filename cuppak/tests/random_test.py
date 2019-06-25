import pytest

import cuppak

from cuppak import *
from cuppak.component import *

def test():
    assert True

def test_a2(abd):
    assert 0 == abd.return_zero()

def test_b2():
    label = DynamicLabelFrame(None, 'abc')
    assert str(type(label)) == "<class 'cuppak.component.dynamiclabelframe.DynamicLabelFrame'>"