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
        if element is None:
            result.append(element)
        if isinstance(element, int):
            result.append(element)
        elif hasattr(element, '__iter__'):
            #check to see if it is of type list
            list_result = flatten_list(element) #recursive call
            for single_integer in list_result:
                result.append(single_integer)
    return result

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def serialize_tree(tree):
    """
  Serialize a tree from top to bottom, left to right to a list of values
  Args:
    a Tree object, each node has an integer value, and optionally have a left and right children, The tree is not ordered or balanced, it's just a binary tree
    example:
        1
       / \
      2   3
     / \ / \
       4 2
  Returns:
    a list of serialized values
    example: [1,2,3,None,4,2,None]

This is effectively a level order traversal -- we just need to keep track of which level we are on at each point and
make sure we are adding the leftmost element first
"""


    res = [] # this will be a list of lists!
    serialize_helper(tree, 0, res)
    return flatten_list(res[:-1])


def serialize_helper(root, level, result):
    if level >= len(result): # if we are seeing this level for the first time
        result.append([])
    if root == None:
        result[level].append(None)
    else:
        result[level].append(root.value)
        serialize_helper(root.left, level + 1, result)
        serialize_helper(root.right, level + 1, result)
    return

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
n4 = Node(4)
n2.right = n4
n2_right = Node(2)
print serialize_tree(n1)
