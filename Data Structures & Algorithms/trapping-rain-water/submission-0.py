class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 2:
            return 0
            
        prefix = [0]
        suffix = [0] * len(height)

        max_prefix = 0
        max_suffix = 0
        for num in height:
            max_prefix = max(max_prefix, num)
            prefix.append(max_prefix)
        prefix.pop()

        for i in range(len(height)-2, -1, -1):
            max_suffix = max(max_suffix,height[i+1])
            suffix[i] = max_suffix
        total_area = 0
        for i in range(len(height)):
            area = min(suffix[i],prefix[i]) - height[i]
            if area >= 0:
                total_area += area
        return total_area
