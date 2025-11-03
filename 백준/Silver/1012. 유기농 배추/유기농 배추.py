import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,w,h):
    board[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == 1:
            dfs(nx,ny,w,h)
            
t = int(input())
for i in range(t):
    w,h,n = map(int,input().split())
    board = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(n):
        x,y = map(int,input().split())
        board[y][x] = 1
    size = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                size +=1
                dfs(x,y,w,h)
    print(size)
            
