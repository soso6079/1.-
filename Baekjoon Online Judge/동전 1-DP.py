#  동전 1 2022-09-26 DP 골드 5
#  https://www.acmicpc.net/problem/2293
#  https://mong9data.tistory.com/68
'''
점화식을 못 세움
'''
import sys

coin = []
n, k = (map(int, sys.stdin.readline().split()))
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

d = [0] * (k+1)

d[0] = 1

for i in coin:
    for j in range(i, k+1):
        if j - i >= 0:
            d[j] += d[j-i]

print(d[k])
