class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for val in nums:
            if val in uniqueSet:
                return True
            uniqueSet.add(val)

        return False
            