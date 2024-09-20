def flatten(item):
    """Helper function to recursively flatten any nested tuples or lists."""
    if isinstance(item, (list, tuple)):
        for sub_item in item:
            yield from flatten(sub_item)
    else:
        yield item
        
def input_checker(*args):
    """
    Determines the validity of the format and input of bits into a gate.
    
    Args:
        *args: Any number of binary integers (0 and 1) in a tuple, list, or string. 
        
    Returns:
        list: The input bits re-expressed as a single flat list
    """
    
    # Flatten the arguments into a single list
    inputs = list(flatten(args))
    
    # If the input format is a string, convert to list of integers
    if isinstance(inputs[0], str):
        inputs = [int(x) for x in inputs[0]]
    
    # Check that all inputs are binary integers
    if any(x not in (0, 1) for x in inputs):
        raise ValueError("All inputs must be binary (0 or 1)")
    
    return inputs