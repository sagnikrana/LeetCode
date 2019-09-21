class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        '''
        Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

        You can use each character in text at most once. Return the maximum number of instances that can be formed.
        '''
        
        balloon_dict = {}

        for item in set(str('balloon')):
            balloon_dict[item] = 0
        
        for item in text:
            if item in balloon_dict:
                balloon_dict[item] = balloon_dict[item]  + 1

        if balloon_dict['l'] != 0:
            balloon_dict['l'] = balloon_dict['l'] // 2

        if balloon_dict['o'] != 0:
            balloon_dict['o'] = balloon_dict['o'] // 2

        return sorted(balloon_dict.values())[0]



if __name__ == '__main__':
    result = Solution.maxNumberOfBalloons(Solution, "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw")
    print(result)