class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        res1 = res

        for i in nums:
            res.append(i)
        return res + res1