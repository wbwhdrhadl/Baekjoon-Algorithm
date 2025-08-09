import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().strip())) for i in range(n)]

def quard_tree(x,y,n):
    base = board[x][y]
    same = True
    for i in range(n):
        if same == False:
            break
        for j in range(n):
            if board[x+i][y+j] != base:
                same = False
                break

    if same == True:
        return str(base)

    half = n//2
    result1 = quard_tree(x,y,half)
    result2 = quard_tree(x,y+half,half)
    result3 = quard_tree(x+half,y, half)
    result4 = quard_tree(x+half,y+half, half)   

    return "("+result1+result2+result3+result4+")"

    





print(quard_tree(0,0,n))

    
             