class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for i in range(len(strs)):
            hash["".join(sorted(strs[i]))].append(strs[i])

        output = []
        for key, value in hash.items():
            output.append(value)
        return output