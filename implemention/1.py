import time
import psutil


def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB

    return rss
    # print(f"[{message}] memory usage: {rss: 10.5f} MB")


def my_solution(value):
    a = [1,2,3,4,5,6,7,8]
    b = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    b_key = {1:'a',2:'b',3:'c',4:'d',5:'e'}  
    h = b[value[0]]
    w = int(value[1])
    c = [(-2,-1),(-2,1),(2,-1),(2,1),
         (-1,-2),(-1,2),(1,-2),(1,2)]
    answer = 0 
    for i in c:
      if h + i[0] not in a:
        pass
      elif w + i[1] not in a:
        pass
      else:
        answer += 1 
        
    return answer


def optimal_solution(value):
	row = int(value[1])
	column = int(ord(value[0])) - int(ord('a')) + 1
	
	# 나이트가 이동할 수 있는 8가지 방향 정의
	steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
	
	# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
	result = 0
	for step in steps:
	    # 이동하고자 하는 위치 확인
	    next_row = row + step[0]
	    next_column = column + step[1]
	    # 해당 위치로 이동이 가능하다면 카운트 증가
	    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
	        result += 1
	
	return result


if __name__ == '__main__':
    print()
    use_before = memory_usage()
    start_time = time.time()
    ########################################################
    s = 'c2'
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
