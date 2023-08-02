import unittest
from project.rod import Rod

class TestRod(unittest.TestCase):
    '''
    Tests to prove methods of the Rod class.
    '''
    def setUp(self):
        '''
        Initialization with all the necessary variables to do the tests. It's important to know that
        if you modify the labyrinth it's possible that you need to do some modifications in the tests.
        For example, there are some tests that need to initialize by themselves the position of the rod,
        if you put a '#' value in this position or you generate a small labyrinth, you could have problems.
        '''
        self.labyrinth = [
            ['#', '#', '#', '#', '.'],
            ['#', '.', '.', '.', '.'],
            ['#', '.', '.', '.', '.'],
            ['#', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '.']
        ]
        self.initial_position = [(2, 1), (2, 2), (2, 3)]
        self.rod = Rod(self.initial_position, self.labyrinth)
        self.null_pos = [
            (i, j) for i, row in enumerate(self.labyrinth) 
            for j, cell in enumerate(row) if cell == '#'
        ]
        
    def test_initialization(self):
        '''
        To check the correct initialization of the Rod class.
        '''
        self.assertEqual(self.rod.current_position, self.initial_position)
        self.assertEqual(self.rod.direction, 'horizontal')
        self.assertEqual(self.rod.labyrinth, self.labyrinth)
        self.assertEqual(self.rod.null_pos, self.null_pos)
        
    def test_update_coordinates(self):
        '''
        Checking if the coordinates are updated propely.
        '''
        self.rod.update_coordinates()
        self.assertEqual(self.rod.y, self.initial_position[2][0])
        self.assertEqual(self.rod.x, self.initial_position[2][1])
    
    def test_valid_movement(self):
        # Trying to move to an invalid position
        invalid_position = [(0, 0), (0, 1), (0, -1)]  # (0, -1) is out of the labyrinth
        old_position = self.rod.current_position.copy()
        self.rod.valid_movement(invalid_position, 0, 4, 1)
        self.assertEqual(self.rod.current_position, old_position)  # Looking if the position changed

        # Trying to move to a valid position
        valid_position = [(1, 1), (1, 2), (1, 3)] 
        self.rod.valid_movement(valid_position, 0, 4, 2)
        self.assertEqual(self.rod.current_position, valid_position)

    def test_movment(self):
        '''
        It's important to modify the labyrinth to do these tests because are more restrictive.
        '''
        # Trying a forward movment
        self.rod.update_coordinates()
        old_position = self.rod.current_position.copy()
        self.rod.movment('forward')
        self.assertNotEqual(self.rod.current_position, old_position)

        # Changing direction to vertical
        old_position = self.rod.current_position.copy()
        self.rod.movment('change_direction')
        self.assertNotEqual(self.rod.current_position, old_position)
        self.assertEqual(self.rod.direction, 'vertical')

        # Trying a not valid movment
        self.rod.current_position = [(1,1),(1,2),(1,3)]
        old_position = self.rod.current_position.copy()
        self.rod.movment('up')
        self.assertNotEqual(self.rod.current_position, old_position)

    def test_change_direction(self):
        # To prove the change direction method this test compare the direction of the rod.
        old_direction = self.rod.direction
        self.rod.change_direction()
        self.assertNotEqual(self.rod.direction, old_direction)

    def test_up(self):
        # To prove an up movment.
        old_position = self.rod.current_position.copy()
        self.rod.up()
        self.assertNotEqual(self.rod.current_position, old_position)

    def test_down(self):
        # To prove a down movment
        old_position = self.rod.current_position.copy()
        self.rod.down()
        self.assertNotEqual(self.rod.current_position, old_position)

    def test_forward(self):
        # To prove a forward movment
        old_position = self.rod.current_position.copy()
        self.rod.forward()
        self.assertNotEqual(self.rod.current_position, old_position)

    def test_back(self):
        # To prove back movment
        self.rod.current_position = [(1,2), (1,3), (1,4)]
        old_position = self.rod.current_position.copy()
        self.rod.back()
        self.assertNotEqual(self.rod.current_position, old_position)


if __name__ == '__main__':
    unittest.main()