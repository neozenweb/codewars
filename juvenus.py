def josephus(items,k):
    result =[]
    incr =1
    while len(items) > 1:
        temp =[]
        if(len(items) >= k):
            div =k
        else:
            div=2
            incr = 1
            print(items)
        for ctr,it in enumerate(items):
            if((ctr+incr)%div ==0) :
                result.append(it)
                temp.append(it)
        for res in temp:
               incr = len(items) - (items.index(res))
               del items[items.index(res)]   
        
    return result
        
