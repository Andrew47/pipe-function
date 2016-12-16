import unittest
from pipe import pipe

class TestPipeMethod(unittest.TestCase):

    #Functions used in testing:

    def plus1(self, arg): return arg + 1
    def plus2(self, arg): return arg + 2
    def plus3(self, arg): return arg + 3
    def no_arg(self): return 2

    def setUp(self):
        self.pipe = pipe

    def test_apply_one_function(self):
        """Applies pipe to one function and has no effect"""
        self.assertEqual(self.pipe(30)(self.plus1), self.plus1(30))

    def test_apply_two_functions_list(self):
        """Applies pipe to two functions and is as expected with list"""
        self.assertEqual(self.pipe(30)([self.plus1
                                       , self.plus2])
                                       , self.plus1(self.plus2(30)))

    def test_apply_two_functions_tuple(self):
        """Applies pipe to two functions and is as expected with tuple"""
        self.assertEqual(self.pipe(30)((self.plus1
                                       , self.plus2))
                                       , self.plus1(self.plus2(30)))

    def test_apply_two_functions_no_argument(self):
        """Applies pipe to two functions and is as expected with no argument"""
        self.assertEqual(self.pipe()((self.no_arg
                                       , self.plus1))
                                       , self.plus1(self.no_arg()))

    def test_apply_three_arguments(self):
        """Applies pipe to three functions and is as expected with list"""
        self.assertEqual(self.pipe(30)([self.plus1
                                       , self.plus2
                                       , self.plus3])
                                       , self.plus3(self.plus2(self.plus1(30))))


if __name__ == '__main__':
  unittest.main()
