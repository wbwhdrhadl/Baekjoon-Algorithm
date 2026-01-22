import sys
input = sys.stdin.readline
from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    for i in vertex:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    visited = [False] * (n+1)
    distance = [0] * (n+1)

    count = 0
    queue = deque([1])
    visited[1] = True
    distance[1] = 0
    
    while queue:
        v = queue.popleft()

        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                distance[next_v] = distance[v] + 1
                queue.append(next_v)
    
    max_val = max(distance[1:])
    for i in range(1,n+1):
        if distance[i] == max_val:
            count+=1
            
    return count

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,vertex))
