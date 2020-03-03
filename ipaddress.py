def ips_between(start, end):
    stlist = start.split('.')
    endlist = end.split('.')
    stlist.reverse()
    endlist.reverse()
    ctr=0
    print(stlist)
    print(endlist)
    
    for i in range(4):
            ctr += (256 ** (i)) * (int(endlist[i]) - int(stlist[i]))
            print(ctr)
    return ctr
