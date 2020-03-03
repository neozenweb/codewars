def expanded_form(num):
    lst = (str(int(elem) * (10**(len(list(str(num))) - 1 -ind))) for ind,elem in enumerate(list(str(num))) if elem!='0')
    return ' + '.join(lst)
    
