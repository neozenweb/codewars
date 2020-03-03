# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(ranks):
    ranks.sort()
    reporting={}
    val=0
    for ind,rk in enumerate(ranks):
       if rk+1 in ranks:
           #reporting[rk+1].append(rk)
           if rk+1 in reporting:
               reporting[rk+1] +=1
           else:
               reporting[rk+1] = 1
    print(reporting)
    for elem in reporting:
        val += reporting[elem]
    return val
           
       