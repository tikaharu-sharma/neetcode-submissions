class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for op in operations:
            if op == "+":
                num = arr[-1]+arr[-2]
                arr.append(num)
            elif op == "D":
                num = arr[-1]*2
                arr.append(num)
            elif op == "C":
                arr.pop()
            else:
                arr.append(int(op))
        
        return sum(arr)
