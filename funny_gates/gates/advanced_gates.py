from funny_gates.gates.basic_gates import AND_gate, OR_gate, XOR_gate, NOT_gate
from funny_gates.helper_functions import input_checker

# Gates that rely on the basic gates

def NOR_gate(list_of_bits):
    """
    Fixed gate.
    Computes the NOR operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the NOR operation (0 or 1).
    """
    return NOT_gate([OR_gate(list_of_bits)])

def NAND_gate(list_of_bits):
    """
    Fixed gate.
    Computes the NAND operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the NAND operation (0 or 1).
    """
    return NOT_gate([AND_gate(list_of_bits)])


def HA_gate(list_of_bits):
    """
    Fixed gate. 
    Computes the Half-Adder operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the Half-Adder Operation; (Value, Carry).
    """
    return XOR_gate(list_of_bits),AND_gate(list_of_bits)


def FA_gate(list_of_bits):
    """
    Fixed gate.
    Computes the Full-Adder operation for two binary inputs.
    
    Args:
        list_of_bits: List containing three integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the Half-Adder operation; (Value, Carry).
    """
    var1 = HA_gate([list_of_bits[0],list_of_bits[1]])
    var2 = HA_gate([list_of_bits[2],var1[0]])
    var3 = OR_gate([var2[1],var1[1]])
    
    return var2[0],var3


def TOF_gate(list_of_bits):
    """
    Fixed gate.
    Computes the Classical Toffoli operation for three binary inputs. 
    Also knwon as a reversible AND gate. 
    
    Args:
        list_of_bits: List containing three integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the Toffoli operation. If the input indexed as [2] is zero, will return (a, b, AND(a,b)).
    """
    
    #In general, the third ouput is XOR(c,AND(a,b))

    gate1 = AND_gate([list_of_bits[0],list_of_bits[1]])
    gate2 = XOR_gate([gate1,list_of_bits[2]])
    
    return list_of_bits[0],list_of_bits[1],gate2