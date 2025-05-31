from collections import deque

n,k = map(int,input().split())
queue = deque(range(1,n+1))

answer = []
while(len(queue)>=1):
    queue.rotate(-(k-1))
    num = queue[0]
    answer.append(num)
    queue.popleft()
    
print("<"+ ", ".join(map(str,answer)) + ">")