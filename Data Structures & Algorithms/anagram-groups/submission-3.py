class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char)-97] += 1
            key = tuple(arr)
            if key in hmap:
                hmap[key].append(word)
            else:
                hmap[key] = [word]
        
        output = []
        for key, value in hmap.items():
            output.append(value)
        
        return output