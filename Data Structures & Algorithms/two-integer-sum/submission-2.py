class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = nums
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == target:
                    return [min(i, j), max(i, j)]

            