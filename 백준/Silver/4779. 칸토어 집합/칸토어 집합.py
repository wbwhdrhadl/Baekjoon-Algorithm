def recursive(lines):
    if len(lines) == 1:
        return lines
    
    third = len(lines)//3
    return recursive(lines[:third]) + ([' ']*third) + recursive(lines[third*2:])

try:
    while True:
        n = input()
        n = int(n)
        
        lines = ['-']*(3**n)
        result = recursive(lines)
        print(''.join(result))
except:
    pass
        