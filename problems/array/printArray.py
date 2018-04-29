def printArray(arr):
    res = []
    for a in arr:
        if isinstance(arr, (list,)):
            for val in a:
                res.append(val)
        else:
            res.append(val)
    print res




a = [[], [1, 2, 3], [4, 5], [], [], [6, 7], [8], [9, 10], [], []]
printArray(a)
