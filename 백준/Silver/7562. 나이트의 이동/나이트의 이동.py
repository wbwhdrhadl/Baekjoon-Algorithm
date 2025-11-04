from collections import deque


moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
def bfs(l,nx,ny,fx,fy):
    
    graph = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    queue.append((nx,ny))

    while queue:
        x,y = queue.popleft()

        if x == fx and y == fy:
            return graph[fx][fy]
        
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    
t = int(input())
for i in range(t):
    l = int(input())
    nx,ny = map(int,input().split())
    fx,fy = map(int,input().split())
    print(bfs(l,nx,ny,fx,fy))
