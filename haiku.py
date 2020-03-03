def is_haiku(text):
    data=[]
    vowels=['a','e','i','o','u']
    for num,line  in enumerate(text.splitlines()):
              line = line.lower()
              counter=0
              for ind,varcomp in enumerate(list(line)):
                  if ind >0 and varcomp in vowels and list(line)[ind-1] not in vowels:
                      counter += 1
                       
                  if ind ==0 and varcomp in vowels:
                      counter+=1
                       
                  if varcomp=='e' and ind < len(list(line))-1 and (list(line)[ind+1].isalpha()==False )and list(line)[ind-1] in ['l','k','y','m','c','g','d','r','s','p','b','f','n','j','t','v','w','x','z']:
                      counter -=1
                       
                  
                  if varcomp=='e' and ind == len(list(line))-1 and list(line)[ind-1] not in vowels:
                      counter -=1
                       
                  if varcomp=='y' and (ind > 0 and ind <len(list(line)) -1) and (list(line)[ind-1].isalpha()==True or list(line)[ind+1].isalpha()==False) and list(line)[ind-1] not in vowels and list(line)[ind+1] not in vowels:
                 
                      counter +=1
                      
                  if varcomp=="y" and ind==0 and list(line)[ind+1].isalpha()==False:
                      counter+=1
                  if varcomp=='y' and ind < len(list(line))-1 and (list(line)[ind+1] in vowels)and (list(line)[ind-1] in vowels):
                      counter -=1
                       
                  if varcomp=="y" and ind==len(list(line))-1 and list(line)[ind-1].isalpha()==True and list(line)[ind-1] not in vowels:
                      counter+=1
                  
                       
                       
              data.append(counter)
    for i in range(0,len(data),3):
        if data[i:i+3]==[5,7,5]:
            return True
        else:
            return False


