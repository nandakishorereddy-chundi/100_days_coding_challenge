class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = n - 1
        while i >= 0:
            while i-1 >= 0 and nums[i] >= nums[i-1]:
                nums[i-1] += nums[i]
                i -= 1
            ans = max(ans, nums[i])
            i -= 1
        return ans