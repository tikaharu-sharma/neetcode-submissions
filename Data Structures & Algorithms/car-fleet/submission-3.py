class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeHash = {}
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            timeHash[position[i]] = time

        stack = []
        position.sort(reverse=True)

        for pos in position:
            if not stack:
                stack.append(timeHash[pos])
                continue
            if timeHash[pos] > stack[-1]:
                stack.append(timeHash[pos])
        
        return len(stack)