def Identity_gate(*args):
    """
    Flexible gate. 
    Computes the identity operation for any number of bits. 
    
    Args:
        *args: A string, list or tuple containing a sequence of binary bits (0 or 1).
        
    Returns:
        tuple: The input to the gate.
    """
    return tuple(args)


def NOT_gate(a):
    """
    Fixed gate.
    Computes the NOT for a single bit
    
    Args:
        a: Integer (0 or 1).
        
    Returns:
        int: The result of the NOT operation (0 or 1).
    """

    if a == 0:
        return 1
    elif a == 1:
        return 0
    
def NOTS_gate(*args):
    """
    Flexible gate.
    Computes the NOT operation for an arbitrary number of binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of binary bits (0 or 1).
        
    Returns:
        tuple: The result of the NOT operation on each input bit.
    """
    return tuple([NOT_gate(x) for x in args])


def AND_gate(a,b):
    """
    Fixed gate. 
    Computes the AND operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of two binary bits (0 or 1).
        
    Returns:
        int: The result of the AND operation (0 or 1).
    """
    return a&b


def ANDS_gate(*args):
    """
    Flexible gate.
    Computes the AND operation for an arbitrary number of binary inputs. All inputs must be (1) to output (1).  
    
    Args:
        *args: A string, list or tuple containing a sequence of binary bits (0 or 1).
        
    Returns:
        tuple: The result of the AND operation for all input bits.
    """
    if all(x == 1 for x in args):
        return 1
    else: 
        return 0


def OR_gate(a,b):
    """
    Fixed gate. 
    Computes the OR operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of two binary bits (0 or 1).
        
    Returns:
        int: The result of the OR operation (0 or 1).
    """
    return a|b


def ORS_gate(*args):
    """
    Flexible gate.
    Computes the OR operation for an arbitrary number of binary inputs. Any input must be (1) to output (1).  
    
    Args:
        *args: A string, list or tuple containing a sequence of binary bits (0 or 1).
        
    Returns:
        tuple: The result of the OR operation for all input bits.
    """
    if any(x == 1 for x in args):
        return 1
    elif all(x == 0 for x in args): 
        return 0


def XOR_gate(a,b):
    """
    Fixed gate
    Computes the XOR operation for two binary inputs.
    
    Args:
        *args: A string, list or tuple containing a sequence of two binary bits (0 or 1).
        
    Returns:
        int: The result of the XOR operation (0 or 1).
    """
    return a^b


