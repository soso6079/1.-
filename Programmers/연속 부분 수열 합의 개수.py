# 2022-10-25 DP
# https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=python3
from itertools import combinations

def solution(elements):
    l = len(elements)
    elements.expand(elements)
    result = []
    for i in range(1, l+1):
        for j in range(l):
            result.append(sum(elements[j:i]))

    result = set(result)
    print(result)
    return 