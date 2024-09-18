from funny_gates.gates import basic_gates as bg
from funny_gates.gates import advanced_gates as ag

class Gates:
    def __init__(self, func, inputs, outputs):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
        
    def __call__(self,*args):
        return self.func(*args)
        
        
        
NOT = Gates(bg.NOT_gate,1,1)
AND = Gates(bg.AND_gate,2,1)
OR = Gates(bg.OR_gate,2,1)
XOR = Gates(bg.XOR_gate,2,1)
NOR = Gates(bg.NOR_gate,2,1)
NAND = Gates(bg.NAND_gate,2,1)
HA = Gates(ag.HA_gate,2,2)
FA = Gates(ag.FA_gate,3,2)
TOF = Gates(ag.TOF_gate,3,3)
