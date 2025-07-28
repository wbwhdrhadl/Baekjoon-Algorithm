# 입력받기
s = input()
n = int(input())


# 저장 배열 구현
arr = [[0] * 26 for _ in range(len(s))]

for i in range(len(s)):
    if i > 0:
        arr[i] = arr[i-1][:]   # 리스트 복사(얕은 복사 방지)
    c = s[i]
    idx = ord(c) - ord('a')
    arr[i][idx]+=1
    

# num_alpha 함수 구현
def num_alpha(alpha, start, end):
    idx = ord(alpha) - ord('a')
    if start > 0:
        print(arr[end][idx] - arr[start-1][idx])
    else:
        print(arr[end][idx])
    
for i in range(n):
    alpha, start, end = input().split()
    start = int(start)
    end = int(end)
    num_alpha(alpha, start, end)
    