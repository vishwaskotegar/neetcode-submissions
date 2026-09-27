class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        streak = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            
            curr = num
            length = 0
            while curr in numSet:
                length += 1
                curr += 1
            streak = max(streak, length)
        return streak