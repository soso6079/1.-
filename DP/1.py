#35분 solved

x = int(input())

r = dict()
r[0] = 0
r[1] = 0
r[2] = 1
r[3] = 1
r[4] = 2

for i in range(2,x+1):
    r[i] = r[i - 1] + 1

    if i % 2 == 0:
        r[i] = min(r[i], r[i // 2] + 1)
    if i % 3 == 0:
        r[i] = min(r[i], r[i // 3] + 1)

answer = r[x]
print(answer)

