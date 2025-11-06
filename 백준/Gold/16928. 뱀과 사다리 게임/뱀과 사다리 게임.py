from collections import deque

n,m = map(int,input().split())
ladder = {}
snake = {}

for i in range(n):
    x, y = map(int,input().split())
    ladder[x] = y

for j in range(m):
    u, v = map(int,input().split())
    snake[u] = v

def bfs(start):
    board = [0] * 101
    visited = [False] * 101
    queue = deque([start])
    visited[start] = True

    while queue:
        x = queue.popleft()
        
        if x == 100:
            return board[x]
        
        for i in range(1,7):
            nx = x + i

            if nx > 100:
                continue

            if nx in ladder:
                nx = ladder[nx]
            elif nx in snake:
                nx = snake[nx]

            if not visited[nx]:
                visited[nx] = True
                board[nx] = board[x] + 1
                queue.append(nx)
print(bfs(1))
