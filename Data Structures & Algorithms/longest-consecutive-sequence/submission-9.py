class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)

        for val in numsSet:
            if (val - 1) in numsSet:
                continue
            length = 1
            while (val + 1) in numsSet:
                length += 1
                val += 1
            longest = max(longest, length)

        return longest