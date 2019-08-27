import pytest
from cuppak.dto import *

def test_column_definition_type():
    component_type = "<class 'cuppak.dto.column_definition.ColumnDefinition'>"
    columndefinition = ColumnDefinition(2)
    assert str(type(columndefinition)) == component_type

def test_column_definition_properties():
    columndefinition = ColumnDefinition(2)
    assert columndefinition.weight == 2

def test_column_definition_invalid_param():
    try:
        columndefinition = ColumnDefinition('2')
        assert False
    except TypeError as error:
        assert str(error) == expected_error


