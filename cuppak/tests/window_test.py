import pytest
#from CuppaK import conftests
#import conftests
#from conftests import *

def window_opens():
    window = Window('ABC', 10, 10, False)
    assert window
