import sys
input = sys.stdin.readline
from collections import deque

queue = deque()

n = int(input())
for i in range(n):
    s = input().split()
    if(s[0] == "push"):
        x = int(s[1])
        queue.append(x)
    elif(s[0] == "pop"):
        if(len(queue)>0):
            print(queue.popleft())
        else:
            print(-1)
    elif(s[0] == "size"):
        print(len(queue))
    elif(s[0] == "empty"):
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif(s[0] == "front"):
        if(len(queue)>0):         
            print(queue[0])
        else:
            print(-1)
    elif(s[0] == "back"):
        if(len(queue)>0):
            print(queue[-1])
        else:
            print(-1)
        
        