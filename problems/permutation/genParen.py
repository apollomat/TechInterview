
def makeParen(k=0, left=0, right=0, str=""):
    if left + right == k:
        print str
        return
    else:
        if left < k/2:
            makeParen(k, left + 1, right, str + "(")
        if right < left:
            makeParen(k, left, right + 1, str + ")")



def paren(value):
    return makeParen(value*2, 0, 0, "")


print paren(2)
