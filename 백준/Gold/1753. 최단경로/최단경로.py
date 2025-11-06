import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost,next_node))

dijkstra(K)


for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else "INF")

        