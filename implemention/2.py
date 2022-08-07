import time
import psutil


def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB

    return rss
    # print(f"[{message}] memory usage: {rss: 10.5f} MB")


def my_solution(map_size, s, map_list):
    answer = 0
    az = [0,1,2,3]  
    face = az.index(s[2])
    location_x = s[0] - 1
    location_y = s[1] - 1
    next_x = [-1, -1, 1, -1]
    next_y = [-1, 0, 1, -1]
    location = (location_a, location_b)

    cnt = 0
    while True:
        initial_face = face
        face = 0
        for i in range(4):
          face -= 1  #왼쪽으로 고개를 돌린다.
          check_x = location_x + next_x[az[face]]
          check_y = location_y + next_y[az[face]]

          if check_x <0 or check_y <0 or (map_list[check_x][check_y]==0) \
          or check_x > map_size[0]-1 or check_x > map_size[1]-1: #갈 수 없는 곳
            
            pass
          else:
            pass

        if check_x < 0 or check_y < 0 or 
      (map_list[check_x][check_y] == 0): #갈 수 없는 조건
            cnt+=1
            pass
        else:
            map_list[check_x][check_y]
            cnt = 0
            break

        if cnt == 4:
          next_x[]
          break
    return answer


# 2일차

# 그리디 알고리즘

## 3. 1이 될 때까지

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c16a9b2e-3f75-464a-a218-357e48286580/Untitled.png)

```python
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
```

나누어 떨어질 때까지 1을 빼고 나누어 떨어지면 `k`로 나눴다.

```python
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
```

최적 답안에서는 `N`이 `K`의 배수가 될때까지 1을 한번에 빼고 한번에 나눈다. 일일이 돌지 않기 때문에 훨씬 빠르게 해결할 수 있다.

문제풀이 소요시간: 4분

|  | 소요시간 | 메모리 사용량(MB) |
| --- | --- | --- |
| 내 답안_1 | 4.029273986816406e-05 | 0 |
| 최적 답안_1 | 0.0006425380706787109 | 0 |
| 내 답안_2 | 4.9114227294921875e-05 | 0 |
| 최적 답안_2 | 5.53131103515625e-05 | 0 |

# 구현

---

코딩 테스트에서 구현은 ‘머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정’이다. 즉 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 의미한다.

이 책에서는 완전 탐색, 시뮬레이션 유형을 모두 구현 유형이라고 표현한다.

**완전 탐색(Brute forcing)**은 모든 경우의 수를 주저 없이 다 계산하는 해결 방법을 말하고,

**시뮬레이션**은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형을 말한다.

1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
2. 특정 소수점 자리까지 출력해야 하는 문제
3. 문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트에 넣어야 하는(파싱을 해야 하는) 문제
4. N개의 원소가 들어있는 리스트에서 R개의 원소를 뽑아 한 줄로 세우는 모든 경우(순열)를 구해야 하는 문제

## 메모리 제약 사항

파이썬은 다른 언어들과 달리 자료형에 대한 깊은 이해가 있지 않아도 괜찮다. 다만 파이썬 역시 유효숫자에 따라 연산 결과가 원하는 값이 나오지 않을 수 있다는 것을 유념하자.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d06db3c6-2022-492a-ae75-e3c36899824f/Untitled.png)

데이터의 개수에 따른 메모리 사용량을 고려해서 메모리 제한을 고려해야 한다. 리스트를 여러 개 선언하고 그 중에서 크기가 1,000만 이상인 리스트가 있다면 메모리 용량 문제로 풀 수 없다는 것을 기억하자.(실제로 이정도 크기로 나올 일은 환경 문제 등으로 인해 잘 없다.)

## 시간 제약 사항

일반적으로 파이썬으로 코딩 테스트를 응시할 경우 제출한 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하면 크게 무리가 없다.

예를 들어, 시간 제한이 1초이고 데이터의 개수가 100만 개인 문제가 있다면 이는 $O(NlogN)$ 이내에 알고리즘을 이용하여 문제를 풀어야 한다. 실제로 $N=1,000,000$일 때 $Nlog_2N$은 약 20,000,000이기 때문이다.

## 구현 문제에 접근하는 방법

- 보통 구현 문제는 사소한 입력 조건 등을 문제에서 명시해주며 **문제의 길이**가 꽤 긴편이다.
- **PyPy3**는 파이썬3의 문법을 그대로 지원하며 파이썬보다 속도가 더 빠르다. PyPy를 지원한다면 꼭 선택하도록 하자.
- 파이썬 라이브러리를 적극 이용하자.
- 그리디와 크게 다르지 않게 느껴질 수 있다.

## 1. 왕실의 나이트

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68201fe3-24d7-4f92-84ff-36321079a9f4/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a59b832-da43-4afd-be4c-ed7203ff1c3e/Untitled.png)

```python
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
```

```python
def optimal_solution(a):
	row = int(a[1])
	column = int(ord(a[0])) - int(ord('a')) + 1
	
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
```

제한시간 20분을 넘겨서 풀어버렸다. 예제와 비슷한 유형임을 생각하고 문제를 풀었다. 이번 코드는 최적 답안보다 내 코드가 소요시간이 더 적었다. `ord`함수 때문인건지 이유는 잘 모르겠다. 

알파벳을 정수로 바꾸는걸 dict를 만들어서 직접 바꿨는데 최적 답안에서는 `ord`함수를 이용했다.

문제풀이 소요시간: 25분

## 2. 게임 개발

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/077db8e6-91cc-47ac-90d0-131086cf7fc2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac02f74f-206f-4503-bcd9-f4189045dec8/Untitled.png)

```python
def my_solution(map_size, s, map_list):
    answer = 0
    az = [0,1,2,3]  
    face = az.index(s[2])
    location_x = s[0] - 1
    location_y = s[1] - 1
    next_x = [-1, -1, 1, -1]
    next_y = [-1, 0, 1, -1]
    location = (location_a, location_b)

    cnt = 0
    while True:
        initial_face = face
        face = 0
        for i in range(4):
          face -= 1  #왼쪽으로 고개를 돌린다.
          check_x = location_x + next_x[az[face]]
          check_y = location_y + next_y[az[face]]

          if check_x <0 or check_y <0 or (map_list[check_x][check_y]==0) \
          or check_x > map_size[0]-1 or check_x > map_size[1]-1: #갈 수 없는 곳
            
            pass
          else:
            pass

        if check_x < 0 or check_y < 0 or 
      (map_list[check_x][check_y] == 0): #갈 수 없는 조건
            cnt+=1
            pass
        else:
            map_list[check_x][check_y]
            cnt = 0
            break

        if cnt == 4:
          next_x[]
          break
    return answer
```

```python
def optimal_solution():	
	# N, M을 공백을 기준으로 구분하여 입력받기
	n, m = map(int, input().split())
	
	# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
	d = [[0] * m for _ in range(n)]
	# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
	x, y, direction = map(int, input().split())
	d[x][y] = 1 # 현재 좌표 방문 처리
	
	# 전체 맵 정보를 입력받기
	array = []
	for i in range(n):
	    array.append(list(map(int, input().split())))
	
	# 북, 동, 남, 서 방향 정의
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]
	
	# 왼쪽으로 회전
	def turn_left():
	    global direction
	    direction -= 1
	    if direction == -1:
	        direction = 3
	
	# 시뮬레이션 시작
	count = 1
	turn_time = 0
	while True:
	    # 왼쪽으로 회전
	    turn_left()
	    nx = x + dx[direction]
	    ny = y + dy[direction]
	    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
	    if d[nx][ny] == 0 and array[nx][ny] == 0:
	        d[nx][ny] = 1
	        x = nx
	        y = ny
	        count += 1
	        turn_time = 0
	        continue
	    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
	    else:
	        turn_time += 1
	    # 네 방향 모두 갈 수 없는 경우
	    if turn_time == 4:
	        nx = x - dx[direction]
	        ny = y - dy[direction]
	        # 뒤로 갈 수 있다면 이동하기
	        if array[nx][ny] == 0:
	            x = nx
	            y = ny
	        # 뒤가 바다로 막혀있는 경우
	        else:
	            break
	        turn_time = 0
	
	# 정답 출력
	print(count)


if __name__ == '__main__':
    print()
    use_before = memory_usage()
    start_time = time.time()
    ########################################################
    size = [4,4]
    s = [1, 1, 0]
    map_list = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
    # k = [[7,3,1,8],[3,3,3,4]]
    print(my_solution(size,s,map_list))
    # print(my_solution(k))
    # print(optimal_solution(s))
    # print(optimal_solution(k))
    ########################################################
    end_time = time.time()
    use_after = memory_usage()
    print(f"[after_work] memory usage: {use_after-use_before: 10.5f} MB")
    print('[running time]:', end_time - start_time)
    print()
