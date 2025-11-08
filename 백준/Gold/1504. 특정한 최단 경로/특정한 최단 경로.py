import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost,next_node))

    return distance

dist1 = dijkstra(1)
dist2 = dijkstra(v1)
dist3 = dijkstra(v2)

path1 = dist1[v1]+dist2[v2]+dist3[N]
path2 = dist1[v2]+dist3[v1]+dist2[N]

result = min(path1,path2)

print(result if result<INF else -1)
    