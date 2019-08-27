from abc import ABC, abstractmethod

class ListValidator(ABC):
    @abstractmethod
    def __init__():
        pass
        
    def validate_list(self, list_object):
        try:
            if type(list_object) in [list, tuple, dict]:
                return True
            else:
                return False
        except:
            return False