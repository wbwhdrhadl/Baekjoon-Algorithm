def recursive(n):
    if n == 1:
        return ['*']
    
    prev = recursive(n // 3)
    result = []

    for row in prev:
        result.append(row * 3)
    for row in prev:
        result.append(row + ' ' * (n // 3) + row)
    for row in prev:
        result.append(row * 3)

    return result

n = int(input())
pattern = recursive(n)
for line in pattern:
    print(line)
