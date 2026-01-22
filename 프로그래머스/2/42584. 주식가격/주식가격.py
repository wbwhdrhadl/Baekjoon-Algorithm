import sys
input = sys.stdin.readline
from collections import deque

def solution(prices):
    result = []
    queue = deque()
    for i in prices:
        queue.append(i)

    while queue:
        count = 0
        now = queue[0]
        queue.popleft()
        for num in queue:
            count += 1
            if now > num:
                break
        result.append(count)
    return result

prices = [1, 2, 3, 2, 3]	
answer = solution(prices)
print(answer)