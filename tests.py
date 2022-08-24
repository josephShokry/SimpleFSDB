from inspect import classify_class_attrs
import unittest
from unittest import result
import calc

class testCalc(unittest.TestCase):
    def test_add_1(self):
        result=calc.add(5,3)
        self.assertEquals(result,8)
    def test_add_2(self):
        result=calc.add(-2,3)
        self.assertEquals(result,1)
        





if __name__=='__main__':
    unittest.main()