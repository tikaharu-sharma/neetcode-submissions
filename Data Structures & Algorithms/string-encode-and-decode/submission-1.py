class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            n = str(len(string))
            s = s + n + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        strs =[]
        while len(s)>0:
            i = 0
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            strs.append(s[i+1:i+1+length])
            s = s[i+1+length:]
        return strs


