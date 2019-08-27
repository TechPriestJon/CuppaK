import pytest
from cuppak.validator.string_validator import StringValidator

##SET UP
class ConcreteAbstractStringValidator(StringValidator):
    def __init__(self):
        pass   

##TESTS
def test_string_validator_not_instantiatable():
    expected_error = "Can't instantiate abstract class StringValidator with abstract methods __init__"
    try:
        string_validator = StringValidator()
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_string_validator_can_instantiate_concrete():
    concrete_frame = ConcreteAbstractStringValidator()
    assert concrete_frame

def test_string_validator_integer():
    validator = ConcreteAbstractStringValidator()
    assert validator.validate_string(1) == False

def test_string_validator_string():    
    validator = ConcreteAbstractStringValidator()
    assert validator.validate_string('1') == True

def test_string_validator_another_string():    
    validator = ConcreteAbstractStringValidator()
    assert validator.validate_string('one') == True

def test_string_validator_float():    
    validator = ConcreteAbstractStringValidator()
    assert validator.validate_string(1.2) == False

def test_string_validator_list():    
    validator = ConcreteAbstractStringValidator()
    assert validator.validate_string([1,2]) == False

