import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a1 = []
for i in range(n):
    array1 = list(map(int,input().split()))
    a1.append(array1)

p,q = map(int,input().split())
    
a2 = []
for i in range(p):
    array2 = list(map(int,input().split()))
    a2.append(array2)

answer = [[0]*q for _ in range(n)]

# 분할 정복 계산
for i in range(n):
    for j in range(q):
        for k in range(m):
            answer[i][j] += a1[i][k] * a2[k][j]
# 출력
for row in answer:
    print(*row)
