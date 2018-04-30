# move 0s to end of array, either in place or out of place
def moveZeros(a):
    indx = 0
    for i in xrange(len(a)):
        if a[i] != 0:
            a[indx] = a[i]
            indx += 1
    while indx < len(a):
        a[indx] = 0
        indx += 1
    return a


a = [5, 0, 3, 1, 0, 0, 3, 4, 5, 6]
print moveZeros(a)
