import unittest
from rod import Rod
from solve_labyrinth import bfs, get_neighbors

class TestRodMovement(unittest.TestCase):
    '''
    Test to check if the algorithm is finding the neighbors
    '''

    def test_get_neighbors(self):
        labyrinth = [
            ["#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", "."],
            ["#", ".", ".", ".", "."],
            ["#", ".", ".", ".", "."],
            ["#", "#", "#", "#", "#"]
        ]

        start = [(1,1), (1,2), (1,3)]
        orientation = "horizontal"
        
        expected_result = [([(1,2), (1,3), (1,4)], "horizontal"), ([(2,1), (2,2), (2,3)], "horizontal")]
        
        self.assertEqual(get_neighbors(labyrinth, start, orientation), expected_result)

    def test_bfs(self):
        '''
        Function to prove if the bfs algorithm is finding the solution.
        Should be good to have a test to prove if the solution is the shortest...
        '''
        labyrinth = [
            ["#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "#"],
            ["#", ".", " ", ".", "#"],
            ["#", "#", "#", "#", "#"]
        ]

        start = [(1,1), (1,2), (1,3)]
        end = (3, 3)
        
        result = bfs(labyrinth, start, end)
        
        self.assertEqual(end, result[0][len(result[0])-1]['pos'][2])  # The result should have the solution

if __name__ == '__main__':
    unittest.main()        