for i in range(100,0,-1):
    print(i)

n = int(input("enter  a number"))
for i in range(1,11):
    print(i*n)

n = 5
sum=0
for i in range(1,n+1):
    sum+=i
    print("total sum=",sum)

n = 5
sum=0
i = 1
while i<=n:
    sum += i
    i += 1
    print("total sum=",sum)