from funny_gates.helper_functions import input_checker

def all_inputs(num_bits):
    """Generate all input strings needed for a Pandas dataframe.
    
    Args:
        num_bits: The number of input bits. 
        
    Returns:
        list: All input bit combinations, stored as a string.
    """
    #generates decimal values of all bits
    numbers = [x for x in range(2**num_bits)]
    #converts decimal to bit string
    bits = [format(i, f"0{num_bits}b") for i in numbers]
    return bits


def minterm_generator(args):
    """
    Generate a minterm function for a given set of inputs.
    
    Args:
        *args: The binary inputs for the minterm.
        
    Returns:
        function: A function that takes binary inputs and returns the minterm output, for the previously passed as args.
    """
    args = input_checker(args)
    def minterm(*inputs):
        inputs = input_checker(*inputs)
        if inputs == args:
            return 1
        return 0
    return minterm


def SOP(inputlist,outputlist):
    """
    Generates a sum of products function from a list of inputs and outputs. Currently only supports one output.
    
    Args:
        inputlist: A list of binary inputs.
        outputlist: A list of binary outputs.
        
    Returns:
        function: A function that takes binary inputs and returns the output using the Sum of Products method.
    """ 

    inputs = tuple(input_checker(i) for i in inputlist)
    
    def allminterms(*args): 
        mintermtuple = tuple([minterm_generator(inputs[i])(*args) for i in range(len(outputlist)) if outputlist[i] == 1])
        
        return 1 if any(mintermtuple) == 1 else 0
    
    return allminterms


def frame_to_func(dataframe):
    """
    Convert a pandas dataframe containing to truth table to a function.
    
    Args:
        dataframe: A pandas dataframe containing the inputs and outputs of a binary operation.

    Returns:
        function: A function that takes a binary input and returns the output of the function.
    """
    inputlist = [dataframe.iloc[x, 0] for x in range(dataframe.shape[0])]
    outputlist = [dataframe.iloc[x, 1] for x in range(dataframe.shape[0])]
    
    return SOP(inputlist,outputlist)