i = 1
while i<=5:
    if (i ==3):
        break
    print(i)
    i+=1

i = 0
while i<=5:
    if (i == 3):
        i+=1
        continue
    print(i)
    i+=1

i = 0
while i<=20:
    if (i %2==0): #even
        i+=1
        continue
    print(i)
    i+=1