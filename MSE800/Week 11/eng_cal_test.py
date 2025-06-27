import unittest
from eng_cal import EngCal

class TestEngCal(unittest.TestCase):
    
    def __init__(self,eng_cal):
        self.eng_cal = eng_cal
        
    def test_power(self):   
        expected = 5       
        self.assertEqual(EngCal().power(2,2), expected)
        
    def test_root(self):          
        expected = 4       
        self.assertEqual(self.eng_cal.root(), expected)
        
    def test_sine(self):          
        expected = 4       
        self.assertEqual(self.eng_cal.power(2,2), expected)
        
    def test_cosine(self):          
        expected = 4       
        self.assertEqual(self.eng_cal.power(2,2), expected)
        
    def test_tangent(self):          
        expected = 4       
        self.assertEqual(self.eng_cal.power(2,2), expected)
       
        
    def test_isdigit(self):
        result =  '123'.isdigit()
        expected = True
        # approach 1
        self.assertEqual(result,expected)
        # approach 2
        self.assertTrue(result)

if __name__ == '__main__':
    eng_cal = EngCal()
    unittest.main(eng_cal)