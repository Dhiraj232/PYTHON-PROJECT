# Question
movies=[]
mov=input("enter a movie")
movies.append(mov)

mov=input("enter a movie")
movies.append(mov)

mov=input("enter a movie")
movies.append(mov)

print(movies)

# wap to check a list a palindrome of element (hint: use copy())

# palindrome means is last position ya first position wiil same 

list1= [1,2,3]
list2= [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")


# Question
Grade= [1,3,6,8,9]
Grade.sort()
print(Grade)
