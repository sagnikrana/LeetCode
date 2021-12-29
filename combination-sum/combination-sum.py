class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def combination(remainder, combList, start):
            if sum(combList) == target or remainder == 0:
                if sorted(copy.deepcopy(combList)) not in result:
                    result.append(sorted(copy.deepcopy(combList)))
                return
            if remainder < 0:
                return

            for i in range(start, len(candidates)):
                combList.append(candidates[i])
                combination(remainder - candidates[i], combList, i)
                combList.pop()

        combination(copy.deepcopy(target), [], 0)
        return result