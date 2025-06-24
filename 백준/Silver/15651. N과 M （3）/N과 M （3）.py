import sys
input = sys.stdin.readline
N, M = map(int,input().split())
# visited = [False] * (N+1)
result = []

def recursion():
    if len(result) == M:
        print(' '.join(map(str,result)))
        return

    for i in range(1,N+1):
        # if visited[i]==False:
        # visited[i]=True 
        result.append(i)
        recursion()
        result.pop()
        # visited[i]=False


recursion()