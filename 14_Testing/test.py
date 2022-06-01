import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)

        self.assertEqual(result, 15)

    def test_do_stuff_string(self):
        test_param = 'afsdfasddfasd'
        result = main.do_stuff(test_param)

        self.assertTrue(isinstance(result, ValueError))

# runs the entire test file
unittest.main()
