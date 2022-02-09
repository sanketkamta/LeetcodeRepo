class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        index = 0
        direction = 1
        for i in s:
            res[index] += i
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction
        return ''.join(res)