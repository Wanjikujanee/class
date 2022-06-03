# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr


class Circle():
      
    	    def __init__(self, r):
              self.radius = r
            def area(self):  	        
                return self.radius**2*3.14
	    
            def perimeter(self):
	         return 2*self.radius*3.14

         
         