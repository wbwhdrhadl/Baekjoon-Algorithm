n = int(input())
answer = []

for i in range(n):
    age,name = input().split()
    age = int(age)
    answer.append((age,name))

answer = sorted(answer, key=lambda x:x[0])

for age,name in answer:
    print(age,name)