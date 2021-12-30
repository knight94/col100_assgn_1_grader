import unittest
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from os import listdir
from os.path import isfile, join, splitext, basename
subpath = "/autograder/submission"
onlyfiles = [f for f in listdir(subpath) if isfile(join(subpath, f))]

impt = __import__(splitext(onlyfiles[0])[0])
test_cases_part1 = {
                    (False, True, True): (False, True),
                    (False, True, False): (True, False),
                    (True, True, True): (True, True),
                    (True, False, False): (True, False),
                    (False, False, False): (False, False),
                    }

test_cases_part2 = {
        (False,False,False,False,False,False,False,False,True):(True, False, False, False, False),
        (False,False,False,False,False,False,False,False,False):(False, False, False, False, False),
        (True,True,True,True,True,True,True,True,True):(True, True, True, True, True),
        (True,False,True,False,True,False,True,False,True):(True, True, False, True, False),
        (True,False,True,False,True,False,True,False,False):(False, True, False, True, False),
        (True,True,False,True, True,False,False,True, False):(False, False, True, False, True),
                    }

test_cases_part3 = {0:{
        (True,False,False,False,False,True,False,False):True,
        (True,True,False,True, True,False,False,True):False,
        (True,True,False,True, True,True,False,False):False,
        (False,True,True,False, True,False,False,True):True, 
        }, 1:{
        (True,False,False,False,False,True,False,False):True,
        (True,True,False,True, True,False,False,True):False,
        (True,True,False,True, True,True,False,False):False,
        (False,True,True,False, True,False,False,True):True,
        }, 2:{
        (True,True,True,True,True,True,True,True):False,
        (False,True,True,True,True,True,True,True):False,
        (True,True,True,True,True,True,False,True):True,
        (False,False,False,True,False,False,True,False):True,
        }, 3:{
        (True,False,False,False,False,True,False,False):False,
        (True,True,False,True, True,False,False,True):True,
        (True,True,False,True, True,True,False,False):True,
        (False,True,True,False, True,False,False,True):False,
                    }}

test_cases_part4 = {
            (False,False,False,False,False,False,False,False):(False, False, False, False, False),
            (True,True,True,True,True,True,True,True):(False, False, False, False, False),
            (True,False,True,False,False,True,False,True):(True, False, True, False, True),
            (False,True,False,True,True,False,True,False):(True, False, True, False, False),
            (False,False,False,True,True,False,True,True):(True, False, True, False, True),
            (True,False,False,True, True,True,False,True):(False, True, False, False, True),
                    }

test_cases_part5 = {
        ((True,True,True,True,True,True,False,False),(True,False,False,False,False,False,False,False), False):((False, False, False, False, False, False, True, False), False),
        ((True,True,True,True,True,True,False,False),(True,False,False,False,False,False,False,False), True):((True, False, False, False, False, False, True, False), False),
        ((False,False,True,True,False,False,False,False),(False,True,True,False, True,False,False,True), True):((True, True, False, False, False, True, False, True), False),
        ((False,False,False,False,False,False,True,False),(False,True,True,False, True,False,False,True), False):((False, True, True, False, True, False, True, True), False),
        ((True,False,True,False,True,False,True,True),(True,False,True,False,False,True,False,True), True):((True, True, False, True, True, True, True, False), True),
        ((True,True,True,True,True,True,False,False),(True,True,True,False,False,True,False,False), False):((False, True, True, False, False, True, True, False), False),
        ((True,True,True,True,True,True,False,False),(True,True,True,False,False,True,False,False), True):((True, True, True, False, False, True, True, False), False),
        ((True, True, True, True, True, True, True, True), (True, True, True, True, True, True, True, True), True):((True, True, True, True, True, True, True, True), True),
                    }

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
        self.add = impt.add
        self.add4 = impt.add4
        self.cmp = impt.cmp
        self.sub4 = impt.sub4 
        self.add8 = impt.add8
        self.mul4 = impt.mul4

    @weight(0)
    @visibility('after_published')
    def test_eval_add(self):
        """Running test cases to check 1 bit adder"""
        for i,o in test_cases_part1.items():
            a, b, c = i
            val = self.add(a, b, c)
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)

    @weight(0)
    @visibility('after_published')
    def test_eval_add4(self):
        """Running test cases to check 4 bit adder"""
        for i,o in test_cases_part2.items():
            val = self.add4(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)

    @weight(0)
    @visibility('after_published')
    def test_eval_cmp(self):
        """Running test cases to check comparator (<)"""
        for i,o in test_cases_part3[impt.rem].items():
            val = self.cmp(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)

    @weight(0)
    @visibility('after_published')
    def test_eval_sub4(self):
        """Running test cases to check 4 bit subtractor"""
        for i,o in test_cases_part4.items():
            val = self.sub4(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            if (o[0] or o[1] or o[2] or o[3]):
                self.assertEqual(val, o)
            else:
                self.assertEqual(val[0:2], o[0:2])

    @weight(0)
    @visibility('after_published')
    def test_eval_add8(self):
        """Running test cases to check 8 bit adder"""
        for i,o in test_cases_part5.items():
            val = self.add8(i[0], i[1], i[2])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)

    @weight(0)
    @visibility('after_published')
    def test_eval_mul4(self):
        """Running test cases to check 4 bit multiplier"""
        for i,o in test_cases_part6.items():
            print("Input value: {}| expected output: {}| output: {}".format(i,o,00))
            val = self.mul4(i[0], i[1])
            print("Input value: {}| expected output: {}| output: {}".format(i,o,val))
            self.assertEqual(val, o)
