import unittest
from life import next_state

class TestLife(unittest.TestCase):
    def test_dead_state(self):
        initial_state = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        expected_state = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        self.assertEqual(next_state(initial_state), expected_state)


    def test_next_state(self):
        initial_state = [
            [0,0,1],
            [0,1,1],
            [0,0,0]
        ]

        expected_state = [
            [0,1,1],
            [0,1,1],
            [0,0,0]
        ]
        
        self.assertEqual(next_state(initial_state), expected_state)

if __name__ == '__main__':
    unittest.main()
