n, m = map(int,input().split())
name_see = set()
name_listen = set()

for i in range(n):
    name = input()
    name_see.add(name)

for i in range(m):
    name = input()
    name_listen.add(name)

answer = name_see & name_listen
answer = sorted(answer)
print(len(answer))
for name in answer:
    print(name)