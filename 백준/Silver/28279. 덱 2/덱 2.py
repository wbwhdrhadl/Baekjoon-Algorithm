import sys
input=sys.stdin.readline
from collections import deque

deque = deque()
n = int(input())
for i in range(n):
    command = input().split()
    if(command[0] == "1"):
        x = command[1]
        deque.appendleft(x)
    elif(command[0] == "2"):
        x = command[1]
        deque.append(x)
    elif(command[0]=="3"):
        if(len(deque)>0):
            print(deque.popleft())
        else:
            print(-1)
    elif(command[0]=="4"):
        if(len(deque)>0):
            print(deque[-1])
            deque.pop()
        else:
            print(-1)
    elif(command[0]=="5"):
        print(len(deque))
    elif(command[0]=="6"):
        if(len(deque)==0):
            print(1)
        else:
            print(0)
    elif(command[0]=="7"):
        if(len(deque)>0):
            print(deque[0])
        else:
            print(-1)
    else:
        if(len(deque)>0):
            print(deque[-1])
        else:
            print(-1)
        