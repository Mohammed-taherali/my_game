"""
Created by: Mohammed Taherali
Github user id: Mohammed-taherali

A simple maze game using the terminal.

Date: 10-07-2022
"""

# Imports.
from sys import argv, exit, stdout
from os import path
import os
import keyboard

# Get the name of maze.
try:
    maze_file = argv[1]
except IndexError:
    exit("Please provide the maze file name.")

# Get the directory of the maze file.
main_dir = path.split(path.abspath(maze_file))[0]
maze_dir = path.join(main_dir, "mazes\\{}".format(maze_file))

# Check if file exists.
if not path.exists(maze_dir):
    exit("File not found.")

# Get maze.
maze = []
with open(maze_dir) as file:
    maze = file.readlines()

# Make the maze look real.
new_maze = []
for row in maze:
    nr = []
    for col in row:
        if col == "#":
            nr.append("█") 
        elif col == " ":
            nr.append(" ")
        elif col == "S":
            nr.append("S")
        elif col == "E":
            nr.append("E")
        else:
            nr.append("\n")
    new_maze.append(nr)


class Game:
    """
    Game class.
    functions:

    __init__() -> None
        Initializes the variables used in the Game class

    start() -> None
        Shows the homescreen of the game.
        User can:
            1] Start the game.
            2] Get help.
            3] Quit the game.

    play() -> None
        Starts the while loop for the game and calls different functions as per their usage.

    help() -> None
        Shows information about the game and controls of the game.

    get_pos(elem: str) -> tuple
        Takes the element (as a string) as input parameter and returns a tuple containing the co-ordinates of that element.

    new_pos(key: str, pos: tuple) -> tuple
        Updates the user's position temporarily according to the key press.

    check_hash(pos: tuple) -> bool
        Checks if hash is present at the position, which is given as the argument to the function.

    update_maze(dest_pos: tuple, org_pos: tuple) -> None
        Updates the maze by moving the user from org_pos to dest_pos.

    read_key() -> str
        Reads the key entered by the user.
        The loop runs infinitey until the user does not press any one of the arrow keys or the 'p' key.

    display_maze() -> None
        Displays the updated maze.
    """
    
    def __init__(self, maze) -> None:
        """
        Initialize the Game class variables.
        """
        self.maze = maze


    def start(self) -> None:
        """
        Load the homepage of the game.
        """

        # Menu option.
        print("\n\t\t\tWelcome to: 'THE MAZE'!")
        print("Play (1)")
        print("Help (2)")
        print("Quit (3)")

        # Get user input.
        self.choice = int(input("> "))

        # Call respective class method.
        if self.choice == 1:
            self.play()
        elif self.choice == 2:
            self.help()
        elif self.choice == 3:
            exit()
        else:
            self.start()


    def play(self) -> None:
        """
        Let the user play the game!
        """

        # Get start and finish positions.
        self.start_pos = self.get_pos("S")
        self.end_pos = self.get_pos("E")
        self.curr_pos = self.start_pos

        # Main loop of the game.
        while True:
            os.system("cls")
            if self.curr_pos == self.end_pos:
                print("You Won!!!")
                exit()
            # Display the maze.
            self.display_maze()

            self.key_press = self.read_key()

            if self.key_press == "p":
                exit()

            self.temp_pos = self.new_pos(self.key_press, self.curr_pos)
            if self.temp_pos and not self.check_hash(self.temp_pos):
                self.update_maze(self.temp_pos, self.curr_pos)
                self.curr_pos = self.temp_pos
                

    def help(self) -> None:
        """
        Load help message.
        """

        self.help_message = """
        Welcome to 'The Maze'.
        This is a simple maze game wherein the goal is to reach the end of the maze.
        
        Controls:
        Use arrow keys to move left, right, up and down.
        P - Quit the game."""
        print(self.help_message)
        print("(Press Enter to go to home screen.)")
        input()
        self.start()


    def get_pos(self, elem: str) -> tuple:
        """
        Find the position of the given element.
        """

        for row_no, row in enumerate(self.maze):
            for col_no, col in enumerate(row):
                if col == elem:
                    return (row_no, col_no)


    def new_pos(self, key: str, pos: tuple) -> tuple:
        """
        Update temp position of user.
        """
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        if key == "left":
            if pos[1] - 1 > 0 and pos[1] - 1 < self.width:
                return (pos[0], pos[1] - 1)
            else:
                return None
        elif key == "right":
            if pos[1] + 1 > 0 and pos[1] + 1 < self.width:
                return (pos[0], pos[1] + 1)
            else:
                return None
        elif key == "up":
            if pos[0] - 1 > 0 and pos[0] - 1 < self.height:
                return (pos[0] - 1, pos[1])
            else:
                return None
        elif key == "down":
            if pos[0] + 1 > 0 and pos[0] + 1 < self.height:
                return (pos[0] + 1, pos[1])
            else:
                return None


    def check_hash(self, pos: tuple) -> bool:
        """
        Check if hash is present at the given position or not.
        Returns True if present, False otherwise.
        """

        if self.maze[pos[0]][pos[1]] == "█":
            return True
        else:
            return False

    
    def update_maze(self, dest_pos: tuple, org_pos: tuple) -> None:
        """
        Update the maze by moving the user.
        """

        self.maze[dest_pos[0]][dest_pos[1]] = "S"
        self.maze[org_pos[0]][org_pos[1]] = " "


    def read_key(self) -> str:
        """
        Read and return the key entered by user.
        """
        while True:
            if keyboard.is_pressed("right"):
                return "right"
            elif keyboard.is_pressed("left"):
                return "left"
            elif keyboard.is_pressed("up"):
                return "up"
            elif keyboard.is_pressed("down"):
                return "down"
            elif keyboard.is_pressed("p"):
                return "p"


    def display_maze(self) -> None:
        """
        Display the updated maze.
        """

        print()
        for row in self.maze:
            print("\t\t", end='')
            for col in row:
                print(col, end='')

        print()


my_game = Game(new_maze)
my_game.start()
