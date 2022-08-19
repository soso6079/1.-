# 20분 풀이 베낌
a = [1,3,1,5]

d = dict()
d[0] = a[0]
d[1] = max(a[1],a[0])
for i in range(2,len(a)):
    d[i] = max(d[i-1], d[i-2]+a[i])


    pass