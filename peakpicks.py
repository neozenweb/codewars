def pick_peaks(arr):
    peaks=[]
    pos=[]
    print(arr)
    for ind,elem in enumerate(arr):       
         if(ind > 0 and ind<len(arr)-1):
             flag = False
             if arr[ind-1] < elem and elem > arr[ind+1]:
                      flag=True
             elif arr[ind+1] == elem:
                 if(arr[ind-1] < elem and arr[ind+1:].count(elem)!= len(arr[ind+1:]) and arr[ind+1] >= arr[ind+2]):
                    flag=True
             
             
          
             if flag:
                 print(arr[ind-1],elem,arr[ind+1])
                 pos.append(ind)
                 peaks.append(elem)
        
    return {"pos":pos, "peaks" :peaks}
