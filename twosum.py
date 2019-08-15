class Solution(object):
    def twoSum(self, nums, target):
        """
		Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:

        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
		
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
		
        for index,num in enumerate(nums):
            if num != "":
                for i in range(index+1, len(nums)):
                    if num + nums[i] == target:
                       return [index,i]
		
		
if __name__ == '__main__':
	result = Solution.twoSum(Solution, [-3,4,3,90], 0)
	print(result)