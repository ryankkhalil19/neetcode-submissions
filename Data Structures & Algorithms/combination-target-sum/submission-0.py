class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(i, total):
            # Base Case 1: Found valid combination
            if total == target:
                res.append(combo.copy())
                return

            # Base Case 2: Overshot target or ran out of candidates
            if total > target or i >= len(nums):
                return

            # Choice 1: Include nums[i] (stay at i to allow unlimited reuse)
            combo.append(nums[i])
            backtrack(i, total + nums[i])

            # Choice 2: Do NOT include nums[i] (undo and move to i + 1)
            combo.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res