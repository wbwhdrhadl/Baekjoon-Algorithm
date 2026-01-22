from collections import deque
def solution(progresses, speeds):
    queue = deque()
    result = []
    
    for i in range(len(progresses)):
        day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        queue.append(day)
    
    now = queue.popleft()
    count = 1
    while queue:
        num = queue[0]
        if num <= now:
            count+=1
            queue.popleft()
            
        else:
            result.append(count)
            now = queue.popleft()
            count = 1

    result.append(count)
        
    return result