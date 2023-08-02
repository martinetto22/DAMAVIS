from rod import Rod

def bfs(labyrinth, start, end):
    '''
    It implements the Breadth-First Search (BFS) algorithm to find the shortest path.

    You can find a good explanation of the algorithm in the following links:
    https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9
    https://medium.com/swlh/breadth-first-search-algorithm-c2c394c77410
    
    Args:
    labyrinth (List[List[str]]) ---> A list of lists representing the labyrinth, where a '#' represents an obstacle
    start (List[Tuple[int]])    ---> A list of three positions (tuples) representing the starting position of the rod.
    end (Tuple[int])            ---> A tuple with the coordinate of the final position, the target destination.Una tupla con la coordenada de la posicion final, el objetivo de destino.

    Returns:
    List[List[Dict[str, Union[Tuple[int], str]]]] ---> A list of paths, where each path is a list of steps from start to finish. from start to finish. Each step is a dictionary containing the position of the rod
                                                      ('pos') and its orientation ('orientation').
    '''
    queue = [({'pos': start, 'orientation': 'horizontal'}, [{'pos': start, 'orientation': 'horizontal'}])]
    visited = set()
    successful_paths = []

    while queue:
        (vertex, path) = queue.pop(0)
        vertex_position = vertex['pos']
        vertex_orientation = vertex['orientation']

        if tuple(vertex_position) not in visited:
            if any(coord==end for coord in vertex_position):
                successful_paths.append(path)
                break
            visited.add(tuple(vertex_position))
            
            for neighbor_position, neighbor_orientation in get_neighbors(labyrinth, vertex_position, vertex_orientation):
                neighbor = {'pos': neighbor_position, 'orientation': neighbor_orientation}
                queue.append((neighbor, path + [neighbor]))
            
    return successful_paths

def get_neighbors(labyrinth, position, orientation):
    '''
    Function to detect the valid neighbours to which the rod can go. Apart from giving the neighbours that can be reached, it also tells how to get there. For this it will validate all the possible movements of
    the the rod.
    
    Args:
    labyrinth (List[List[str]])      ---> A list of lists representing the labyrinth, where a '#' represents an obstacle. 
    position (List[Tuple[int, int]]) ---> List of the initial coordinates of the rod. Each tuple consists of two integers which define the initial coordinates of each section of the rod.
    orientation (str)                ---> Orientation of the rod. Can be vertical or horizontal.
    
    Returns:
    neighbors (List) ---> List of all neighbours that can be reached by the rod.
    '''
    
    neighbors = []
    
    for direction in ['forward', 'back', 'up', 'down', 'change_direction']:
        rod = Rod(position, labyrinth)
        rod.direction = orientation
        
        if direction == 'forward':
            rod.forward()
        elif direction == 'back':
            rod.back()
        elif direction == 'up':
            rod.up()
        elif direction == 'down':
            rod.down()
        elif direction == 'change_direction':
            rod.change_direction()
        
        if rod.current_position != position and all(coord not in rod.null_pos for coord in rod.current_position):
            neighbors.append((rod.current_position, rod.direction))
    
    return neighbors