# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    l_button = [3, 0]
    r_button = [3, 2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            l_button[0], l_button[1] = (i // 3), 0
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            r_button[0], r_button[1] = (i // 3) - 1, 0
        else:
            if i == 0:
                i = 11
            middle = [i // 3, 1]
            l_dist = abs(middle[0] - l_button[0]) + abs(middle[1] - l_button[1])
            r_dist = abs(middle[0] - r_button[0]) + abs(middle[1] - r_button[1])
            # print("### i:", i, "### middle:", middle, "right_button", r_button, "left_button", l_button, (l_dist, r_dist))
            if l_dist < r_dist:
                answer += 'L'
                l_button = middle
            elif r_dist < l_dist:
                answer += 'R'
                r_button = middle
            else:
                if hand == 'right':
                    answer += 'R'
                    r_button = middle
                else:
                    answer += 'L'
                    l_button = middle

    return answer


numbers1, hand1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'
numbers2, hand2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'
numbers3, hand3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'
print(solution(numbers2, hand2))
