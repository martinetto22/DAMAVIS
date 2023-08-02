import unittest
from rod import Rod

class TestBfs(unittest.TestCase):
    def test_bfs(self):
        labyrinth = [
            ['#', '.', '#', '#', '#'],
            ['#', '.', '#', '#', '#'],
            ['#', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#']
        ]
        start = [(0, 1), (0, 2), (0, 3)]
        end = (2, 4)
        result = bfs(labyrinth, start, end)
        expected_result = [
            {'pos': start, 'orientation': 'horizontal'},
            {'pos': [(0, 2), (0, 3), (0, 4)], 'orientation': 'horizontal'},
            {'pos': [(1, 3), (1, 2), (1, 1)], 'orientation': 'vertical'},
            {'pos': [(2, 2), (2, 3), (2, 4)], 'orientation': 'horizontal'}
        ]
        self.assertEqual(result, [expected_result])
