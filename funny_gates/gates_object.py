import funny_gates.gates.basic_gates as bg
import funny_gates.gates.advanced_gates as ag
from funny_gates.helper_functions import input_checker
import pandas as pd

class Gates:
    """A class to represent a gate object. These simulate the actions of logic gates.

    A Gates object can be called with a tuple, list or string of bits as input and will return the output of the gate.

    Methods:
        inputs: Gets the number of input bits for a certain gate
        truth: Prints the truth table of a gate as a Pandas dataframe"""
    def __init__(self, func, inputs = None, outputs = None):
        """Initialises the Gates object.
        
        Args:
            func: The function that the gate will perform. This should be a Python function that takes a list of bits as input.
            inputs: The number of input bits for the gate. If the gate is flexible, this should be None.
            outputs: The number of output bits for the gate. If the gate is flexible, this should be None."""
        self.func = func
        self.fixed = inputs
                
    def __call__(self,*args): 
        """Calls the function of the gate object."""

        #checks the input format is valid and standardises to a list
        list_of_bits = input_checker(args)
        #checks that the correct number of bits are put as argument
        if not self.fixed == None:
            num_inputs = len(list_of_bits)
            if self.fixed!=num_inputs:
                raise ValueError(f"Gate requires ({self.fixed}) input bits")
        
        return self.func(list_of_bits)
    
    def inputs(self, *args):
        """Gets the number of input bits for a certain gate
        
        Args:
            *args: For fixed gates, no additional arguments are required.
            *args: For flexible gates, int for the number of input bits. 
        
        Returns:
            int: The number of input bits """ 
        #determines number of input bits
        if isinstance(self.fixed, int):   #if the gate is fixed
            num_bits = self.fixed
        elif self.fixed == None:          #if the gate is flexible
            if len(args) == 1:            #if the flexible gate has an argument
                num_bits = args[0]
            elif len(args) != 1 or not isinstance(args[0], int): #if the flexible gate has too many or too few arguments
                raise ValueError("Input validation failed: Flexible gates require the number of input bits to be specified as an integer.")
        else:                             #catch all for edge cases
            raise ValueError("Input validation failed: Ensure that fixed gates have no additional inputs, and flexible gates are provided with exactly one integer.")
        
        return num_bits
    
    def truth(self,*args):
        """Prints the truth table of a gate as a Pandas dataframe
        
        Args:
            *args: For fixed gates, no additional arguments are required.
            *args: For flexible gates, int for the number of input bits.
        
        Returns:
            Dataframe: Truth table for the specified gate.  """
        #determines number of input bits for flexible gates and fixed gates
        if self.fixed == None:
            if len(args) != 1 or not isinstance(args[0], int):
                raise ValueError("Input validation failed: Flexible gates require the number of bits to be specified as an integer.")
            num_bits = self.inputs(args[0])
        elif not self.fixed == None:
            num_bits = self.fixed

            
        #generates decimal values of all bits
        numbers = [x for x in range(2**num_bits)]
        #converts decimal to bit string
        bits = [format(i, f"0{num_bits}b") for i in numbers]
        #converts bit string to lists of bits
        bits_in_list = [[int(y) for y in x] for x in bits]
        #runs bit strings through gate
        outputs = [self.func(x) for x in bits_in_list]   
        
        
        truth_table = pd.DataFrame({
        'Inputs': bits,
        'Outputs': outputs})
        
        return truth_table
        
# Convert all Python functions to Gates objects  
Identity = Gates(bg.Identity_gate)
NOT = Gates(bg.NOT_gate,1,1)
NOTS = Gates(bg.NOTS_gate)
AND = Gates(bg.AND_gate,2,1)
OR = Gates(bg.OR_gate,2,1)
XOR = Gates(bg.XOR_gate,2,1)
NOR = Gates(ag.NOR_gate,2,1)
NAND = Gates(ag.NAND_gate,2,1)
HA = Gates(ag.HA_gate,2,2)
FA = Gates(ag.FA_gate,3,2)
TOF = Gates(ag.TOF_gate,3,3)
