# 문자열 압축

def solution(s):
    answer = len(s)
    # 1개 단위(Step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        count = 1
        compressed = ''
        prev = s[:step]
        for i in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if s[i:i + step] == prev:
                count += 1
            # 다른 문자열이 나오면(압축 못할 시)
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                # 다시 상태 초기화
                prev = s[i:i + step]
                count = 1
        # 남아 있는 문자열에 대하여 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
