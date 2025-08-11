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
        if base == 0:
            return (0, 1, 0)
        elif base == -1:
            return (1, 0, 0)
        else:
            return (0, 0, 1)
            
    half = size//3
    m1,z1,o1 = count_paper(x,y,half)
    m2,z2,o2 = count_paper(x+half,y,half)
    m3,z3,o3 = count_paper(x+(2*half),y,half)
    m4,z4,o4 = count_paper(x,y+half,half)
    m5,z5,o5 = count_paper(x,y+(2*half),half)
    m6,z6,o6 = count_paper(x+half,y+half,half)
    m7,z7,o7 = count_paper(x+half,y+(2*half),half)
    m8,z8,o8 = count_paper(x+(2*half),y+half,half)
    m9,z9,o9 = count_paper(x+(2*half),y+(2*half),half)

    return (m1+m2+m3+m4+m5+m6+m7+m8+m9,z1+z2+z3+z4+z5+z6+z7+z8+z9,o1+o2+o3+o4+o5+o6+o7+o8+o9)
    
minus, zero, one = count_paper(0,0,n)
print(minus)
print(zero)
print(one)