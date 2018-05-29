from LogFunc import LogFunc

class OrGate(LogFunc):
# Execute function will do the And between two boolean values
#
# @return
# True: when both given values are true.
# False: when any of the given values is False.
    def execute(self):
        if self.Input0 == False and self.Input1 == False: 
            self._set_output(False) 
        else: 
            self._set_output(True) 

