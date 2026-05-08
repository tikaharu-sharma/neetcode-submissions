class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        p1 = 0
        ans = []
        while p1 < len(num) - 2 and num[p1] <= 0:
            target = 0 - num[p1]
            p2 = p1 + 1
            p3 = len(num) - 1
            while p2 < p3:
                sum = num[p2] + num[p3]
                if sum > target:
                    p3 -= 1
                elif sum < target:
                    p2 += 1
                else:
                    ans.append([num[p1],num[p2],num[p3]])
                    p2 += 1
                    while num[p2] == num[p2-1] and p2<p3:
                        p2 += 1
            p1 += 1
            while p1 < len(num) - 1:
                if num[p1] == num[p1-1]:
                    p1 += 1
                else:
                    break
        return ans
