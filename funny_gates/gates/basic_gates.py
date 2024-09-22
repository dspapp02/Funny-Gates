def Identity_gate(list_of_bits):
    """
    Flexible gate. 
    Computes the identity operation for any number of bits. 
    
    Args:
        list_of_bits: List containing any number of integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The input to the gate.
    """
    return tuple(list_of_bits)


def NOT_gate(list_of_bits):
    """
    Fixed gate.
    Computes the NOT for a single bit
    
    Args:
        list_of_bits: List containing one integer (0 or 1). These is the input bit.
        
    Returns:
        int: The result of the NOT operation (0 or 1).
    """
    #Reminder for myself that built in gates only accept lists
    if isinstance(list_of_bits,int):
        raise ValueError("Remember that built in gates only accept lists")
        
    if list_of_bits == [0]:
        return 1
    elif list_of_bits == [1]:
        return 0
    

def NOTS_gate(list_of_bits):
    """
    Flexible gate.
    Computes the NOT operation on any number of bits.
    
    Args:
        list_of_bits: List containing any number of integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The input to the gate.
    """
    return tuple([NOT_gate([x]) for x in list_of_bits])


def AND_gate(list_of_bits):
    """
    Fixed gate. 
    Computes the AND operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the AND operation (0 or 1).
    """
    return list_of_bits[0]&list_of_bits[1]


def OR_gate(list_of_bits):
    """
    Fixed gate. 
    Computes the OR operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the OR operation (0 or 1).
    """
    return list_of_bits[0]|list_of_bits[1]


def XOR_gate(list_of_bits):
    """
    Fixed gate
    Computes the XOR operation for two binary inputs.
    
    Args:
        list_of_bits: List containing two integers (0 or 1). These are the input bits.
        
    Returns:
        tuple: The result of the XOR operation (0 or 1).
    """
    return list_of_bits[0]^list_of_bits[1]


