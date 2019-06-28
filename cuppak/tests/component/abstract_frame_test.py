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

def test_abstract_frame_can_instantiate_concrete():
    concrete_frame = ConcreteAbstractFrame(None, [], [])
    assert concrete_frame

def test_abstract_frame_handles_invalid_columns_parameters():
    expected_error = 'columns must be a list'
    try:
        concrete_frame = ConcreteAbstractFrame(None, 1, [])
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_abstract_frame_handles_invalid_rows_parameters():
    expected_error = 'rows must be a list'
    try:
        concrete_frame = ConcreteAbstractFrame(None, [], 'dog')
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_abstract_frame_alter_dimensions():
    rows = []
    columns = []

    assert False

