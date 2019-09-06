class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.
        """
        s_list = list(s)
        tracker = []
        
        mapping = {'(':')', '{':'}','[':']'}
        if len(s_list) == 0:
            return True
        
        
        for i,bracket in enumerate(s_list):
            if i == 0 or len(tracker) == 0:
                tracker.append(bracket)
            else:
                if tracker[-1] in mapping:
                    if mapping[tracker[-1]] == bracket:
                        del tracker[-1]
                    else:
                        tracker.append(bracket)
            
        if len(tracker) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    result = Solution.isValid(Solution,"()[]{}")
    print(result)