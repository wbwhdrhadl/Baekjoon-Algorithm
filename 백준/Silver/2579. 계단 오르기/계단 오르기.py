n = int(input())
score = [0] * (n+1)
for i in range(1,n+1):
    score[i] = int(input())

max_score = [0] * (n+1)

if n>=1:
    max_score[1] = score[1]
if n>=2:
    max_score[2] = score[1] + score[2]
if n>=3:
    for i in range(3,n+1):
        max_score[i]= max(max_score[i-2] + score[i], max_score[i-3] + score[i-1] + score[i])
        


print(max_score[n])