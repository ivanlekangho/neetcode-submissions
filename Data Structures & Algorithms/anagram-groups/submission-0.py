class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {} # sorted -> list of anagrams
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagram:
                anagram[sorted_s] = []
            anagram[sorted_s].append(s)
        
        result = []
        for key in anagram:
            result.append(anagram[key])
        return result
