import funny_gates.gates.basic_gates as bg
import funny_gates.gates.advanced_gates as ag
from funny_gates.helper_functions import input_checker
import pandas as pd

class Gates:
    def __init__(self, func, inputs = None, outputs = None):
        self.func = func
        self.fixed = inputs
        #not entirely sure why self.__call__.__doc__ doesn't work
        self.__doc__ = func.__doc__ 
                    
    def __call__(self,*args):
        #checks the input format is valid and standardises to a list
        list_of_bits = input_checker(args)
        #checks that the correct number of bits are put in
        if not self.fixed == None:
            num_inputs = len(list_of_bits)
            if self.fixed!=num_inputs:
                raise ValueError(f"Gate requires ({self.fixed}) input bits")
        output = self.func(*list_of_bits)
        return output
    
    def inputs(self, *args):
        """Gets the number of input bits for a certain gate
        
        Args:
            *args: For fixed gates, no additional arguments are required.
            *args: For flexible gates, specify an input bit string. 
        
        Returns:
            int: The number of input bits """ 
        #determines number of input bits
        if isinstance(self.fixed, int):   #if the gate is fixed
            num_bits = self.fixed
        elif self.fixed == None:          #if the gate is flexible
            inputs = input_checker(args)
            num_bits = len(inputs)
        else:                             #catch all for edge cases
            raise ValueError("Input validation failed: Ensure that fixed gates have no additional inputs, and flexible gates are provided with an input bit string.")
        
        return num_bits
    
    def truth(self,*args):
        """Prints the truth table of a gate as a Pandas dataframe
        
        Args:
            *args: For fixed gates, no additional arguments are required.
            *args: For flexible gates, int for the number of input bits.
        
        Returns:
            Dataframe: Truth table for the specified gate.  """
        #determines the number of input bits differently based on flexible or fixed gates
        if not self.fixed == None:
            num_bits = self.fixed
        elif self.fixed == None:
            if len(args) != 1 or not isinstance(args[0], int):
                raise ValueError("Input validation failed: Flexible gates require the number of bits to be specified as an integer.")
            num_bits = args[0]

            
        #generates decimal values of all bits
        numbers = [x for x in range(2**num_bits)]
        #converts decimal to bit string
        bits = [format(i, f"0{num_bits}b") for i in numbers]
        #converts bit string to lists of bits
        bits_in_list = [(int(y) for y in x) for x in bits]
        #runs bit strings through gate
        outputs = [self.func(*x) for x in bits_in_list]   
        
        
        truth_table = pd.DataFrame({'Inputs': bits,'Outputs': outputs})
        
        return truth_table
        
# Convert all Python functions to Gates objects  
Identity = Gates(bg.Identity_gate)
NOT = Gates(bg.NOT_gate,1,1)
NOTS = Gates(bg.NOTS_gate)
AND = Gates(bg.AND_gate,2,1)
ANDS = Gates(bg.ANDS_gate)
OR = Gates(bg.OR_gate,2,1)
ORS = Gates(bg.ORS_gate)
XOR = Gates(bg.XOR_gate,2,1)
NOR = Gates(ag.NOR_gate,2,1)
NAND = Gates(ag.NAND_gate,2,1)
HA = Gates(ag.HA_gate,2,2)
FA = Gates(ag.FA_gate,3,2)
TOF = Gates(ag.TOF_gate,3,3)
