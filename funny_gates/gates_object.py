import funny_gates.gates.basic_gates as bg
import funny_gates.gates.advanced_gates as ag
import pandas as pd

class Gates:
    def __init__(self, func, inputs, outputs):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs
        
    def __call__(self,*args):
        return self.func(*args)
    
    @property
    def truth(self):
        numbers = [x for x in range(2**self.inputs)]
        bits = [format(i, f"0{self.inputs}b") for i in numbers]
        outputs = [self.func(x) for x in bits]
        
        
        truth_table = pd.DataFrame({
        'Inputs': bits,
        'Outputs': outputs})
        
        print(truth_table.to_string(index = False))
    
        
        
        
NOT = Gates(bg.NOT_gate,1,1)
AND = Gates(bg.AND_gate,2,1)
OR = Gates(bg.OR_gate,2,1)
XOR = Gates(bg.XOR_gate,2,1)
NOR = Gates(bg.NOR_gate,2,1)
NAND = Gates(bg.NAND_gate,2,1)
HA = Gates(ag.HA_gate,2,2)
FA = Gates(ag.FA_gate,3,2)
TOF = Gates(ag.TOF_gate,3,3)
