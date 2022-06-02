# importing sys
import sys
  
# adding Folder_2 to the system path
sys.path.insert(0, 'D:/CodeRepository/PythonDSA/10_Modules/built_in_modules')

import guessing_game

import unittest

class TestMain(unittest.TestCase):
    def test_guessing_game(self):
        result = guessing_game.check_answer(5,5)
        self.assertTrue(result)


# runs the entire test file
if __name__ == '__main__':
    unittest.main()
