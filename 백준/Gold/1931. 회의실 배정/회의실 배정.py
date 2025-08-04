# 회의실 개수 입력받기
n = int(input())

# 회의 시작시간, 종료시간
time = []
for i in range(n):
    s,e = map(int,input().split())
    time.append((s,e))
time.sort(key=lambda x: (x[1],x[0]))

# print(time)

# 회의실 최대 개수 구하기
count = 0
current = 0
for start,end in time:
    if start >= current:
        # print(start, end)
        current = end
        count+=1
print(count)
    