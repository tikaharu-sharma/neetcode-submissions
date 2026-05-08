class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = (target-position[i])/speed[i]
        cars = dict(sorted(cars.items(), key = lambda item:item[0], reverse = True))

        stack = []

        for item in cars:
            if stack and cars[item] <= stack[-1]:
                continue
            else:
                stack.append(cars[item])
        
        return len(stack)