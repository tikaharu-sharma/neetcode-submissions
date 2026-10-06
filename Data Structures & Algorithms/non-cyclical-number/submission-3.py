class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            new_num = 0
            while n != 0:
                rem = n%10
                new_num += (rem**2)
                n = n//10
            if new_num == 1:
                return True
            if new_num in seen:
                return False
            seen.add(new_num)
            n = new_num
            