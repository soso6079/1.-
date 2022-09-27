#  바이러스 2022-09-25 BFS, DFS
#  https://www.acmicpc.net/problem/2606

import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = (map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [False for _ in range(n + 1)]


# no matter BFS or DFS
def bfs(graph, init):
    cnt = -1  # 시작 지점 제외
    q.append(init)

    while q:
        now = q.popleft()
        visited[now] = True
        cnt += 1

        for j in graph[now]:
            if not visited[j]:
                visited[j] = True
                q.append(j)

    return cnt

print(bfs(graph, 1))
