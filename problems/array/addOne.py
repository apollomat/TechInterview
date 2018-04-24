def addOne(l):
    for i in range(len(l) - 1, -1, -1):
        l[i] = (l[i] +  1) % 10
        if(l[i] != 0):
            return
    l[0] = 1
    l.append(0)
    return



if __name__ == "__main__":
    arr = [9]
    addOne(arr)
    print arr
