# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    sum_bridge = 0
    bridge_q = deque([0] * bridge_length)
    truck_q = deque(truck_weights)

    while bridge_q:
        time += 1
        sec_after_weight = bridge_q.popleft()
        sum_bridge -= sec_after_weight

        if truck_q:
            if sum_bridge + truck_q[0] <= weight:
                truck = truck_q.popleft()
                sum_bridge += truck
                bridge_q.append(truck)
            else:
                bridge_q.append(0)

    return time


bridge1, w1 = 2, 10
truck1 = [7, 4, 5, 6]
bridge2, w2 = 100, 100
truck2 = [10]
truck3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(bridge1, w1, truck1))
print(solution(bridge2, w2, truck2))
print(solution(bridge2, w2, truck3))
