#Given an array and an index, find the product of the elements of the array except the element at that index.


def product(arr):

    product = 1
    output = [1] * len(arr)
    for index in xrange(len(arr)):
        output[index] *= product
        product *= arr[index]
    product = 1
    for index in xrange(len(arr)-1,-1,-1):
        output[index] *= product
        product *= arr[index]

    print output



a = [5,6,1,2]
print product(a)
