from collections import deque

m,n = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

for j in range(m):
    for i in range(n):
        if board[i][j] == 1:
            queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))

bfs()

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result,board[i][j])

print(result - 1)
    