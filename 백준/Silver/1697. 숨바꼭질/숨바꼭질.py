from collections import deque

def bfs(n,k):
    MAX = 100000

    graph = [0] * (MAX + 1)
    
    queue = deque([n])

    while queue:
        x = queue.popleft()
        
        if x == k:
            return graph[x]

        for nx in (x-1, x+1, 2*x):

            if 0<=nx<=MAX and graph[nx]==0:
                graph[nx] = graph[x]+1
                queue.append(nx)

n, k = map(int,input().split())
print(bfs(n,k)) 