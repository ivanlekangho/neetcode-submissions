class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts1 = {}
        counts2 = {}

        for char in s:
            if char not in counts1:
                counts1[char] = 0
            counts1[char] += 1

        for char in t:
            if char not in counts2:
                counts2[char] = 0
            counts2[char] += 1

        for key in counts1:
            if key not in counts2:
                return False
            if counts1[key] != counts2[key]:
                return False
            
        return True
        

        