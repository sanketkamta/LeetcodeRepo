class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i = 0
        j = len(height) - 1
        while i < j:
            res = (j - i) * min(height[i],height[j])
            if res > maxi:
                maxi = res
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return maxi