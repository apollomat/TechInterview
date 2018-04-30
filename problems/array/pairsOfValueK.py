# # Find all pairs with difference k
def findDiff(a, k):

    a = sorted(a)
    res = []
    l = 0
    r = 1
    while l < len(a) and r < len(a):
        if a[r] - a[l] < k:
            r += 1
        elif a[r] - a[l] > k:
            l += 1
        else:
            res.append([a[l], a[r]])
            l += 1
            r += 1

    return res


if __name__ == "__main__":
    a = [1, 4, 6, 7, 8, 10, 11, 14, 20]
    diff = 3
    print findDiff(a, diff)
    # print a[:end]
