from solve_labyrinth import get_neighbors, bfs

def main():
    # If you wish to add more labyrinths, you can add any other labyrinth in the following dictionary:
    labyrinths = {
        '1': [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ],
        '2':[
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["#", ".", ".", ".", "#", ".", ".", "#", "."],
            [".", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", "#", ".", ".", ".", ".", ".", "#", "."],
            [".", "#", ".", ".", ".", ".", ".", "#", "."]
        ],
        '3':[
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["#", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", "#", ".", ".", ".", "."],
            [".", "#", ".", ".", ".", ".", ".", "#", "."],
            [".", "#", ".", ".", ".", ".", ".", "#", "."]
        ],
        '4':[
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".","#",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".",".",".",".","."],
            [".","#",".",".",".","#",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."]
        ]
    }

    # The next snippet code is to show the labyrinths and let the user choose any of the possible labyrinths.

    print('Choose one of the following labyrinths:\n')
    for key, l in labyrinths.items():
        print(f"Labyrinth key: {key}")
        for row in l:
            print(' '.join(row))
        print("\n")  

    while True:
        try:
            lab_key = input('Type the labyrinth key:\n')

            labyrinth = labyrinths[lab_key]

            break
        except KeyError as err:
            print('You are not choosing a valid key, please look the valid keys and choose one:')


    # Startint with the problem:
    start, end = (tuple([(0,0), (0,1), (0,2)])), (len(labyrinth) - 1, len(labyrinth[0]) - 1)
    path = bfs(labyrinth, start, end)

    # Printing the solution:
    print('\n\nSOLUTION:\nInformation with the path choosen and the orientation:\n')
    try:
        for p in path[0]:
            print(p)
            
        print('\nNumber of jumps:')
        print(len(path[0])-1)
    except IndexError as err:
        print("It's not possible to find any path. There is probably not enough room for the rod to manoeuvre.")
        print('\nNumber of jumps:')
        print(-1)

if __name__ == "__main__":
    main()