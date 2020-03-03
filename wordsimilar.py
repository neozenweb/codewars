class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        wordsimilar={}
        print("**********")
        print(self.words)
 
      
        
        retval =''
        for wd in self.words:
           
            print(list(wd))
            if wd.lower() == term.lower():
                return wd
            wordsimilar[wd]=abs(len(wd)-len(term))
        
    
        print(wordsimilar)
        val = sorted(wordsimilar.values())
        finals=[]
        for wd in wordsimilar:
            if abs(wordsimilar[wd] - val[0]) <= 3:
                finals.append(wd)
        print("*****")
        print(finals)
        wordsimilar.clear()
        
        for item in finals:
            ctr = 0
            #print(item+"NOW"+term)
            for ltr in list( dict.fromkeys(item)):
                if term.lower().count(ltr.lower()) > 0:
                    print(item,ltr, item.lower().count(ltr.lower()))
                    ctr += item.lower().count(ltr.lower())
               
           
            wordsimilar[item]=ctr
        print(wordsimilar)
        print(sorted(wordsimilar.values()))
        for key, value in wordsimilar.items():
            if sorted(wordsimilar.values())[-1] == value and len(key) - len(term)< 3:
                retval = key
                break
            elif sorted(wordsimilar.values())[-2] == value and len(key) - len(term)< 2:
                retval = key
                
            elif sorted(wordsimilar.values())[-3] == value and len(key) - len(term)< 1:
                retval = key
                
               

            
        return retval