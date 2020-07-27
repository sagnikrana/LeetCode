class Solution(object):
    def reverse(self, x):
        """
        Given a 32-bit signed integer, reverse digits of an integer.

		Example 1:

		Input: 123
		Output: 321
		Example 2:

		Input: -123
		Output: -321
		Example 3:

		Input: 120
		Output: 21
		Note:
		Assume we are dealing with an environment which could only store integers
		within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
		of this problem, assume that your function returns 0 when the reversed
		integer overflows.
		
        :type x: int
        :rtype: int
        """
        x = int(x)
        if x < 0:
        	str_x = str(x)[1:len(str(x))]
        	new_num = -1  * int(str_x[::-1])
        else:
        	str_x = str(x)
        	new_num = 1  * int(str_x[::-1])
        
        if new_num > (2**31)-1 or new_num < -2 ** 31:
            return 0
        else:
            return new_num


if __name__ == '__main__':
	result = Solution.reverse(Solution,1534236469)
	print(result)