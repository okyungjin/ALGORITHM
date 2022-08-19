# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3

from collections import deque

def solution(bridge_length, weight, truck_weights):
    q_trucks = deque(truck_weights)

    # init bridge
    first_truck = q_trucks.popleft()
    bridge = deque([first_truck])
    time = 1
    truck_cnt_on_bridge = 1
    weight_sum_on_bridge = first_truck
    
    while bridge:
        time += 1

        # all truck passed
        if truck_cnt_on_bridge == 0: break

        # last truck passes through the bridge
        if len(bridge) == bridge_length:
            last_truck = bridge.popleft()
            if last_truck != 0:
                weight_sum_on_bridge -= last_truck
                truck_cnt_on_bridge -= 1

        # new truck can be put on the bridge
        if q_trucks and weight_sum_on_bridge + q_trucks[0] <= weight:
            cur_truck = q_trucks.popleft()
            bridge.append(cur_truck)
            weight_sum_on_bridge += cur_truck
            truck_cnt_on_bridge += 1
        else:
            bridge.append(0)


    return time


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
