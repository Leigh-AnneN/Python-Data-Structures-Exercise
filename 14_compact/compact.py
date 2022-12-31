def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # copy_lst= lst.copy()
    # falsey = ({}, [], (), 0, 0.0, "", None, False)
    # for element in copy_lst:
    #     if element in falsey: 
    #         element.remove()
    # return copy_lst

    return [val for val in lst if val]