class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        result_list = []
        for index,num in enumerate(nums):
            if num in result_dict.keys():
                result_list.append(index)
                result_list.append(nums.index(result_dict[num]))
                return result_list
            else:
                result_dict[target-num] = num