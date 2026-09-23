class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new_triplets = []

        for num1, num2, num3 in triplets:
            if num1 <= target[0] and num2 <= target[1] and num3 <= target[2]:
                new_triplets.append([num1, num2, num3])
        
        if not new_triplets:
            return False
            
        arr1 = [new_triplets[i][0] for i in range(len(new_triplets))]
        arr2 = [new_triplets[i][1] for i in range(len(new_triplets))]
        arr3 = [new_triplets[i][2] for i in range(len(new_triplets))]

        if max(arr1)==target[0] and max(arr2)==target[1] and max(arr3)==target[2]:
            return True
        return False