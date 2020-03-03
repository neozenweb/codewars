def solution(roman):
    reference={
            'I':{'index': 0, 'value':1},
            'V':{'index': 1, 'value':5},
            'X':{'index': 2, 'value':10},
            'L':{'index': 3, 'value':50},
            'C':{'index': 4, 'value':100},
            'D':{'index': 5, 'value':500},
            'M':{'index': 6, 'value':1000}
        }
    total=reference.get(roman[0])['value']
    flag=True
    i=1
    while i <= len(roman)-1:
        ind = reference.get(roman[i-1])['index']
        nxt = reference.get(roman[i])['index']
        if(ind >= nxt):
            total = total + reference.get(roman[i])['value']
            i=i+1  
        else:
             total = total + reference.get(roman[i])['value'] - 2 *reference.get(roman[i-1])['value']
             i=i+1
    return total
