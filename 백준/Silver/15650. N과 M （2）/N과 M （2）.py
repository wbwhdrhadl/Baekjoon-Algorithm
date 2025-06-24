import sys
input = sys.stdin.readline
N, M = map(int,input().split())
visited = [False] * (N+1)
result = []

def recursion(start):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return

    for i in range(start,N+1):
        if visited[i]==False:
            visited[i]=True 
            result.append(i)
            recursion(i + 1)
            result.pop()
            visited[i]=False
     


recursion(1)