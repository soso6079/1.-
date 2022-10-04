#  곱셈 2022-10-04 실버 1
# https://www.acmicpc.net/problem/1629
# https://jjangsungwon.tistory.com/10
# https://bit.ly/3RssnEM
import sys

a, b, c = map(int, sys.stdin.readline().split())

def sol(a, b):
    if b == 1:
       return a % c
    else:
        temp = sol(a, b // 2)

        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

print(sol(a, b))