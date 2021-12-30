class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = Counter(nums)
        return next(iter({k: v for k, v in sorted(b.items(), key=lambda item: item[1])}))