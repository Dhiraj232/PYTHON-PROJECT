#Question
cities=["delhi","mumbai","jalandhar","bettiah"]
heroes=["salman","Amir","ajay"]

def print_len(list):
    print(len(list))

print(len(cities))
print(len(heroes))

#Question
cities=["delhi","mumbai","jalandhar","bettiah"]
heroes=["salman","Amir","ajay"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()

#Question
def cal_fact(n):
    fact=1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)

#Question

def converter(USD_Val):
    inr_val=USD_Val*83
    print(USD_Val,"USD =", inr_val,"INR")
converter(20)