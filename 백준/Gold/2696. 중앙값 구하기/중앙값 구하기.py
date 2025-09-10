import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    numbers = []

    # 수열 입력 받기
    while len(numbers) < M:
        numbers += list(map(int, input().split()))

    result = []
    max_heap = []  # 왼쪽 (최대 힙, 음수 저장)
    min_heap = []  # 오른쪽 (최소 힙)

    for i in range(M):
        num = numbers[i]

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # 정렬 조건 유지
        if min_heap and -max_heap[0] > min_heap[0]:
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)

        # 홀수번째 입력일 때만 결과 저장
        if i % 2 == 0:
            result.append(-max_heap[0])

    # 출력
    print(len(result))
    for i in range(0, len(result), 10):
        print(" ".join(map(str, result[i:i+10])))
