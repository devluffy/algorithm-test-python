import heapq

n = int(input())
h = []
ret = []

for _ in range(n):
    val = int(input())
    if( val != 0):
        heapq.heappush(h, val)
    else:
        if( len(h) == 0 ):
            ret.append(0)
        else:
            ret.append(heapq.heappop(h))

print("End")

for i in ret:
    print(i)
    