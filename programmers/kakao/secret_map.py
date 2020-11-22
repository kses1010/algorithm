#  비밀지도

def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        # 십진수를 2진수로 바꾸기 [2:0]을 통해 0b 삭제
        b_map = str(bin(decimal1 | decimal2))[2:]
        # 전체 길이가 n을 맞출 수 있도록 0을 추가하는 메서드 ex)11110 일 때 앞에 0을 붙여주어 지도 크기를 맞춰야한다.
        b_map = '0' * (n - len(b_map)) + b_map

        b_map = b_map.replace('1', '#')
        b_map = b_map.replace('0', ' ')
        answer.append(b_map)
    return answer


def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        b_map = bin(arr1[i] | arr2[i])[2:]
        answer.append(("0" * (n - len(b_map)) + b_map).replace("1", "#").replace("0", " "))
    return answer


n1, map1, map2 = 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
n2, map3, map4 = 6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]
print(solution(n1, map1, map2))
print(solution(n2, map3, map4))
