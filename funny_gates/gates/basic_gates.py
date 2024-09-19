def input_checker(*args):
    """Used to determine the validity of the inputs into a gate"""
    args = args[0]
    #Checks that the arguments are of valid form
    if len(args) == 1 and isinstance(args[0], list):
        inputs = args[0]
    elif all(isinstance(x, int) for x in args):
        inputs = args
    elif len(args) == 1 and isinstance(args[0],str):
        inputs = [int(x) for x in args[0]]
    else:
        raise ValueError("Inputs must be integers or integers in list/string")
    
    #checks that the inputs are binary
    if any(x not in (0,1) for x in inputs):
        raise ValueError("All inputs must be binary (0 or 1)")
        
    return inputs

def Identity_gate(*args):
    """
    Computes the identity operation for a one bit gate
    
    Args:
        *args: Integer (0 or 1).
        
    Returns:
        int: The input to the gate.
    """
    #Checks that the arguments are of valid form
    if len(args) == 1 and isinstance(args[0], list):
        if len(args[0])!=1:
            raise ValueError("Requires one (1) input bits")
        inputs = args[0][0]
    elif len(args) == 1 and isinstance(args[0],int):
        if len(args)!=1:
            raise ValueError("Requires one (1) input bits")
        inputs = args[0]
    elif len(args) == 1 and isinstance(args[0],str):
        inputs = int(args[0])
    else:
        raise ValueError("Inputs must be integers or integers in list/string")
        
    #checks that inputs are binary
    if inputs not in (0,1):
        raise ValueError("All inputs must be binary (0 or 1)")
        
    #performs operation
    return inputs

def NOT_gate(*args):
    """
    Computes the NOT operation
    
    Args:
        *args: Integer (0 or 1).
        
    Returns:
        int: The result of the NOT operation (0 or 1).
    """
    #Checks that the arguments are of valid form
    if len(args) == 1 and isinstance(args[0], list):
        if len(args[0])!=1:
            raise ValueError("Requires one (1) input bits")
        inputs = args[0][0]
    elif len(args) == 1 and isinstance(args[0],int):
        if len(args)!=1:
            raise ValueError("Requires one (1) input bits")
        inputs = args[0]
    elif len(args) == 1 and isinstance(args[0],str):
        inputs = int(args[0])
    else:
        raise ValueError("Inputs must be integers or integers in list/string")
        
    #checks that inputs are binary
    if inputs not in (0,1):
        raise ValueError("All inputs must be binary (0 or 1)")
        
    #performs operation
    if inputs == 0:
        return 1
    else:
        return 0

def AND_gate(*args):
    """
    Computes the AND operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list containing two integers.
        
    Returns:
        int: The result of the AND operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
        
    return inputs[0]&inputs[1]


def OR_gate(*args):
    """
    Computes the OR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list containing two integers.
        
    Returns:
        int: The result of the OR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
        
    return inputs[0]|inputs[1]

def XOR_gate(*args):
    """
    Computes the XOR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list containing two integers.
        
    Returns:
        int: The result of the XOR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
        
    return inputs[0]^inputs[1]

def NOR_gate(*args):
    """
    Computes the NOR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list containing two integers.
        
    Returns:
        int: The result of the NOR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
    
    return NOT_gate(OR_gate(inputs[0],inputs[1]))

def NAND_gate(*args):
    """
    Computes the NAND operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list containing two integers.
        
    Returns:
        int: The result of the NAND operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
    
    #checks length of input string
    if len(inputs)!=2:
        raise ValueError("Requires two (2) input bits")
        
    return NOT_gate(AND_gate(inputs[0],inputs[1]))