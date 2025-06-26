import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

# 총 3개의 visited 배열 사용
# 세로(열) visited 배열
cols=[False] * N
# 오른쪽 대각선 visited 배열
right=[False] * (2 * N - 1)
# 왼쪽 대각선 visited 배열
left=[False] * (2 * N -1)

# nqueen 백트랙킹 구현 
def nqueen(row):
    global cnt
    if row == N:
        cnt += 1
        return
        
    for i in range(N): # 한 행에 하나씩 말을 두기
        if cols[i]==False and right[i+row]==False and left[i-row+N-1]==False:
            cols[i]=True
            right[i+row]=True
            left[i-row+N-1]=True
            nqueen(row+1)
            cols[i]=False
            right[i+row]=False
            left[i-row+N-1]=False

nqueen(0)
print(cnt)