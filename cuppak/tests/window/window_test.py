import pytest
from cuppak.window import *

def test_swindow_opens():
    window = Window('ABC', 10, 10, False)
    assert window
