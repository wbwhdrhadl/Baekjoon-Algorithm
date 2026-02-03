from collections import Counter

def solution(clothes):
    total_count = 1
    clothes_dic = {}
    for i in range(len(clothes)):
        clothes_name, clothes_type = clothes[i]
        clothes_dic[clothes_type] = clothes_dic.get(clothes_type, 0) + 1
        
    for count in clothes_dic.values():
        total_count*=(count+1)
    return total_count-1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))