class DifferentVectorLengths(Exception):
    def __init__(self, message):
        self.message = "Different Vector Lengths"
        



class Vector:
  
    def __init__(self, veclist):
        
        self.vector = veclist

   #equals methos
    def equals(self, other):
         print (self.vector)
         print (other.vector)
         return self.vector== other.vector
     
    
   #Representing an object method
    def __repr__(self):
        return self.vector
    def __str__(self):
        tup="("
        tempvec=[]
        for ind,i in enumerate(self.vector):
            tup +=str(i).replace(' ','')
            if ind>=0 and ind<len(self.vector)-1:
                tup+=","
    
        tup +=")"
         
        return str(tup)
    
    #Addition method
    def add(first, other):
         if len(first.vector) != len(other.vector):
             raise DifferentVectorLengths("Vectors should be of same length.")
         else:
             newvec=[]
             for ind,x in enumerate(first.vector):
                 newvec.append(x + other.vector[ind])
         return Vector(newvec)
    #Subtraction method
    def subtract(first, other):
         if len(first.vector) != len(other.vector):
             raise DifferentVectorLengths("Vectors should be of same length.")
         else:
             newvec=[]
             for ind,x in enumerate(first.vector):
                 newvec.append(x - other.vector[ind])
         return Vector(newvec)
     #dot method
    def dot(first, other):
         if len(first.vector) != len(other.vector):
             raise DifferentVectorLengths("Vectors should be of same length.")
         else:
             newvec=[]
             sum=0
             for ind,x in enumerate(first.vector):
                 newvec.append(x * other.vector[ind])
         for elem in newvec:
             sum += elem
         return sum
         return Vector(newvec)
     #norm method
    def norm(first):
         import math
         newvec=[]
         sum=0
         for ind,x in enumerate(first.vector):
                 newvec.append(x * x)
         for elem in newvec:
             sum += elem
         return math.sqrt(sum)
