import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from os import listdir
from os.path import isfile, join, splitext, basename
subpath = "/autograder/submission"
onlyfiles = [f for f in listdir(subpath) if isfile(join(subpath, f))]

impt = __import__(splitext(onlyfiles[0])[0])

test_cases_part6 = {
            ((True, True, False, False), (True, True, False, False)):(True, False, False, True, False, False, False, False),
            ((True, True, True, True), (False, True, True, True)):(False, True, False, False, True, False, True, True),
            ((True, False, False, False), (True, False, False, False)):(True, False, False, False, False, False, False, False),
            ((True, True, True, True), (True, False, False, False)):(True, True, True, True, False, False, False, False),
            ((False, True, False, True), (False, True, False, True)):(False, False, True, False, False, True, True, False),
            ((True, True, False, False), (False, False, False, False)):(False, False, False, False, False, False, False, False),
            ((False, False, False, False), (True, True, True, True)):(False, False, False, False, False, False, False, False),
            ((True,True,False,True), (True,False,False,True)):(True, True, False, False, False, True, True, False),
            ((True,True,True,True),(True,True,True,True)):(True, False, False, False, False, True, True, True),
            ((True, True, False, True), (True, True, False, True)):(True, False, False, True, True, True, True, False),
                    }
class TestSimpleArithmetic(unittest.TestCase):
    def setUp(self):
        self.mul4 = impt.mul4
        self.mul4i = impt.mul4i

    @weight(0)
    #@visibility('after_published')
    def test_eval_mul4(self):
        """Running test cases to check 4 bit multiplier"""
        for i,o in test_cases_part6.items():
            print("Input value: {}| expected output: {}| output: {}".format(i,o,00))
            val = self.mul4(i[0], i[1])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)

    @weight(0)
    #@visibility('after_published')
    def test_eval_mul4i(self):
        """Running test cases to check 4 bit multiplier"""
        for i,o in test_cases_part6.items():
            print("Input value: {}| expected output: {}| output: {}".format(i,o,00))
            val = self.mul4i(i[0], i[1])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)
