#/////////////////// Day 6 //////////////////

#Task List
# Functions
# Code block
# Indentation

# Mini Maze Escape Game

# Define the maze as a 2D list (you can customize this)
maze = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#']
]

# Player starting position
player_x, player_y = 1, 1

# Function to print the maze
def print_maze():
    for row in maze:
        print(''.join(row))

# Function to move the player
def move(direction):
    global player_x, player_y
    if direction == 'up':
        player_x -= 1
    elif direction == 'down':
        player_x += 1
    elif direction == 'left':
        player_y -= 1
    elif direction == 'right':
        player_y += 1

# Main game loop
while True:
    print_maze()
    print("Controls: 'w' (up), 's' (down), 'a' (left), 'd' (right), 'q' (quit)")
    user_input = input("Enter your move: ")

    if user_input == 'q':
        print("Thanks for playing!")
        break
    elif user_input in ['w', 's', 'a', 'd']:
        move(user_input)
        if maze[player_x][player_y] == '#':
            print("Oops! You hit a wall.")
            move('down')  # Reset the move
        elif maze[player_x][player_y] == ' ':
            maze[player_x][player_y] = 'X'  # Mark visited cell
        elif maze[player_x][player_y] == 'X':
            print("You've already been here.")
    else:
        print("Invalid input. Use 'w', 's', 'a', 'd', or 'q'.")

    # Check if the player reached the exit
    if player_x == 3 and player_y == 3:
        print("Congratulations! You escaped the maze!")
        break
