from collections import deque

n = int(input())
moves = list(map(int,input().split()))

dq = deque((i+1,move) for i, move in enumerate(moves))

answer = []

while dq:
    index, move = dq.popleft()
    answer.append(index)

    if not dq:
        break

    if move > 0:
        dq.rotate(-(move-1))
    else:
        dq.rotate(-move)
    

print(' '.join(map(str,answer)))