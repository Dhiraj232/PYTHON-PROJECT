# Loop are used for sequential traversal.
veggitable= ["potato","ladysfinger","brinjal"]
for val in veggitable:
    print(val)

tup=(1,2,3,4,2,8,9)
for num in tup:
    print(num)

str= "apnacollege"
for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("END")