import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int,input().split())) for _ in range(n)]

def count_paper(x,y,size):
    base = board[x][y]
    same = True

    for i in range(x,x+size):
        if not same:
            break
        for j in range(y,y+size):
            if board[i][j] != base:
                same = False
                break
    if same:
        return (1,0) if base == 0 else (0,1)

    half = size//2
    w1,b1 = count_paper(x,y,half)
    w2,b2 = count_paper(x,y+half,half)
    w3,b3 = count_paper(x+half, y, half)
    w4,b4 = count_paper(x+half, y+half, half)
    return (w1+w2+w3+w4, b1+b2+b3+b4)
    
white, blue = count_paper(0,0,n)
print(white)
print(blue)