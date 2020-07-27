class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        main_list = nums1 + nums2
        main_list = sorted(main_list)
        if len(main_list)%2 == 0:
            return (main_list[len(main_list)//2] + main_list[(len(main_list)//2) - 1]) / 2
        else:
            return main_list[(len(main_list)//2)]

if __name__ == '__main__':
    result = Solution.findMedianSortedArrays(Solution,[1,2],[3])
    print(result)