class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
    
        heapq.heapify(sticks)   # 變成 min-heap，最小值永遠在頂端
        cost = 0
        
        while len(sticks) > 1:
            a = heapq.heappop(sticks)  # 取最小
            b = heapq.heappop(sticks)  # 取次小
            cost += a + b
            heapq.heappush(sticks, a + b)  # 合併後放回去
        
        return cost