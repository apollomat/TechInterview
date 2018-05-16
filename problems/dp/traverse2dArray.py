def traverse(size_x=5, size_y=5):
    arr = [[0 for y in range(size_y)] for x in range(size_x)]
    print arr

    for i in range(len(arr[0])):
        arr[0][i] = 1
    for j in range(len(arr)):
        arr[j][0] = 1

    for x in range(size_x)[1:]:
        for y in range(size_y)[1:]:
            arr[x][y] = arr[x-1][y] + arr[x][y-1]

    print arr[-1][-1]

print traverse()
