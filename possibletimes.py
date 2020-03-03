# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C, D):
    HH=[]
    MM=[]
    validtimes=[]
    givendigits=[str(A),str(B),str(C),str(D)]
    
    
    for ind,dig in enumerate(givendigits):
        for i in range(4):
            if ind != i:
                if int(dig+givendigits[i]) < 24:
                        HH.append(dig+givendigits[i])
                if int(dig+givendigits[i]) < 60:
                        MM.append(dig+givendigits[i])

    for hh in HH:
        for mm in MM:
        
            if hh[0] in mm or hh[1] in mm:
                    pass
            else:
                    validtimes.append(hh+":"+mm)
           

    return len(validtimes)
        