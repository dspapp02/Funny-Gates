from funny_gates.gates.basic_gates import AND_gate, OR_gate, XOR_gate, NOT_gate
from funny_gates.helper_functions import input_checker

# Gates that rely on the basic gates

def NOR_gate(a,b):
    """
    Fixed gate.
    Computes the NOR operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of two binary bits (0 or 1).
        
    Returns:
        int: The result of the NOR operation (0 or 1).
    """
    return NOT_gate(OR_gate(a,b))

def NAND_gate(a,b):
    """
    Fixed gate.
    Computes the NAND operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of two binary bits (0 or 1).
        
    Returns:
        int: The result of the NAND operation (0 or 1).
    """
    return NOT_gate(AND_gate(a,b))


def HA_gate(a,b):
    """
    Fixed gate. 
    Computes the Half-Adder operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of three binary bits (0 or 1).
        
    Returns:
        tuple: The result of the Half-Adder Operation; (Value, Carry).
    """
    return XOR_gate(a,b),AND_gate(a,b)


def FA_gate(a,b,c):
    """
    Fixed gate.
    Computes the Full-Adder operation for three binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list/string containing three integers.
        
    Returns:
        tuple: The result of the Full-Adder operation; (Value, Carry).
    """
    var1 = HA_gate(a,b)
    var2 = HA_gate(c,var1[0])
    var3 = OR_gate(var2[1],var1[1])
    
    return var2[0],var3


def TOF_gate(a,b,c):
    """
    Fixed gate.
    Computes the Classical Toffoli operation for three binary inputs. 
    Also knwon as a reversible AND gate. 
    
    Args:
        *args: A string, list or tuple containing a sequence of three binary bits (0 or 1).
        
    Returns:
        tuple: The result of the Toffoli operation. If input c is zero, will return (a, b, AND(a,b)).
    """
    #In general, the third ouput is XOR(c,AND(a,b))

    #Performs operation
    gate1 = AND_gate(a,b)
    gate2 = XOR_gate(gate1,c)
    
    return a,b,gate2