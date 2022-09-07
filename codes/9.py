n = int(input())
sum = 0
for i in range(n):
    tmp = 1
    for j in range(i+1):
        tmp *= j+1
    sum += tmp
print(sum)