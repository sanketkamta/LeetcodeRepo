class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if dic.get(n) is None:
                dic[n] = 1
            else:
                return True
        return False