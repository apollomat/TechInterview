def flatten_list(nested_list):
    # Essentially we want to loop through each element in the list
    # and check to see if it is of type integer or list
    """
      Flatten a arbitrarily nested list
      Args:
        nested_list: a nested list with item to be either integer or list
        example:
          [2,[[3,[4]], 5]]
      Returns:
        a flattened list with only integers
        example:
          [2,3,4,5]
    """

    result = []

    for element in nested_list:
        if isinstance(element, int):
            result.append(element)
        elif hasattr(element, '__iter__'):
            #check to see if it is of type list
            list_result = flatten_list(element) #recursive call
            for single_integer in list_result:
                result.append(single_integer)
    return result

nested_list =   [2,[[3,[4]], 5]]

print flatten_list(nested_list)
