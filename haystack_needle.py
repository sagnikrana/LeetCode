class Solution(object):
    def haystack_needle(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        flag = False

        if len(needle) > len(haystack):
        	return -1

        if haystack == '' or needle == '':
        	return 0

        for index,item in enumerate(haystack):
        	if item == needle[0]:
        		counter = 0
        		for next_index,target in enumerate(needle):
        			if index + next_index > len(haystack)-1:
        				return -1
        			if target == haystack[index+next_index]:
        				counter = counter + 1
        			else:
        				break
        		if counter == len(needle):
        			flag = True
        			return index

        if flag == False:
        	return -1

if __name__ == '__main__':
	result = Solution.haystack_needle(Solution,'mississippi','issipi')
	print(result)