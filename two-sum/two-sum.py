class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi = {}
        for i in range(len(nums)):
            if nums[i] not in hashi:
                hashi[target - nums[i]] = i
            else:
                return hashi[nums[i]], i