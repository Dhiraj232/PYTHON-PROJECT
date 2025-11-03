# When function call itself repeditially
# Recursion almost same in loops

#recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

#Recursion
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")
show(3)

#factorial recursion
def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(6))

