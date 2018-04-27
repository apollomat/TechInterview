# input: sorted array with duplicates
def remove(a):
    start = 0
    for indx in range(len(a)):
        if a[indx] == a[start]:
            continue
        else:
            start += 1
            a[start] = a[indx]
    return start + 1

if __name__ == "__main__":
    a = [1,1,1,1,2,2,2,3,4,4,4,4,5,6,6,6]
    end = remove(a)
    print a[:end]
