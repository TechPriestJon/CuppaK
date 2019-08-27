from abc import ABC, abstractmethod

class CommandValidator(ABC):
    @abstractmethod
    def __init__():
        pass
        
    def validate_command(self, command_object):
        try:
            if callable(command_object):
                return True
            else:
                return False
        except:
            return False