import unittest
from RPS_game import play, quincy
from RPS import player


class RPSTest(unittest.TestCase):

    def test_player(self):
        result = play(player, quincy, 1000)
        self.assertTrue(result['player1'] > result['player2'])


if __name__ == "__main__":
    unittest.main()  
