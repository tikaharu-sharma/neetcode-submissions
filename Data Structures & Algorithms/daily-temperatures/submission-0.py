class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)

        for j in range(1, len(temperatures)):
            while stack and temperatures[j] > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = j - i
            
            stack.append(j)
        
        while stack:
            i = stack.pop()
            result[i] = 0
        
        return result