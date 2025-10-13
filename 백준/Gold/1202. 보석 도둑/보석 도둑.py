import sys, heapq
input = sys.stdin.readline  # ← 빠른 입력으로 변경

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort(key=lambda x: x[0])  # 보석 무게 기준 정렬
bags.sort()  # 가방 용량 정렬



total = 0
heap = []
idx = 0
for bag in bags:
    while idx<n and jewels[idx][0] <= bag:
        heapq.heappush(heap, -jewels[idx][1])
        idx +=1
    if heap:
        total += -heapq.heappop(heap)

print(total)
