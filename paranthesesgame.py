def valid_parentheses(string):
    flag = False
    openpara = list(numb for numb,item in enumerate(string) if item=="(")
    closepara = list(numb for numb,item in enumerate(string) if item==")")
    data = zip(openpara,closepara)
    print(openpara,closepara)
    for item in data:
        print(item)
        if isinstance(item[0],int)and isinstance(item[1],int):
            if item[0] < item[1]:
                flag = True
            else:
                flag = False
                break
        else:
            flag=False
            break
    if len(openpara)==0 and len(closepara)==0:
        flag=True
    elif len(openpara)!= len(closepara):
        flag=False
    return flag
            
        
