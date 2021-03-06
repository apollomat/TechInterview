

def longest(str, k):
    dict_t = {}
    longest = 0
    start = 0
    # try to find the longest substring, so keep adding elements while you can
    for indx, char in enumerate(str):
        while len(dict_t) > k:
            if dict_t[str[start]] > 1:
                dict_t[str[start]] -= 1
            else:
                del dict_t[str[start]]
            start += 1

        longest = max(longest, indx - start + 1)
        if char not in dict_t:
            dict_t[char] = 0
        dict_t[char] += 1
    print longest

str = "abcadcacacaca"
k = 3
print longest(str, k)



a b c a b c
