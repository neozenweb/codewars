def zero(*argzero):
    if len(argzero)>0:
        for i in argzero:
            if(i !=None):
                newval= eval('0' + str(i))
                return int(newval)
    else:
        return 0

def one(*argone):
    if len(argone)>0:
        for i in argone:
            if(i !=None):
                newval= eval('1' + str(i))
                return int(newval)
    else:
        return 1
    
def two(*argtwo):
    if len(argtwo)>0:
        for i in argtwo:
            newval= eval('2' + str(i))
            return int(newval)
    else:
        return 2

def three(*argthree):
    if len(argthree)>0:
        for i in argthree:
            if(i !=None):
                newval= eval('3'+str(i))
                return int(newval)
    else:
        return 3
 
def four(*argfour):
    if len(argfour)>0:
        for i in argfour:
            if(i !=None):
                newval= eval('4' + str(i))
                return int(newval)
    else:
        return 4
 
def five(*argfive):
    if len(argfive)>0:
        for i in argfive:
            if(i !=None):
                newval= eval('5' + str(i))
                return int(newval)
    else:
        return 5
 
def six(*argsix):
    if len(argsix)>0:
        for i in argsix:
             if(i !=None):
                newval= eval('6' + str(i))
                return int(newval)
    else:
        return 6

 
def seven(*argseven):
    if len(argseven)>0:
        for i in argseven:
             if(i !=None):
                newval= eval('7' + str(i))
                return int(newval)
    else:
        return 7
 
def eight(*argeight):
    if len(argeight)>0:
        for i in argeight:
            if(i !=None):
                newval= eval('8' + str(i))
                return int(newval)
    else:
        return 8
 
def nine(*argnine):
    if len(argnine)>0:
        for i in argnine:
            if(i !=None):
              newval= eval('9' + str(i))
              return int(newval)
    else:
        return 9
    
def plus(numbplus):
    val= numbplus
    return "+" + str(val)
def minus(numbminus):
    val= numbminus
    return "-" + str(val)
def times(numbtimes):
    val= numbtimes
    print(val)
    return "*" + str(val)
def divided_by(numbby):
    val= numbby
    if(val!=0):
        return "//" +str(val)
    else:
        return None

