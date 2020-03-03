def persistence(n):
    ctr=0
    while len(str(n)) > 1:
        prod=1
        for i in range(len(str(n))):
            prod = prod * int(str(n)[i])
        n = prod
        ctr = ctr + 1
    return ctr
