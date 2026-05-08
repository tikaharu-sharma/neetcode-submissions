class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hmap = {}
        for word in strs:
            w = str(sorted(word))
            if w in hmap:
                hmap[w].append(word)
            else:
                hmap[w] = [word]
        return list(hmap.values())
        

        
        