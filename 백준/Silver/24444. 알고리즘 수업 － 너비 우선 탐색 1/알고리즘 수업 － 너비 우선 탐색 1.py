import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

# 방문 배열 
visited = [0] * (n+1)
order = 1

def bfs(start):
    global order
    queue = deque([start])
    visited[start] = order
    

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if visited[nxt] == 0:
                order += 1
                visited[nxt] = order
                queue.append(nxt) 
            
bfs(r)

for i in range(1,n+1):
    print(visited[i])
    
    