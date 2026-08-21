class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCountMap = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            charCountMap[tuple(count)].append(string)
        
        return list(charCountMap.values())