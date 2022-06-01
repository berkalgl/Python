# https://docs.python.org/3/library/unittest.html
import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)

# runs the entire test file
if __name__ == '__main__':
    unittest.main()

