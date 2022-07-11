# https://docs.python.org/3/library/unittest.html
import unittest
import main

class TestMain(unittest.TestCase):
    def stepUp(self):
        print('Called before each test scenario')

    def test_do_stuff(self):
        '''This tests the stuff'''
        test_param = 10
        result = main.do_stuff(test_param)

        self.assertEqual(result, 15)

    def test_do_stuff_string(self):
        test_param = 'afsdfasddfasd'
        result = main.do_stuff(test_param)

        self.assertIsInstance(result, ValueError)

    def test_do_stuff_none(self):
        test_param = None
        result = main.do_stuff(test_param)

        self.assertEqual(result, 'Not a valid number')
    
    def test_do_stuff_empty_string(self):
        test_param = ''
        result = main.do_stuff(test_param)

        self.assertEqual(result, 'Not a valid number')

    def test_do_stuff_zero(self):
        test_param = 0
        result = main.do_stuff(test_param)

        self.assertEqual(result, 'Not a valid number')

    def tearDown(self):
        print('Called after each test scenario')

# runs the entire test file
if __name__ == '__main__':
    unittest.main()

# python -m unittest
# runs the all test files in the directory although there is main if control

# python -m unittest -v gives more details
