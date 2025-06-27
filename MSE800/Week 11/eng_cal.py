class EngCal:
        
#power, root, and trigonometric functions (sine, cosine, and tangent). 
    def __init__(self):
        pass
    
    def power(self, base, exponent):
        return base ** exponent
    
    def root(self, number, n=2):
        return number ** (1/n)
    
    def sine(self, angle):
        import math
        return math.sin(math.radians(angle))
    
    def cosine(self, angle):
        import math
        return math.cos(math.radians(angle))
    
    def tangent(self, angle):
        import math
        return math.tan(math.radians(angle))
