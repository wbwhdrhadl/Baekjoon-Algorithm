from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        x = queue.popleft()
        for nxt in graph[x]:
            if visited[nxt] == 0:
                visited[nxt] = -visited[x]
                queue.append(nxt)
            else:
                if visited[nxt] == visited[x]:
                    return False
    return True
    
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    is_binary = True
    visited = [0] * (V+1)    
    for i in range(1, V+1):
        if visited[i] == 0:
            if not bfs(i):
                is_binary = False
                break
    print("YES" if is_binary else "NO")