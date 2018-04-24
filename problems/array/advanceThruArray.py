def advance(l):
    max_reach, n = 0, len(l)
    for i, x in enumerate(l):
        if max_reach < i: # if you cant reach this element
            return False
        if max_reach >= n - 1: # if you reached the last element or higher
            return True
        max_reach = max(max_reach, i + x)

    return False


if __name__ == "__main__":
    a = [3,3,1,0,2,0,1]
    b = [3,2,0,0,2,0,1]
    print advance(a)
    print advance(b)
