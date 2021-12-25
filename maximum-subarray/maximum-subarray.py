class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = curmax = nums[0]
        for i in range(1, len(nums)):
            curmax = max(nums[i], curmax+nums[i])
            maxi = max(maxi, curmax)
        return maxi