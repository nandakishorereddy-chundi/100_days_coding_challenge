class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import Counter
        f = {}
        for i, e in enumerate(nums):
            if e in f:
                f[e].append(i)
            else:
                f[e] = [i]
        for e in f:
            if target-e in f:
                if target-e == e and len(f[e]) > 1:
                    ans = [f[e][0], f[e][1]]
                    return ans
                elif target-e != e:
                    ans = [f[e][0], f[target-e][0]]
                    return ans