def removeElements(arr, removeInt):
    indx = 0

    for curr, value in enumerate(arr):
        if removeInt == value:
            continue
        else:
            arr[indx] = arr[curr]
            indx += 1
    return indx
