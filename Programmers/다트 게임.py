# 2022-10-24 Implementation
# https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=python3

def solution(dartResult):
    option = ['*', '#']
    bonus = {'S': 1, 'D': 2, 'T': 3}
    score = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            score.append(int(dartResult[i]))
            if dartResult[i] == '0':
                if dartResult[i - 1] == '1':
                    score.pop()
                    score.pop()
                    score.append(10)
                    print(12543242345)

            continue

        if dartResult[i] in option:
            if dartResult[i] == '*':
                score[-1] = score[-1] * 2
                if len(score) == 1:  # 첫 번째일 때
                    continue
                else:
                    score[-2] = score[-2] * 2
            else:  # 아차상(#)일 때
                score[-1] -= 2 * score[-1]

        elif dartResult[i] in bonus.keys():
            score[-1] = score[-1] ** bonus[dartResult[i]]

    print(score)
    return sum(score)
