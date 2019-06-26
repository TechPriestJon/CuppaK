import pytest
from cuppak.component.abstract_frame import AbstractFrame

class ConcreteAbstractFrame(AbstractFrame):
    def __init__(self, window, columns, rows, **kw):
        super().__init__(window, columns, rows, **kw)  

    def change_child_state(self, state):
        super().change_child_state(state)        

def test_abstract_frame_not_instantiatable():
    expected_error = "Can't instantiate abstract class AbstractFrame " + \
        'with abstract methods __init__, change_child_state'
    try:
        abstract_frame = AbstractFrame(None, [], [])
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_abstract_frame_get_components():
    assert False

def test_abstract_frame_alter_dimensions():
    assert False

