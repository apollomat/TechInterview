class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        dict_t = {}
        start = 0
        curr_max = 0
        for indx in range(len(s)):
            if s[indx] in dict_t: # if char is in there

                if dict_t[s[indx]] < start: # if the character currently isn't included
                    curr_max = max(curr_max, indx - start + 1)
                else: # if it is included, don't include it and start it at the next character
                    start = dict_t[s[indx]] + 1
            else:
                curr_max = max(curr_max, indx - start + 1)
            dict_t[s[indx]] = indx
        return curr_max
            
