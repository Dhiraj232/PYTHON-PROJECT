#Question
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) +n
sum = calc_sum(5)
print(sum)

#Question
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]
print_list(fruits)
