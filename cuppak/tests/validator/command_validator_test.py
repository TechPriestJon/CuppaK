import pytest
from cuppak.validator.command_validator import CommandValidator

##SET UP
class ConcreteAbstractCommandValidator(CommandValidator):
    def __init__(self):
        pass   

##TESTS
def test_command_validator_not_instantiatable():
    expected_error = "Can't instantiate abstract class CommandValidator with abstract methods __init__"
    try:
        command_validator = CommandValidator()
        assert False
    except TypeError as error:
        assert str(error) == expected_error

def test_command_validator_can_instantiate_concrete():
    concrete_frame = ConcreteAbstractCommandValidator()
    assert concrete_frame

def test_command_validator_integer():
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command(1) == False

def test_command_validator_string():    
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command('1') == False

def test_command_validator_float():    
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command(1.2) == False

def test_command_validator_list():    
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command([1,2]) == False

def test_command_validator_command():    
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command(lambda x: x + 1) == True

def test_command_validator_another_command():    
    validator = ConcreteAbstractCommandValidator()
    assert validator.validate_command(command) == True

def command():
    print('command')