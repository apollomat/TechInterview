'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = x ^ y # gives all bits that are different
        count = 0
        while res > 0:
            if res & 1:
                count += 1
            res = res/2

        return count
