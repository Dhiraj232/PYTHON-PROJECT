a  = 8
b = 12
max_value = max(a,b)
while True:
    if max_value %a ==0 and max_value%b==0:
        print(max_value)
        break
    max_value = max_value+1
