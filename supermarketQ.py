def queue_time(customers,n):
    if(len(customers) > 0):
        till=[]
        valnow=customers[0]
        toadd=0
        maxval=0
        for ind in range(len(customers)):
              print (ind%3, customers[ind])
              if(ind <n):
                  till.insert(ind,[customers[ind]])
              else:
                  for num in range(n):
                      valnow=sum(till[toadd])
                      if  sum(till[num]) < valnow:
                          print("current value is " +str(sum(till[num])))
                          valnow = sum(till[num])
                          toadd=num
                  print ("min is "+str(till[toadd]))
                  #till[ind%3].append(customers[ind])
                  till[toadd].append(customers[ind])
        print (till)
        for line in till:
            if sum(line) >maxval:
                maxval = sum(line)
        print (str(maxval))
    else:
        print(str(0))
