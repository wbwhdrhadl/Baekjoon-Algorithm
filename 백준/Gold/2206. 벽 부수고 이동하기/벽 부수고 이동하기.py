import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(): 
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while queue:
        x,y,broken = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken]+1
                    queue.append((nx,ny,broken))
                elif board[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[x][y][broken]+1
                    queue.append((nx,ny,1))

    return -1
print(bfs())
                