import unittest
from unittest.mock import patch
from game import the_game, evaluate

class TestGameFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['5', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    def test_evaluate(self, mock_input):
        result = evaluate('1 + 2 * 3 / 4 - 5')
        self.assertAlmostEqual(result, -2.5, places=3)

    @patch('builtins.input', side_effect=iter(['2', '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
    def test_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            the_game()
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
