import pytest
from cuppak.validator.list_validator import ListValidator

##SET UP
class ConcreteAbstractListValidator(ListValidator):
    def __init__(self):
        pass   

##TESTS
def test_list_validator_not_instantiatable():
    expected_error = "Can't instantiate abstract class ListValidator with abstract methods __init__"
    try:
        list_validator = ListValidator()
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_list_validator_can_instantiate_concrete():
    concrete_frame = ConcreteAbstractListValidator()
    assert concrete_frame

def test_list_validator_integer():
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list(1) == False

def test_list_validator_string():    
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list('1') == False

def test_list_validator_float():    
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list(1.2) == False

def test_list_validator_list():    
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list([1,2]) == True

def test_list_validator_tuple():    
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list((1,'quack',2)) == True

def test_list_validator_dictionary():    
    validator = ConcreteAbstractListValidator()
    assert validator.validate_list({'duck':'quack', 'number': 1}) == True

