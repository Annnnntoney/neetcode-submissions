class HitCounter:
    def __init__(self):
        self.times = [0] * 300   # 記錄這個 bucket 對應哪個 timestamp
        self.hits  = [0] * 300   # 記錄該 timestamp 的 hit 數

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.times[i] != timestamp:
            # 這個 bucket 是舊的，重置
            self.times[i] = timestamp
            self.hits[i] = 1
        else:
            self.hits[i] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            # 只計算還在 300 秒窗口內的 bucket
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
