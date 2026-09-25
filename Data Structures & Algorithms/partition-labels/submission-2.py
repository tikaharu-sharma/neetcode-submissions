class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_map = {}
        for i in range(len(s)):
            last_index_map[s[i]] = i
        
        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last_index_map[c])
            if i == end:
                res.append(end-start+1)
                start = i+1

        return res
            
