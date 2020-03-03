def alphabet_war():
    reinforces=["abcdefg","hijklmn"]
    airstrikes=["   *   ", "*  *   "]
    reinforces=["aaaaa","bbbbb", "ccccc", "ddddd"]
    airstrikes=["*", " *", "   "]
    
    reinforces=["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ]
    airstrikes=["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]

   
    
    '''
    def reinforcing(a):
         spaces =list(i for i,sp in enumerate(a) if sp==" ")
         for sp in spaces:           
             for numb,curr in enumerate(reinforces[1:],start=1):
                           if(curr[sp]=="*"):
                                continue
                           else:
                               a=a.replace(a[sp],curr[sp],1)
                               reinforces[numb]=reinforces[numb].replace(curr[sp],"*",1)
                               break
                    
         return a
    '''
    def reinforcing(a):
         rein =reinforces
        
         spaces =list(i for i,sp in enumerate(a) if sp==" ")
         flag = "N"
         print(a)
         print("spaces are  ")
         print(spaces)
         for spnum, sp in enumerate(spaces):
             print("Now doing for space " + str(sp))
                
             for numb,curr in enumerate(rein[1:],start=1):
                            if(curr[sp]=="&" ):
                            #if(sp <= len(curr)):
                           
                                 if(numb == len(rein) -1):
                                        a=a.replace(a[sp],"_",1)
                                 continue
                            
                            else:
                               #print("replacing    " + a[sp],curr[sp])
                               #print("selected reinf  " + curr)
                               a=a.replace(a[sp],curr[sp],1)
                               #reinforces[numb]=reinforces[numb].replace(curr[sp],"",1)
                               rein[numb]=rein[numb].replace(curr[sp],"&",1)
                               break
         #a = a.replace("_"," ")       
         return a
   

    def striking(inp):
       
        for stk, a in enumerate(airstrikes):
             for ind, elem in enumerate(a,start=0):
                     if elem=="*":
                        if ind >= 1 and ind < len(inp)-1:
                            inp =inp.replace(inp[ind-1]+inp[ind]+inp[ind+1],"   ",1)
                        elif ind == 0:
                            inp =inp.replace(inp[ind]+inp[ind+1],"  ",1)
                        elif ind == len(inp)-1:
                             inp =inp.replace(inp[ind-1]+inp[ind],"  ",1)
                     print("after striking      " + str(stk) + inp)
                     inp = reinforcing(inp)
                     print("after reinforcing   "  + inp)
        return inp

    backup = list(item for item in reinforces)
    result = striking(reinforces[0])
    result = result.replace(" ", "_")
    print("result is " +result)
