#  Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    TOTAL = 10
    buy = dict()
    answer = 0

    for idx, key in enumerate(want):
        buy[key] = number[idx]

    # 할인 목록에 사고 싶은 목록이 다 있는지 확인
    for key in buy.keys():
        if discount.count(key) < buy[key]:
            return 0

    for i in range(len(discount)):
        if (len(discount) - i) < TOTAL:
            break
        sufficient = False
        now = discount[i:i + TOTAL]

        for key in buy.keys():
            if now.count(key) < buy[key]:
                break
            if key == list(buy.keys())[-1]:
                sufficient = True
        if sufficient:
            answer += 1

    return answer
