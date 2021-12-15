import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from col100_assignment_1 import add, add4

class TestSimpleArithmetic(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.add = add
        self.add4 = add4

    @weight(1)
    def test_eval_add(self):
        """Evaluate 1+1+1"""
        val = self.add(True, True, True)
        print(val)
        self.assertEqual(val, (True, True))

    @weight(1)
    def test_eval_add4_1(self):
        """Evaluate 0101+0101+0"""
        val = self.add4(True,False,True,False,True,False,True,False,False)
        print(val)
        self.assertEqual(val, (False,True,False,True,False))

    @weight(1)
    def test_eval_add4_2(self):
        """Evaluate wrong 0101+0101+0"""
        val = self.add4(True,False,True,False,True,False,True,False,False)
        print(val)
        self.assertEqual(val, (False,True,False,True,True))
