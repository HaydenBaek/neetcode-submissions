class Twitter:

    def __init__(self):
        self.newsFeed = []
        self.followerList = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsFeed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        stackCopy = self.newsFeed.copy()
        result = []
        count = 0
        followSet = self.followerList[userId]
        while stackCopy and count < 10:
            personId, feedId = stackCopy.pop()

            if personId in followSet or personId == userId:
                result.append(feedId)
                count += 1
        
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)
