# 스도쿠 문제 풀기
import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(9)]

def is_valid(rows,cols,i):
    for N in range(9):
        if board[rows][N]==i:
            return False
    for M in range(9):
        if board[M][cols]==i:
            return False
    start_row = rows//3 * 3
    start_col = cols//3 * 3
    for N in range(3):
        for M in range(3):
            if board[start_row+M][start_col+N] == i:
                return False

    return True
    
# 스토쿠 백트래킹 함수
def solve():
    for rows in range(9): # 한 행을 기준으로 잡음
        for cols in range(9): # 한 열을 기준으로 잡음
            if board[rows][cols] == 0:
                for i in range(1,10):
                    if is_valid(rows, cols, i):
                        board[rows][cols]=i
                        if solve():
                            return True
                        board[rows][cols] = 0
                return False
    return True

solve()

for row in board:
    print(' '.join(map(str,row)))