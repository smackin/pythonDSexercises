def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    return list(set(l1) & set(l2))
    return list(set(l1) & set(l2))
    # sets remove duplicates.  so if you make each list a set, it would remove the duplicate.  Then you can return back to list().  


def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3


