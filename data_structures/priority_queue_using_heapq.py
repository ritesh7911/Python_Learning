import heapq

l = [1,2,4,10,11,2,3,100]


heapq.heapify(l)

print(l)
print(type(l))
print(heapq.heappop(l))
print(l)
max_value = -heapq.heappop(l)
print(max_value)
print(-heapq.heappop(l))

print(heapq)