n = int(input())
answer = []

for i in range(n):
    word = input()
    answer.append(word)

answer = set(answer)
answer = sorted(answer, key=lambda x:(len(x),x))

for i in answer:
    print(i)