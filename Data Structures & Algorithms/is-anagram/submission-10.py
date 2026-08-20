class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        instanceMapS = {}
        instanceMapT = {}

        for char in s:
            if char not in instanceMapS:
                instanceMapS[char] = 1
            
            else:
                instanceMapS[char] += 1
        
        for char in t:
            if char not in instanceMapT:
                instanceMapT[char] = 1
            
            else:
                instanceMapT[char] += 1

        return instanceMapS == instanceMapT