class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map = {}
        for i in range(len(s)):
            last_index_map[s[i]] = i
        
        res = []
        i = 0
        while i < len(s):
            size = 0
            last_index = last_index_map[s[i]]
            while i <= last_index:
                last_index = max(last_index, last_index_map[s[i]])
                i += 1
                size += 1
            res.append(size)

        return res
            
