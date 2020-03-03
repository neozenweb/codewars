class DimensionsOutOfBoundError(Exception):
    def __init__(self, message):
        self.message = "DimensionsOutOfBoundError"
        




class Package:
    
    def __init__(self,length,width,height,weight):
          if self.validrange(length,"Length"):
               self._length = length
          else:
               raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("length",length,0,"length",350))
                  
          if(self.validrange(width,"Width")):
              self._width = width
          else:
               raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("width",width,0,"width",300))
                  
          if(self.validrange(height,"Height")):
              self._height = height
          else:
             raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("height",height,0,"height",150))
          if(self.validrange(weight,"Weight")):
              self._weight = weight
          else:
               raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("weight",weight,0,"weight",40))
                  
          if(self.validrange(self._length,"Length") and self.validrange(self._width,"Width") and self.validrange(self._height,"Height") and self.validrange(self._weight,"Weight")):
              self.volume = self._length*self._width*self._height
          else:
              self.volume=-1
     
          
    def validrange(self,num,label):

            if( label=="Length"):
               if (num >0 and num<351):
                     return True
               else:
                     return False
                
            if( label=="Width"):
                if(num >0 and num<301):
                    return True
                else:
                    return False
            
            if( label=="Height"):
                if(num >0 and num<151):
                    return True
                else:
                     return False
            
            if( label=="Weight"):
                if (num >0 and num<41):
                    return True
                else:
                    return False
    
    def __repr__(self):

        print("IN Repr")
        if(self.volume > -1 ):
              return ("Volume is {}".format(self.volume))
        else:
              return("Enter valid dimensions for calculating the package volume.")
     
        
            
    def __str__(self):
        print("IN self str")
        if(self.volume > -1 ):
              return ("Volume is {}".format(self.volume))
        else:
              return("Enter valid dimensions for calculating the package volume.")
  
       
    @property
    def length(self):
        print("Getting value")
        return self._length

    @length.setter
    def length(self, value):
               if (value >0 and value<351):
                     self.volume = (self.volume/self._length) * value
                     self._length =value
                     return value
               else:
                    raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("length",value,0,"length",350))
                    return -1
    @property
    def width(self):
        print("Getting value")
        return self._width

    @width.setter
    def width(self, value):
               if (value >0 and value<301):
                     self.volume = (self.volume/self._width) * value
                     self._width =value
                     return value
               else:
                     raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("width",value,0,"width",300))
                     return -1
    @property
    def height(self):
        print("Getting value")
        return self._height

    @height.setter
    def height(self, value):
               if (value >0 and value<151):
                     self.volume = (self.volume/self._height) * value
                     self._height = value
                     return value
               else:
                     raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("height",value,0,"height",150))
                     return -1
    @property
    def weight(self):
        print("Getting value")
        return self._weight

    @weight.setter
    def weight(self, value):
               if (value >0 and value<41):
                     self._weight=value
                     return value
               else:
                     raise DimensionsOutOfBoundError("Package {}=={} out of bounds, should be: {} < {} <= {}".format("weight",value,0,"weight",40))
                     return -1
         
    
