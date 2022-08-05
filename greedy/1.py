import time

# 20분 소요 (1번으로 풀었음)
def solution_1(a: list):
    # n, m, k = map(int, input('입력').split())
    # num_list = list(map(int, input().split()))
    #n = 숫자의 개수 / m = 총 더해지는 수 / k = 동일 숫자 반복 가능 횟수

    n, m, k = 5, 8, 3
    num_list = [2, 4, 5, 4, 6]

    num_list.sort()
    max_num = num_list[-1]
    cnt = 0
    answer = 0

    for i in range(m):
        if cnt > k:
            if max_num == num_list[-1]:
                max_num = num_list[-2]
            else:
                max_num = num_list[-1]
        answer += max_num
        cnt += 1

    # cnt = m // k
    # answer += (max_num*k*cnt) + (num_list[-2]*cnt)

    return answer


def solution_2(a: list):
    # n, m, k = map(int, input('입력').split())
    # num_list = list(map(int, input().split()))
    #n = 숫자의 개수 / m = 총 더해지는 수 / k = 동일 숫자 반복 가능 횟수

    n, m, k = 5, 8, 3
    num_list = [2, 4, 5, 4, 6]

    num_list.sort()
    max_num = num_list[-1]
    cnt = 0
    answer = 0

    # for i in range(m):
    #   if cnt > k:
    #     if max_num == num_list[-1]:
    #       max_num = num_list[-2]
    #     else:
    #       max_num = num_list[-1]
    #   answer += max_num
    #   cnt += 1

    cnt = m // k
    answer += (max_num * k * cnt) + (num_list[-2] * cnt)

    return answer


if __name__ == "__main__":
    start_time = time.time()
    print(solution_1([5, 8, 3]))
    end_time = time.time()
    print(f'소요 시간:{abs(end_time-start_time)}')

    start_time = time.time()
    print(solution_2([5, 8, 3]))
    end_time = time.time()
    print(f'소요 시간:{end_time-start_time}')
