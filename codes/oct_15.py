## two dimensional array creating in python
n = int(input().strip())
two_dimensional_array = [[] for _ in range(n)]
print(two_dimensional_array)
print(len(two_dimensional_array))
for i in range(n):
    for j in range(5):
        two_dimensional_array[i].append(0)
print(two_dimensional_array)
lastAnswer = 0






