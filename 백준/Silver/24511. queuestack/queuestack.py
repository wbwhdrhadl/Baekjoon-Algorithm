from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
m = int(input())
C = list(map(int,input().split()))

dq = deque()

# 큐인 자료만 배열에 넣기
for i in range(n):
    if A[i]==0:
        dq.append(B[i])

for i in range(m):
    dq.appendleft(C[i])
    print(dq.pop(), end=' ')
 