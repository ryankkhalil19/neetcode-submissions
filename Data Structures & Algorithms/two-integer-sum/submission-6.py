class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in valMap:
                return [valMap[difference], i]
            valMap[nums[i]] = i
            
