class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = list(s)
        y = list(t)
        for item in x:
             if item in y:
                y.remove(item)
        return y[0]