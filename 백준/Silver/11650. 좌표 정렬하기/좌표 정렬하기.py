n = int(input())

answer = []
for i in range(n):
    x,y = map(int,input().split())
    answer.append((x,y))

sorted_answer = sorted(answer, key=lambda x:(x[0],x[1]))

for k,v in sorted_answer:
    print(k, v)
    