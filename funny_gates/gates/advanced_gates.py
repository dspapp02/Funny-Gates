from funny_gates.gates.basic_gates import AND_gate, OR_gate, XOR_gate, NOT_gate
from funny_gates.helper_functions import input_checker

# Gates that rely on the basic gates

def NOR_gate(*args):
    """
    Fixed gate.
    Computes the NOR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list/string containing two integers.
        
    Returns:
        tuple: The result of the NOR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    return NOT_gate(OR_gate(inputs[0],inputs[1]))

def NAND_gate(*args):
    """
    Fixed gate.
    Computes the NAND operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list/string containing two integers.
        
    Returns:
        tuple: The result of the NAND operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    return NOT_gate(AND_gate(inputs[0],inputs[1]))


def HA_gate(*args):
    """
    Fixed gate. 
    Computes the Half-Adder operation for three binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list/string containing three integers.
        
    Returns:
        tuple: The result of the Half-Adder Operation; (Value, Carry).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    return XOR_gate(inputs[0],inputs[1]),AND_gate(inputs[0],inputs[1])


def FA_gate(*args):
    """
    Fixed gate.
    Computes the Full-Adder operation for two binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list/string containing three integers.
        
    Returns:
        tuple: The result of the Half-Adder operation; (Value, Carry).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    var1 = HA_gate(inputs[0],inputs[1])
    var2 = HA_gate(inputs[2],var1[0])
    var3 = OR_gate(var2[1],var1[1])
    
    return var2[0],var3


def TOF_gate(*args):
    """
    Fixed gate.
    Computes the Classical Toffoli operation for three binary inputs. 
    Also knwon as a reversible AND gate. 
    
    Args:
        *args: Either three integers (0 or 1) or a single list/string containing three integers.
        
    Returns:
        tuple: The result of the Toffoli operation. If input c is zero, will return (a, b, AND(a,b)).
    """
    
    #In general, the third ouput is XOR(c,AND(a,b))
    
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    #Performs operation
    gate1 = AND_gate(inputs[0],inputs[1])
    gate2 = XOR_gate(gate1,inputs[2])
    
    return inputs[0],inputs[1],gate2