class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        # for i in range(len(strs)):
        #     hash["".join(sorted(strs[i]))].append(strs[i])

        for s in strs: 
            hash["".join(sorted(s))].append(s)

        return list(hash.values())

        # output = []
        # for key, value in hash.items():
        #     output.append(value)
        # return output