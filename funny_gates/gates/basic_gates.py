from funny_gates.helper_functions import input_checker

def Identity_gate(*args):
    """
    Flexible gate. 
    Computes the identity operation for any number of bits. 
    
    Args:
        *args: Any number of integers (0 and 1) or a single list/string containing these integers. 
        
    Returns:
        tuple: The input to the gate.
    """
    inputs = input_checker(args)
        
    return tuple(inputs)


def NOT_gate(*args):
    """
    Fixed gate.
    Computes the NOT for a single bit
    
    Args:
        *args: Integer (0 or 1).
        
    Returns:
        int: The result of the NOT operation (0 or 1).
    """
    inputs = input_checker(args)
    #performs operation
    if inputs == [0]:
        return 1
    elif inputs == [1]:
        return 0
    

def NOTS_gate(*args):
    """
    Flexible gate.
    Computes the NOT operation on any number of bits.
    
    Args:
        *args: Any number of integers (0 and 1) or a single list/string containing these integers. 
        
    Returns:
        tuple: The input to the gate.
    """
    inputs = input_checker(args)
        
    return tuple([NOT_gate(x) for x in inputs])


def AND_gate(*args):
    """
    Fixed gate. 
    Computes the AND operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list/string containing two integers.
        
    Returns:
        tuple: The result of the AND operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    return inputs[0]&inputs[1]


def OR_gate(*args):
    """
    Fixed gate. 
    Computes the OR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list/string containing two integers.
        
    Returns:
        tuple: The result of the OR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    return inputs[0]|inputs[1]


def XOR_gate(*args):
    """
    Fixed gate
    Computes the XOR operation for two binary inputs.
    
    Args:
        *args: Either two integers (0 or 1) or a single list/string containing two integers.
        
    Returns:
        tuple: The result of the XOR operation (0 or 1).
    """
    #checks that the inputs have a valid form
    inputs = input_checker(args)
        
    return inputs[0]^inputs[1]


