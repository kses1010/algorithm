from collections import deque


class Solution:
    # 50분 투자한 직접 풀이
    def dailyTemperatures(self, t: [int]) -> [int]:
        list_f = []
        temp = deque()
        temp.append(t[0])

        if len(t) == 1:
            return list_f[0]

        for i in range(1, len(t)):
            if t[i] > max(t):
                list_f.append(0)
            else:
                temp.append(t[i])
                print(len(temp), i, temp)
                if temp[0] < t[i]:
                    temp.popleft()
                    list_f.append(len(temp))

        return list_f

    def daily_temperatures(self, T: [int]) -> [int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


sol = Solution()
t = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.daily_temperatures(t))

answers = [0] * len(t)
print(answers)
