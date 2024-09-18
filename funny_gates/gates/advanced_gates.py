def HA_gate(*args):
    """
    Computes the Half-Adder operation for three binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list containing three integers.
        
    Returns:
        int: The result of the Half-Adder Operation; (Value, Carry).
    """
    
    #checks that inputs have the proper form
    if len(args) == 1 and isinstance(args[0], list):
        inputs = args[0]
    elif all(isinstance(x, int) for x in args):
        inputs = args
    else:
        raise ValueError("Inputs must be integers or integers in list")
        
    #checks the number of inputs
    if len(inputs)!=2:
        raise ValueError("Too many inputs")

    if any(x not in (0,1) for x in inputs):
        raise ValueError("All inputs must be binary (0 or 1)")
    return XOR_gate(inputs[0],inputs[1]),AND_gate(inputs[0],inputs[1])

def FA_gate(*args):
    """
    Computes the Full-Adder operation for two binary inputs.
    
    Args:
        *args: Either three integers (0 or 1) or a single list containing three integers.
        
    Returns:
        int: The result of the Half-Adder operation; (Value, Carry).
    """
    
    #checks that inputs have the proper form
    if len(args) == 1 and isinstance(args[0], list):
        inputs = args[0]
    elif all(isinstance(x, int) for x in args):
        inputs = args
    else:
        raise ValueError("Inputs must be integers or integers in list")
    
    #checks the number of inputs
    if len(inputs)!=3:
        raise ValueError("Too many inputs")

    #checks that inputs are binary
    if any(x not in (0,1) for x in inputs):
        raise ValueError("All inputs must be binary (0 or 1)")
        
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
    
    #In general, the third ouput is XOR(c,AND(a,b))
    
    #also known as a CCNOT gate, as the outputs are always unchanged, unless
    #a and b are one, in which case c is flipped
    
    #checks that inputs have the proper form
    if len(args) == 1 and isinstance(args[0], list):
        inputs = args[0]
    elif all(isinstance(x, int) for x in args):
        inputs = args
    else:
        raise ValueError("Inputs must be integers or integers in list")
        
    #checks the number of inputs
    if len(inputs)!=3:
        raise ValueError("Too many inputs")

    #checks that inputs are binary
    if any(x not in (0,1) for x in inputs):
        raise ValueError("All inputs must be binary (0 or 1)")
        
    #Performs operation
    gate1 = AND(inputs[0],inputs[1])
    gate2 = XOR(gate1,inputs[2])
    
    return inputs[0],inputs[1],gate2