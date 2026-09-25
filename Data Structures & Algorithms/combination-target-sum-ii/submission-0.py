class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combo = []

        def backtrack(i, total):
            # Base Case 1: Found valid combination
            if total == target:
                res.append(combo.copy())
                return

            # Base Case 2: Overshot target or ran out of candidates
            if total > target or i >= len(candidates):
                return

            # Decision 1: Take it
            combo.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            # Decision 2: Leave it
            combo.pop()
            while ((i < len(candidates) - 1) and candidates[i] == candidates[i + 1]):
                i += 1
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res