import time
from collections import deque


def my_solution(graph):
    n, m = len(graph), len(graph[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        check = deque()
        check.append((x,y))

        while check:
            x, y = check.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue

                if graph[nx][ny] == 0:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    check.append((nx, ny))

        return graph[n - 1][m - 1]

    answer = bfs(0, 0)
    return answer

    # def dfs(x,y):

    #     if x<= -1 or x>= n or y <= -1 or y >=m:
    #         return False

    #     if graph[x][y] == 1:
    #         graph[x][y] = 0

    #         dfs(x+1,y)
    #         dfs(x,y+1)
    #         dfs(x-1,y)
    #         dfs(x,y-1)

    #         return True
    #     return False

    return answer


def optimal_solution(value):
    answer = 0

    return answer


if __name__ == '__main__':
    print()
    start_time = time.time()
    ########################################################
    s = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    # k = [[7,3,1,8],[3,3,3,4]]
    print(my_solution(s))
    # print(my_solution(k))
    # print(optimal_solution(s))
    # print(optimal_solution(k))
    ########################################################
    end_time = time.time()
    print('[running time]:', end_time - start_time)
    print()
