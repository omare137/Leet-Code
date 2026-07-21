class Solution:
    def longestPalindrome(self, s: str) -> str:
        pals = []
        longest=''
        pal=''
        for i in range(len(s)): 
            for j in range(i+1,len(s)):
                if s[i] != s[j]:
                    continue
                elif s[i]==s[j]:
                    pal = s[i:j+1]
                    if pal != pal[::-1]:
                        continue
                    else:
                        pals.append(pal)
        if not pals:
            return s[0]
        longest = max(pals, key=len)
        return longest