class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hmap = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            count = str(count)
            if count in hmap:
                hmap[count].append(word)
            else:
                hmap[count] = [word]
        return list(hmap.values())
        

        
        