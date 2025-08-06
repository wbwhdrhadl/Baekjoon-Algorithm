s = input()

minus_split = s.split('-')
minus_sum = sum(map(int,minus_split[0].split('+')))

for group in minus_split[1:]:
    minus_sum-=sum(map(int,group.split('+')))

print(minus_sum)