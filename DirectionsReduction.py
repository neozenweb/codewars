def dirReduc(arr):
    index=0
    while index <= len(arr)-2:
        if (str(arr[index]).upper() == "NORTH" and str(arr[index+1]).upper()=="SOUTH") or (str(arr[index].upper()) == "SOUTH" and str(arr[index+1]).upper()=="NORTH"):
            del arr[index:index+2]
            index =0
        elif (str(arr[index]).upper() == "EAST" and str(arr[index+1]).upper()=="WEST") or (str(arr[index]).upper() == "WEST" and str(arr[index+1]).upper()=="EAST"):
            del arr[index:index+2]
            index=0
        else:
            index = index + 1
    return arr
            
    
