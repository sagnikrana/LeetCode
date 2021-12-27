class Solution(object):
    def __init__(self):
        self.result = {}
        
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return 1
        if (m - 1, n) in self.result:
            down = self.result[(m - 1, n)]
        else:
            down = self.result[(m - 1, n)] = self.uniquePaths(m - 1, n)
            
        if (m, n - 1) in self.result:
            right = self.result[(m, n - 1)]
        else:
            right = self.result[(m, n - 1)] = self.uniquePaths(m, n - 1)

        return down + right