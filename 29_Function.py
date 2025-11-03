# Block of statement that perform a specific task.
def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(5,10)

def calc_sum(a,b): #parameter
    return a+b
sum = calc_sum(1,2) #functional call ; Arguments
print(sum)


def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal_avg(1,3,4)

def cal_prod(a,b):
    print(a*b)
    return a*b
cal_prod(2,3)