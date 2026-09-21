class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0) + 1
        
        values = []
        for key, value in hash.items():
            values.append([value,key])

        values.sort()
        output = []
        while len(output) < k: 
            output.append(values.pop()[1])
        return output
