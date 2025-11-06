from collections import deque

m, n, h = map(int, input().split())

board = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    board.append(layer)

queue = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                queue.append((k, i, j))

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        h_, x, y = queue.popleft()
        
        for i in range(6):
            nh = h_ + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m:
                if board[nh][nx][ny] == 0:
                    board[nh][nx][ny] = board[h_][x][y] + 1
                    queue.append((nh, nx, ny))

bfs()

result = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0:
                print(-1)
                exit(0)
            result = max(result, board[k][i][j])

print(result - 1)
