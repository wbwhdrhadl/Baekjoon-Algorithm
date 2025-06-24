import sys
input = sys.stdin.readline
N, M = map(int,input().split())
result = []

def recursion(start):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return

    for i in range(start,N+1):
        result.append(i)
        recursion(i)
        result.pop()


recursion(1)