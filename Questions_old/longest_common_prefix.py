class Solution(object):
    def longest_of_2(stra, strb):
        '''
        Helper function to find the lonest common prefix between the two strings
        '''
        len1 = len(stra)
        len2 = len(strb)
        stra = stra[0:min(len1, len2)]
        strb = strb[0:min(len1, len2)]
        flag = False
        result = ""
        for index, i in enumerate(stra):
            if len(stra) > 0:
                flag = True

            if index == 0:
                if stra[index] == strb[index] and flag == True:
                    result = i
            else:
                if stra[index] == strb[index] and len(result) > 0 and (index - stra.index(result[-1]) == 1) and flag == True:
                    result = result + i
        return result

    def longestCommonPrefix(self, strs):
        '''
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:

        Input: ["flower","flow","flight"]
        Output: "fl"
        '''
        if len(strs) > 1:
            sample= strs[0]
            res = {}
            for index, item in enumerate(strs):
                if index != 0:
                    # print(item)
                    from_func = self.longest_of_2(sample,item)
                    res[from_func] = len(from_func)
            print(res)
            return min(res.keys(), key=(lambda k: res[k]))
        else:
            if strs[0] == "":
                return ""
            else:
                return strs[0]

if __name__ == '__main__':
    result = Solution.longestCommonPrefix(Solution, ['flight','flow','flown'])
    print(result)