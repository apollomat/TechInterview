def shortestDistance(arr, word1, word2):
    word_pos = {}
    min_dist = 1000000

    for indx, word in enumerate(arr):
        if word == word1 and word2 in word_pos:
            min_dist = min(min_dist, indx - word_pos[word2])
        elif word == word2 and word1 in word_pos:
            min_dist = min(min_dist, indx - word_pos[word1])

        word_pos[word] = indx

    return min_dist




arr = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print shortestDistance(arr, word1,word2) #return 3
print shortestDistance(arr, "makes", "coding") # return 1
