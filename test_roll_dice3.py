
import unittest
from unittest.mock import patch
import random
from roll_dice3 import roll_dice

class TestDiceRoll(unittest.TestCase):

    @patch('random.randint')

    #Test that rolling results neither 1 nor 6
    def test_roll_dice_neither_one_nor_six(self, mock_randint):
        mock_randint.side_effect = [3, 4]  
        result = roll_dice()
        self.assertEqual(result, [(3, 4)])

    @patch('random.randint')


    #Test that both dice show 6. First rolled both 6 second rolled 3 and 4
    def test_roll_dice_both_six(self, mock_randint):
        mock_randint.side_effect = [6, 6, 3, 4]
        result = roll_dice()
        self.assertEqual(result, [(3, 4)]) 

    @patch('random.randint')
    def test_roll_dice_both_one(self, mock_randint):

        #Test that both dice show 1. First two rolls are 1, then 3 and 4
        mock_randint.side_effect = [1, 1, 2, 4]  
        result = roll_dice()
        self.assertEqual(result, [(2, 4)]) 

    @patch('random.randint')
    def test_roll_dice_exceed_attempts(self, mock_randint):

        #Test that maximum attempts are exceeded.Will roll 1,1 then 6,6,6,6
        mock_randint.side_effect = [1, 1, 6, 6, 6, 6]  
        result = roll_dice()
        self.assertEqual(result, []) 

if __name__ == '__main__':
    unittest.main()

"""
import unittest
from roll_dice3 import roll_dice

class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        result = roll_dice()
        
        # Check if result is a list
        self.assertIsInstance(result, list)
        
        # Check if result is either empty or has dice values
        if result:
            dice1, dice2 = result[0]
            self.assertIn(dice1, range(1, 7))
            self.assertIn(dice2, range(1, 7))
        else:
            self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
"""