import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global size
    board[x][y] = 0
    size += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            dfs(nx,ny)

res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            size = 0
            dfs(i,j)
            res.append(size)
            
res.sort()
print(len(res))
for r in res:
    print(r)
 