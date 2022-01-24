def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if b == a: 
        return "Numbers are Equal"
    if a > b: 
        return "First is Greater"
    else: 
        return "Second is Greater"