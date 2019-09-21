class Solution:

    def return_longest_sequential(stra,strb):
        '''
        Returns the longest sequential substring in a given string
        '''
        stra = "abc"
        strb = "aabcd"
        indexes = []
        for item in stra:
            indexes.append(strb.index(item))
        
        result_indexes = []

        for ind,num in enumerate(indexes):
            if ind == len(indexes) - 1:
                break
            if abs(indexes[ind] - indexes[ind+1]) == 1:
                if ind == len(indexes) - 2:
                    result_indexes.append(ind)
                    result_indexes.append(ind+1)
                else:
                    result_indexes.append(ind)


        result = ""

        for item in result_indexes:
            result = result + strb[indexes[item]]

        return result

    def boldWords(self, words,S):

        """
        words: List[str], S: str
        return -> str
        Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

        The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

        For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

        Note:

        words has length in range [0, 50].
        words[i] has length in range [1, 10].
        S has length in range [0, 500].
        All characters in words[i] and S are lowercase letters.
        """


        
if __name__ == '__main__':
    # result = Solution.boldWords(Solution, ['flight','flow','flown'],"flightflowflown")
    result = Solution.return_longest_sequential("anik","sagnik")
    print(result)