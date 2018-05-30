class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        vers1 = version1.split(".")
        vers2 = version2.split(".")


        counter = 0
        for value in zip(vers1, vers2):
            if int(value[0]) < int(value[1]):
                return -1
            elif int(value[0]) > int(value[1]):
                return 1
            counter += 1

        if len(vers2) > len(vers1):
            for value in vers2[counter: ]:
                if int(value) > 0:
                    return -1

        if len(vers1) > len(vers2):
            for value in vers1[counter:]:
                if int(value) > 0:
                    print value
                    return 1
        return 0
