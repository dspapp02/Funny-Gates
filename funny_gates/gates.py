def NOT(a):
    """Code snippet to define a NOT gate
    Requires a binary input"""
    inputs = a
    text = "a"
    
    if inputs not in (0,1):
        raise ValueError(f"Non-binary Input; {text} = {inputs}")
        
    if a == a-1:
        raise ValueError("You did it!")  
        
    if a == 0:
        return 1
    else:
        return 0


def AND(a,b):
    """Code snippet to define an AND gate
    Requires a binary input"""
    
    #Short snippet that checks the inputs are binary, and returns which input 
    #is a problem. This is reused in all gates. 
    inputs = [a,b]
    text = ["a","b"]
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
        
    return a&b


def OR(a,b):
    """Code snippet to define an OR gate
    Requires a binary input"""
    inputs = [a,b]
    text = ["a","b"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
        
    return a|b


def XOR(a,b):
    """Code snippet to define a XOR gate
    Requires a binary input"""
    inputs = [a,b]
    text = ["a","b"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
        
    return a^b


def NOR(a,b):
    """Code snippet to define a NOR gate
    Requires a binary input"""
    inputs = [a,b]
    text = ["a","b"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
    
    return NOT(OR(a,b))


def NAND(a,b):
    """Code snippet to define an NAND gate
    Requires a binary input"""
    inputs = [a,b]
    text = ["a","b"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
        
    return NOT(AND(a,b))


def HA(a,b):
    """Code snippet to define a Half-Adder gate
    Requires a binary input
    Returns (Value, Carry)"""
    inputs = [a,b]
    text = ["a","b"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
        
    return XOR(a,b),AND(a,b)


def FA(a,b,c):
    """Code snippet to define a Full-Adder gate
    Requires a binary input
    Returns (Value, Carry)"""
    inputs = [a,b,c]
    text = ["a","b","c"]
    
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
    
    var1 = HA(a,b)
    var2 = HA(c,var1[0])
    var3 = OR(var2[1],var1[1])
    
    return var2[0],var3


def TOF(a,b,c):
    """Code snippet to define a Toffoli gate; a reversible AND gate
    Requires a binary input
    If c = 0, returns (a,b,AND(a,b))"""
    
    #In general, the third ouput is XOR(c,AND(a,b))
    
    #also known as a CCNOT gate, as the outputs are always unchanged, unless
    #a and b are one, in which case c is flipped
    
    #Returns error for non-binary inputs
    inputs = [a,b,c]
    text = ["a","b","c"]
    for i in range(len(inputs)):
        if inputs[i] not in (0,1):
            raise ValueError(f"Non-binary Input; {text[i]} = {inputs[i]}")
    
    #Performs operation
    gate1 = AND(a,b)
    gate2 = XOR(gate1,c)
    
    return a,b,XOR(c,AND(a,b))