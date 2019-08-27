from abc import ABC, abstractmethod

class IntegerValidator(ABC):
    @abstractmethod
    def __init__():
        pass
        
    def validate_int(self, int_object):
        try:
            if int_object.is_integer():
                return True
            else:
                return False
        except:
            return False