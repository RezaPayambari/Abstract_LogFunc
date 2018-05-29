from AndGate import AndGate
from OrGate import OrGate
from NandGate import NandGate

#AndGate
n=AndGate(True,False,"AndGate")

n.execute()
n.showInfo()

#OrGate
o=OrGate(False,True,"OrGate")

o.execute()
o.showInfo()

#NandGate

nand=NandGate(True,True,"NandGate")

nand.execute()
nand.showInfo()
