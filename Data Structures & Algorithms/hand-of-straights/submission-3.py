class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        frequency = {}
        for num in hand:
            frequency[num] = frequency.get(num, 0) + 1

        hand.sort()
        for num in hand:
            if frequency[num] != 0:
                freq = frequency[num]
                for i in range(groupSize):
                    if (num+i) not in frequency or frequency[num+i] < freq:
                        return False
                    frequency[num+i] -= freq
        return True
