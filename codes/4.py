date=int(input("请输入年份："))
if(date%400==0): 
    print("YES")
elif(date%100==0): 
    print("NO")
elif(date%4==0):
    print("YES")
else: 
    print("NO")