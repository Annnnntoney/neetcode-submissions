class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, num in enumerate(nums):
            remain = target - num
            if remain in dic:
                return [dic[remain], index]
            dic[num] = index
        
        return None