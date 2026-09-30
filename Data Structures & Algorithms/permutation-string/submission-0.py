class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Hash = {}
        s2Hash = {}

        for c in s1:
            s1Hash[c] = s1Hash.get(c, 0) + 1

        l = 0

        for r in range(len(s2)):
            
            s2Hash[s2[r]] = s2Hash.get(s2[r],0) + 1
            if (r - l + 1) > len(s1):
                s2Hash[s2[l]] -= 1
                if s2Hash[s2[l]] == 0:
                    del s2Hash[s2[l]]
                l += 1
            print(s1Hash, s2Hash)
            if s1Hash == s2Hash:
                return True
            
        return False