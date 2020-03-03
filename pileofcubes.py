import math
def find_nb(m):
    flag = False
    sum=0
    for num in range(1,int(math.pow(m,1/3))):
        sum = sum + num**3
        if sum == m:
            flag = True
            break
        elif sum > m:
            flag=False
            break
    
    if flag==True:
        return int(num)
    else:
        return -1
