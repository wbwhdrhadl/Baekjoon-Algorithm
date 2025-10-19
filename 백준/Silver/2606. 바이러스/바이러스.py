import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

visited = [0] * (n+1)
count = 0

def dfs(node):
    global count
    visited[node] = 1
    for index in graph[node]:
        # print(index)
        if visited[index] == 0:
            count+=1
            # print(f'카운트값은{count}')
            dfs(index)
    
dfs(1)

print(count)
