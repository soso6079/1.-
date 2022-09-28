#  Level2
#  https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3
from collections import deque
import sys


q1 = sys.stdin.readline().split(',')
q1[-1] = q1[-1][:-3]

q2 = sys.stdin.readline().split(',')
q1 = (map(int, q1))
q2 = (map(int, q2))

print(q1, q2)
def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)

    q1_s = sum(q1)
    q2_s = sum(q2)
    total = q1_s + q2_s
    cnt = 0
    if total % 2 != 0:
        return -1

    for _ in range(100):
        if q1_s > q2_s:
            num = q1.popleft()
            q2.append(num)
            q1_s -= num
            q2_s += num

        elif q1_s < q2_s:
            num = q2.popleft()
            q1.append(num)
            q2_s -= num
            q1_s += num
        elif q1_s == q2_s:
            break
        else:
            cnt += 1
    return cnt

print(solution(q1, q2))