class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = []
        for x in triplets:
            if x[0] == target[0] and x[1] <= target [1] and x[2] <= target[2]:
                ans.append(x)
            elif x[1] == target[1] and x[0] <= target[0] and x[2] <= target[2]:
                ans.append(x)
            elif x[2] == target[2] and x[1] <= target[1] and x[0] <= target[0]:
                ans.append(x)
        f = [0, 0, 0]
        for x in ans:
            f[0] = max(x[0], f[0])
            f[1] = max(x[1], f[1])
            f[2] = max(x[2], f[2])
        return f == target

        