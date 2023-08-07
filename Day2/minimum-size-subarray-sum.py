class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0:
            return 0
        