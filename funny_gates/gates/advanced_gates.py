from funny_gates.gates.basic_gates import AND_gate, OR_gate, XOR_gate, NOT_gate, NAND_gate, NOR_gate, input_checker

def HA_gate(*args):
    """
    Computes the Half-Adder operation for three binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list containing three integers.
        
    Returns:
        int: The result of the Half-Adder Operation; (Value, Carry).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
        
    return XOR_gate(inputs[0],inputs[1]),AND_gate(inputs[0],inputs[1])

def FA_gate(*args):
    """
    Computes the Full-Adder operation for two binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list/string containing three integers.
        
    Returns:
        int: The result of the Half-Adder operation; (Value, Carry).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)

    #checks length of input string
    if len(inputs)!=3:
        raise ValueError("Requires three (3) input bits")
        
    var1 = HA_gate(inputs[0],inputs[1])
    var2 = HA_gate(inputs[2],var1[0])
    var3 = OR_gate(var2[1],var1[1])
    
    return var2[0],var3


def TOF_gate(*args):
    """
    Computes the Classical Toffoli operation for three binary inputs. 
    Also knwon as a reversible AND gate. 
    
    Args:
        *args: Either three integers (0 or 1) or a single list containing three integers.
        
    Returns:
        int: The result of the Toffoli operation. If input c is zero, will return (a, b, AND(a,b)).
    """
    
    #checks that the inputs have a valid form
    inputs = input_checker(args)

    #checks length of input string
    if len(inputs)!=3:
        raise ValueError("Requires three (3) input bits")
        
    #Performs operation
    gate1 = AND_gate(inputs[0],inputs[1])
    gate2 = XOR_gate(gate1,inputs[2])
    
    return inputs[0],inputs[1],gate2