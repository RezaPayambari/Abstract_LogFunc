from LogFunc import LogFunc

class AndGate(LogFunc):
# Execute function will do the And between two boolean values
#
# @return
# True: when both given values are true.
# False: when any of the given values is False.
    def execute(self):
        if self.Input0 == True and self.Input1 == True:
            self._set_output(True)
        else:
            self._set_output(False)
