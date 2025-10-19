import sys
input = sys.stdin.readline
from collections import deque

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]

visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
dfs_line = []
bfs_line = []

# 그래프에 넣기
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

# DFS 함수 구하기
def dfs(node):
    dfs_line.append(node)
    visited_dfs[node]=1
    for index in graph[node]:
        if visited_dfs[index] == 0:
            dfs(index)

# BFS 함수 구하기
def bfs(node):
    queue = deque([node])
    visited_bfs[node] = 1

    while queue:
        node = queue.popleft()
        bfs_line.append(node)
        for nxt in graph[node]:
            if visited_bfs[nxt] == 0:
                visited_bfs[nxt] = 1
                queue.append(nxt)

dfs(r)
print(' '.join(map(str,dfs_line)))
    
bfs(r)
print(' '.join(map(str,bfs_line)))