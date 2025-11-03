#Question
i=1
while i<=100: #stopping condition
    print(i)
    i+=1

#Question
i=100
while i>=1:
    print(i)
    i-=1

#Question
n=int(input("enter a number"))
i=1
while i<=10:
    print(n*i)
    i+=1

#Question
hero=["salman","AMIR","virat","Dhiraj"] #traverse

idx = 0
while idx<len(hero):
    print(hero[idx])
    idx+=1

#Question
nums= (1,4,9,16,25,36,49,81,100)
x=36
i= 0
while i<len(nums):
    if(nums[i]==x):
        print("Found at idx",i)
        i+=1