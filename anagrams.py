def anagrams(word, words):
    retlist=[]
    for wd in words:
         if len(word)==len(wd) and (''.join(sorted(list(wd)))== ''.join(sorted(list(word)))):
           retlist.append(wd)
    return retlist
