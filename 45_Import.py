import math
print(math.sqrt(16))


import math, random
print(math.factorial(5))
print(random.randint(1, 10))


# divisible_module.py

def check_divisible(num):
    if num % 5 == 0 and num % 11 == 0:
        print("Divisible by both 5 and 11")
    else:
        print("Not divisible by both 5 and 11")
