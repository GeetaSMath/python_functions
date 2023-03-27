import unittest
import math_fun
from math_fun import add
from math_fun import product


class Operation(unittest.TestCase):
    def test_add(self):
        self.assertEqual( math_fun.add(2, 4) , 6)
        self.assertEqual(math_fun.add(4) , 6)

        #assert math_fun.add(2, 4) == 6
        #assert math_fun.add(4) == 6

    def test_product(self):
        self.assertEqual( math_fun.product(5, 5), 25)
        self.assertEqual(math_fun.product(5) ,10)
        #assert math_fun.product(5, 5) == 25
        #assert math_fun.product(5) == 10


if __name__ == '__main__':
    unittest.main()
