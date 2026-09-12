class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for c in range(len(s)):

            l, r = c, c
            #odd
            streak = 1
            l -= 1
            r += 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                streak += 2
                l -= 1
                r += 1
            
            if streak > len(longest):
                longest = s[l + 1:r]
            
            l, r = c, c + 1
            streak = 0
            #even
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                streak += 2
                l -= 1
                r += 1
            if streak > len(longest):
                longest = s[l + 1:r]

        return longest
                    
        