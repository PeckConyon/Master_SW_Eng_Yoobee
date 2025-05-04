import  math


class CircleHelper:

    def calculate_Sin(self,value):
        sinValue = math.sin(value)
        sinValue = round(sinValue,2)
        return sinValue
    
    def calculate_Cos(self,value):
        cosValue = math.cos(value)
        cosValue = round(cosValue,2)
        return cosValue
    
    def calculate_circle_ara(self,diameter):
        area =  2 *   math.pi * (diameter/2)
        area = round(area,2)
        return area