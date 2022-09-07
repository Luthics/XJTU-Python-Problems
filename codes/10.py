n = int(input())
sum = 0
for i in range(n):
    if((i+1) % 7 == 0 and (i+1) % 13 != 0):
        sum += i+1
print(sum)