import time
import psutil


def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB

    return rss
    # print(f"[{message}] memory usage: {rss: 10.5f} MB")


def my_solution(value):
    answer = value[0]
    k = value[-1]
    cnt = 0
    while True:
        if answer == 1:
            break
        if answer % k == 0:
            answer = answer / k
            cnt += 1
        else:
            answer -= 1
            cnt += 1
    return cnt


def optimal_solution(s):
    result = 0
    n = s[0]
    k = s[1]
    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1)
    return result


if __name__ == '__main__':
    print()
    use_before = memory_usage()
    start_time = time.time()
    ########################################################
    s = [25, 5]
    # k = [[7,3,1,8],[3,3,3,4]]
    # print(my_solution(s))
    # print(my_solution(k))
    print(optimal_solution(s))
    # print(optimal_solution(k))
    ########################################################
    end_time = time.time()
    use_after = memory_usage()
    print(f"[after_work] memory usage: {use_after-use_before: 10.5f} MB")
    print('[running time]:', end_time - start_time)
    print()
