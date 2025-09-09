import sys
import heapq
input = sys.stdin.readline

# 입력받기
n =int(input())
heap = []
for i in range(n):
    nums = list(map(int, input().split()))
    for i in nums:
        if len(heap) < n:
            heapq.heappush(heap,i)
        else:
            if i > heap[0]:
                heapq.heappushpop(heap,i)

print(heap[0])
