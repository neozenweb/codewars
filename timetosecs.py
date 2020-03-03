import re
def to_seconds(time):
     validTime = re.compile('[0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}\Z')
     if validTime.match(time):
         digitTime = re.compile('\d')
         hhmmss = digitTime.findall(time)
         if len(hhmmss) != 6:
             return None
         else:
             if int(hhmmss[2]+hhmmss[3])  > 59 or int(hhmmss[4]+hhmmss[5])  > 59:
                 return None
             else:
                 return (int(hhmmss[0]+hhmmss[1]) * 3600 + int(hhmmss[2]+hhmmss[3]) * 60 +int(hhmmss[4]+hhmmss[5]))
     else:
         return None
       
