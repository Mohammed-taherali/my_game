"""
Created by: Mohammed Taherali

A simple maze game using the terminal.
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

# full path name for debugging.
# "C:\\Users\\91841\\Desktop\\mohammed\\my_game\\mazes\\maze.txt"


# Get maze.
maze = []
with open(maze_dir) as file:
    maze = file.readlines()

# How to check whether a key is pressed or not.
# while True:
#     if keyboard.is_pressed("left"):
#         print("P pressed")
#         break

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

    get_pos(maze: list[list]) -> tuple
        Takes the maze (list of lists) as input parameter and returns a tuple containing the co-ordinates of the user ('S')

    update_pos(curr_pos: tuple, maze: list[list]) -> list[list]
        Updates the position of user ('S') and returns the updated maze.
    """
    
    def __init__(self, maze) -> None:
        """
        Initialize the Game class variables.
        """
        self.maze = maze

    # COMPLETE
    def start(self):
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

    # TODO
    def play(self):
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
                

    # COMPLETE
    def help(self) -> None:
        """
        Load help message.
        """

        self.help_message = """
        Welcome to 'The Maze'.
        This is a simple maze game wherein the goal is to reach the end of the maze.
        
        Controls:
        Use arrow keys to move left, right, up and down.
        P - Pause the game."""
        print(self.help_message)
        print("(Press Enter to go to home screen.)")
        input()
        self.start()

    # COMPLETE
    def get_pos(self, elem: str) -> tuple:
        """
        Find the position of the given element.
        """

        for row_no, row in enumerate(self.maze):
            for col_no, col in enumerate(row):
                if col == elem:
                    return (row_no, col_no)

    # CHANGES MADE.
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

    # COMPLETE
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

        # print(dest_pos[0], dest_pos[1])
        # print(org_pos[0], org_pos[1])
        self.maze[dest_pos[0]][dest_pos[1]] = "S"
        self.maze[org_pos[0]][org_pos[1]] = " "

    # COMPLETE
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

    # COMPLETE
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

    # def __init__(self, maze) -> None:
    #     """
    #     Initialize the variables.
    #     """

    #     self.maze = maze
    #     self.choice = int()
    #     self.end_pos = tuple()
    #     self.start_pos = tuple()
    #     self.curr_pos = tuple()
    #     self.help_message = str()
    #     self.key_press = str()
    #     self.temp_pos = tuple()
    #     self.user_pos = tuple()


    # def start(self) -> None:
    #     """
    #     Start the main game.
    #     """

    #     print("\n\t\t\tWELCOME TO: 'THE MAZE!'")
    #     print("Play (1) \nHelp (2) \nQuit (3)")

    #     # Get User's choice
    #     try:
    #         self.choice = int(input("> "))
    #     except ValueError:
    #         self.start()

    #     # Call respective method corresponding to the selected option.
    #     if self.choice == 1:
    #         self.play()
    #     elif self.choice == 2:
    #         self.help()
    #     elif self.choice == 3:
    #         exit()
    #     else:
    #         self.start()


    # def play(self) -> None:
    #     """
    #     This function contains the main code of the game.
    #     """

    #     # end_pos = self.end_pos(self.maze)

    #     # while True:
    #     #     # Get current position and maze.
    #     #     self.current_pos = self.get_pos(self.maze)
    #     #     self.maze = self.update_pos(self.current_pos, self.maze)
    #     #     print(self.current_pos)
    #     #     for row in self.maze:
    #     #         for col in row:
    #     #             print(col, end='')
    #     #     exit()

    #     # Get the initial position of user and the endpoint.
    #     self.start_pos = self.get_pos()
    #     self.end_pos = self.final_pos()
    #     self.curr_pos = self.start_pos

    #     # Start the while loop of game.
    #     while True:

    #         # Wait for user input.
    #         self.key_press = self.get_dir()
    #         self.temp_pos = self.update_pos()
    #         if not self.check_hash():
    #             pass
    #             self.update_maze()
    #         print(self.maze)
    #         exit()

    # def help(self) -> None:
    #     """
    #     Print help message.
    #     """
        
    #     self.help_message = """
    #     Welcome to 'The Maze'.
    #     This is a simple maze game wherein the goal is to reach the end of the maze.
        
    #     Controls:
    #     Use arrow keys to move left, right, up and down.
    #     P - Pause the game."""
    #     print(self.help_message)
    #     print("(Press Enter to go to home screen.)")
    #     input()
    #     self.start()


    # def get_pos(self) -> tuple:
    #     """
    #     Get the current position of user.
    #     """

    #     for row_no, row in enumerate(self.maze):
    #         for col_no, col in enumerate(row):
    #             if col == "S":
    #                 return (row_no, col_no)
                    

    # def check_hash(self) -> bool:
    #     """
    #     Check if there is hash at the given location or not.
    #     Returns True if hash is present, False otherwise.
    #     """
    #     if self.maze[self.temp_pos[0]][self.temp_pos[1]] == "#":
    #         return True
    #     else:
    #         return False

    # def update_maze(self) -> None:
    #     """
    #     Update the maze by changing the position of the user.
    #     """

    #     self.user_pos = self.get_pos()
    #     self.maze[self.temp_pos[0]][self.temp_pos[1]] = "S"
    #     self.maze[self.user_pos[0]][self.user_pos[0]] = " "


    # def final_pos(self) -> tuple:
    #     """
    #     Returns the exit or endpoint of maze.
    #     """

    #     for row_no, row in enumerate(self.maze):
    #         for col_no, col in enumerate(row):
    #             if col == "E":
    #                 return (row_no, col_no)


    # def get_dir(self):
    #     """
    #     Get the key pressed by user.
    #     """

    #     return keyboard.read_key()


    # def update_pos(self) -> tuple:
    #     """
    #     Update the user's current position.
    #     """

    #     if dir == "left":
    #         return (self.curr_pos[0], self.curr_pos[1] - 1)
    #     elif dir == "right":
    #         return (self.curr_pos[0], self.curr_pos[1] + 1)
    #     elif dir == "up":
    #         return (self.curr_pos[0] - 1, self.curr_pos[1])
    #     elif dir == "down":
    #         return (self.curr_pos[0] + 1, self.curr_pos[1])


    # # def update_pos(self, curr_pos: tuple, maze: list[list]) -> list[list]:
    #     """
    #     Update user's current position.
    #     """
        


    #     # if curr_pos == self.get_pos(maze):
    #     #     return maze
    #     # else:
    #     #     new_pos = self.get_pos(maze)
    #     #     print(maze)
    #     #     maze[new_pos[0]][new_pos[1]] = "S"
    #     #     maze[curr_pos[0]][curr_pos[1]] = " "
    #     #     return maze


# my_game.start()

# for row in t:
#     for col in row:
#         print(col, end='')