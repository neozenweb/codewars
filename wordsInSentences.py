# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    import re
    check = re.compile('[a-z][A-Z]*',re.IGNORECASE)
    sentences = S.split(".")
    lengths=[]
    #print(sentences)
    for sent in sentences:
        words = sent.split(' ')
        for ind,wd in enumerate(words):
            print(wd)
            print(len(check.findall(wd.strip())))
            
            if len(wd.strip()) == 0 or len(check.findall(wd.strip())) ==0:
               del words[ind]
        
        print(words)
        lengths.append(len(words))
    lengths.sort()
    print(lengths[-1])
    return lengths[-1]
            