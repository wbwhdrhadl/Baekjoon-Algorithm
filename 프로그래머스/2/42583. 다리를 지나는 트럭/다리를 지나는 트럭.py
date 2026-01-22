from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue_weight = deque(truck_weights)
    queue_move = deque([0]*bridge_length)
    
    total_time = 0
    total_weight = 0

    while queue_weight or total_weight > 0:
        total_time+=1
        
        out = queue_move.popleft()
        total_weight -= out
        
        if queue_weight and total_weight+queue_weight[0] <= weight:
            truck = queue_weight.popleft()
            queue_move.append(truck)
            total_weight+=truck
        else:
            queue_move.append(0)
    

    return total_time