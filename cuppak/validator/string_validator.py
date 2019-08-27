from abc import ABC, abstractmethod

class StringValidator(ABC):
    @abstractmethod
    def __init__():
        pass
        
    def validate_string(self, string_object):
        try:
            if isinstance(string_object, str):
                return True
            else:
                return False
        except:
            return False