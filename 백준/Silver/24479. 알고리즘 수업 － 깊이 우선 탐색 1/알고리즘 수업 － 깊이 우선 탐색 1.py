import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 증가
input = sys.stdin.readline

n, m, r = map(int,input().split())

# 그래프 만들기
graph = [[] for _ in range(n+1)]

# 그래프에 숫자 넣기
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 순서 정렬하기
for i in range(1, n+1):
    graph[i].sort()

# 방문 배열 만들기
visited = [0] * (n+1)
order = 1

# dfs 함수 만들기
def dfs(node):
    global order
    visited[node] = order
    for index in graph[node]:
        if visited[index] == 0:
            order+=1
            dfs(index)

    
# 루트부터 dfs 알고리즘 시작    
dfs(r)

# 최종 결과 출력
for i in range(1,n+1):
    print(visited[i])