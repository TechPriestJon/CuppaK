import pytest
from cuppak.validator.integer_validator import IntegerValidator

##SET UP
class ConcreteAbstractIntegerValidator(IntegerValidator):
    def __init__(self):
        pass   

##TESTS
def test_integer_validator_not_instantiatable():
    expected_error = "Can't instantiate abstract class IntegerValidator with abstract methods __init__"
    try:
        integer_validator = IntegerValidator()
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_integer_validator_can_instantiate_concrete():
    concrete_frame = ConcreteAbstractIntegerValidator()
    assert concrete_frame

def test_integer_validator_int():
    validator = ConcreteAbstractIntegerValidator()
    validator.validate_int(1)

def test_integer_validator_str():    
    validator = ConcreteAbstractIntegerValidator()
    assert validator.validate_int('1') == False

def test_integer_validator_float():    
    validator = ConcreteAbstractIntegerValidator()
    assert validator.validate_int(1.2) == False

def test_integer_validator_list():    
    validator = ConcreteAbstractIntegerValidator()
    assert validator.validate_int([1,2]) == False

