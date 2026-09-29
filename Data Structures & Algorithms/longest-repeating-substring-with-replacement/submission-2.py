class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        char = {}

        for r in range(len(s)):
            char[s[r]] = char.get(s[r], 0) + 1
            if (r - l + 1) - max(char.values()) > k:
                char[s[l]] = char.get(s[l]) - 1
                l += 1
            res = max(r - l + 1,res)
        return res