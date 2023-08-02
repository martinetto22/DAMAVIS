class Rod():
    
    '''
    Class to represent the functionalities of the rod. The functions that give the possible movements to the rod are created.
    '''
    
    def __init__(self, initial_position, labyrinth):
        '''
        Initialization of the rod
        
        Args:
        labyrinth (List[List[string]])           ---> List of lists defining the maze. Each string represents a cell of the maze, where '#' represents a wall and '.' represents an empty space.
                                                      
        initial_position (List[Tuple[int, int]]) ---> List of the initial coordinates of the rod. Each tuple consists of two integers which define the initial coordinates of each section of the rod.

        Atributos:
        labyrinth        ---> The labyrinth.
        path (List)      ---> List to store the rod path.
        current_position ---> Initial position of the rod.
        direction (str)  ---> Define the orientation of the rod, to know if it's in horizontal or vertical position.
        null_pos (List)  ---> List with all the coordinates in the labyrinth with: '#'.
        
        '''
        self.labyrinth = labyrinth
        self.path = []
        self.current_position = initial_position
        self.direction = 'horizontal'
        self.null_pos = [
            (i, j) for i, row in enumerate(labyrinth) 
            for j, cell in enumerate(row) if cell == '#'
        ]
        
    def update_coordinates(self):
        '''
        Actualize the coordinates of the head's rod (last element in the current_position's list)
        
        Example:
            The next list represents the rod:
            
            [(0,1), (0,2), (0,3)]
            
            This function actualize the head, the position (0,3). self.y = 0 and self.x = 3
        '''
        self.y, self.x = self.current_position[2]
        
    def valid_movement(self, positions, lower_bound, upper_bound, x_y):
        '''
        Function to check if the movement to be performed is valid. It is necessary to check if any of the coordinates of the rod coincides with any of the coordinates where there is '#' or if the coordinates are
        inside the albyrinth.
        If lower_bound == -1 it is because it is not necessary to check the limit here.
        If upper_bound == float(inf) it is because it is not necessary to check the limit here.
        
        Args:
        positions (List)        ---> New coordinates that the rod should occupy after executing the desired movement.
        lower_bound (int)       ---> Lower limit of the labyrinth (depending on the orientation of the labyrinth, the lower limit is in reference to the x or y axis).
        upper_bound (int/float) ---> The upper bound of the rod (same as lower_bound but upper bound). It is a float when given as an infinite value.
        x_y (int)               ---> Current coordinate of x or y.
        
        Returns:
        bool ---> True if all future rod positions are valid (within the maze and do not match a '#' cell). False otherwise.
        '''
        if all(pos not in self.null_pos for pos in positions) and lower_bound < x_y < upper_bound:
            self.current_position = positions
          
    
    def movment(self, mov):
        '''
        Function that executes the movement of the rod. First the orientation of the rod is checked and then it identifies which movement is to be performed. Depending on the movement, the new coordinates of the
        rod are generated and their validity is checked with the function valid_movment. Finally, if any movement has been made, the list in which the path is saved is updated.
        
        Args:
        mov (str)         ---> Indicate the movement to do.
        '''
        orientation = self.direction
        
        if orientation == 'vertical':
            if mov == 'change_direction':
                self.valid_movement([(self.y,self.x-1), (self.y,self.x), (self.y, self.x+1)], 0, len(self.labyrinth[0])-1, self.x)
                self.path.extend([(self.y+1, self.x)])
                self.direction = 'horizontal'
            else:        
                if mov == 'up':
                    self.valid_movement([(self.y-2, self.x+1), (self.y-1, self.x+1), (self.y, self.x+1)], -1, len(self.labyrinth[0])-1, self.x)

                elif mov == 'down':
                    self.valid_movement([(self.y-2, self.x-1), (self.y-1, self.x-1), (self.y, self.x-1)], 0, float('inf'), self.x)

                elif mov == 'forward':
                    self.valid_movement([(self.y-1, self.x), (self.y, self.x), (self.y+1, self.x)], -1, len(self.labyrinth)-1, self.y)

                elif mov == 'back':
                    self.valid_movement([(self.y-3, self.x), (self.y-2, self.x), (self.y-1, self.x)], 0, float('inf'), self.y-2)

                self.path.extend([(self.y, self.x)])
                    
        elif orientation == 'horizontal':
            if mov == 'change_direction':
                self.valid_movement([(self.y-1,self.x), (self.y,self.x), (self.y+1, self.x)], 0, len(self.labyrinth)-1, self.y)
                self.path.extend([(self.y, self.x+1)])
                self.direction = 'vertical'
            
            else:
                if mov == 'up':
                    self.valid_movement([(self.y-1, self.x-2), (self.y-1, self.x-1), (self.y-1, self.x)], 0, float('inf'), self.y)

                elif mov == 'down':
                    self.valid_movement([(self.y+1, self.x-2), (self.y+1, self.x-1), (self.y+1, self.x)], -1, len(self.labyrinth)-1, self.y)

                elif mov == 'forward':
                    self.valid_movement([(self.y, self.x-1), (self.y, self.x), (self.y, self.x+1)], -1, len(self.labyrinth[0])-1, self.x)

                elif mov == 'back':
                    self.valid_movement([(self.y, self.x-3), (self.y, self.x-2), (self.y, self.x-1)], 0, float('inf'), self.x-2)
                        
                self.path.extend([(self.y, self.x)])
                
        
    def change_direction(self):
        '''
        Function to perform a rotation on the rod (it will go from horizontal to vertical or vice versa, from vertical to horizontal).
        This function uses the midpoint of the rod to find the new coordinates, so do not use the update_coordinates method.
        '''
        self.y, self.x = self.current_position[1]
                
        self.movment('change_direction')
  
        
    def up(self):
        '''
        Function to perform the upward movement (depending on the orientation, up for x or up for y).
        '''
        self.update_coordinates()
        
        self.movment('up')
        
    
    def down(self):
        '''
        Function to perform the downward movement (depending on the orientation, up for x or up for y).
        '''
        self.update_coordinates()
        
        self.movment('down')
        
            
    def forward(self):
        '''
        Function to perform the forward movement.
        '''
        self.update_coordinates()
        
        self.movment('forward')
        
            
    def back(self):
        '''
        Function to perform the back movement.
        '''
        self.update_coordinates()
        
        self.movment('back')
    