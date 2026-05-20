class Twitter:

    def __init__(self):
        self.follow_dict = defaultdict(set)
        self.time = 0
        self.array = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.array.append([self.time, userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        i = 1
        maxheap = self.array[:]
        heapq.heapify_max(maxheap)

        res = []

        while i <= 10 and maxheap:
            time, userid, tweetid = heapq.heappop_max(maxheap)
            followers = self.follow_dict.get(userId, [])
            if userid == userId or userid in followers:
                res.append(tweetid)
                i = i+1
            
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dict[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_dict[followerId].discard(followeeId)
