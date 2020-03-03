class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
       
    
    
    #Equality test
    
    def __eq__(self, other):
        first_num = int(self.top) * int(other.bottom)
        second_num = int(other.top) * int(self.bottom)
        return first_num == second_num
    
   #Representing an object method
    def __repr__(self):
        return str(self.top) + '/' + str(self.bottom)

    #Addition method
    def __add__(self, other):
        common_factor=1
        final_denominator = int(self.bottom) * int(other.bottom)
        final_numerator = (int(other.bottom)* int(self.top)) + (int(self.bottom)* int(other.top))
        if final_numerator > final_denominator:
            up = final_numerator
            down = final_denominator
        elif final_denominator > final_numerator:
            up = final_denominator
            down = final_numerator
        else:
            up = final_denominator
            down = final_numerator
       
        while True:
                
                if down > 0 and up % down >= 1:
                    tempdown = up % down
                    tempup = down
                    up=tempup
                    down=tempdown
     
                    if down > 0:
                       common_factor = down
                 
                else:
                    break
        if final_numerator ==  final_denominator:
             final_numerator =1
             final_denominator = 1
        else:
             final_numerator = int(final_numerator/common_factor)
             final_denominator = int(final_denominator/common_factor)
        print ("{}/{}".format(str(final_numerator),str(final_denominator)))
        return Fraction(final_numerator,final_denominator)
       
    
Fraction(1,4) +Fraction(2,5)
