#Importing Things

#Creating your character
name = input("What shall I call you?")

#Introduction
print(f"""Hello, {name}, and welcome to my scary forest of horrors!
To escape pursuit by your enemies, you must make it through the scary forest.
Go forth, {name}, you wary traveler.""")

#Size of maze
maze_size = int(input("Do you want a size 3 or 4 maze?"))

#Two piece maze
if maze_size == 3:
    print("""The arrangement of squares is 1 2 3
                              4 5 6
                              7 8 9.
    You may move to any adjacent square, unless the path is blocked.
    You are in square 1. The exit is in square 8.
    A cobra blocks the path to square 4. You must proceed to square 2.""")
    print("""1 2 3
4 5 6
7 8 9.
You may proceed to square 5 or square 3. What do you pick?""")
    int(input("5 or 3?"))