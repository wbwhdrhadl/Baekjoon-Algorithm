from collections import deque

def solution(priorities, location):
    answer = 0
    count = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i],i])
    max_pri = max(map(lambda x: x[0], queue))
    while queue:
        now_num = queue[0]
        if now_num[0] == max_pri:
            count += 1
            queue.popleft()
            if queue:
                max_pri = max(map(lambda x: x[0], queue))
            if now_num[1] == location:
                return count
        else:
            queue.append(queue[0])
            queue.popleft()
    