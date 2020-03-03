def bananas(s):
    comp=list("banana")
    inp = list(s)
    num=0
    output=[]
    final=""
    if 'banana' in ''.join(inp):
        for i in range(''.join(inp).index('banana')+6,len(inp)):
                    inp[i]='-'
    print (inp)
    for ind,char in enumerate(comp):
      flag=False
      
       
      for num,ch in enumerate(inp):
               
           if ch==char:
             if flag:
                  inp[num]='-'
             else:
                 flag=True
          
           else:
               flag = False
           
   
    
    
    final = ''.join(ltr for ltr in inp if ltr!='-')
    print (final)
   
    if final == 'banana':
        output.append(''.join(inp))
 
    return output

    
