#Importing Things

#Creating your character
name = input("What shall I call you?")

#Introduction
print(f"""Hello, {name}, and welcome to my scary forest of horrors!
To escape pursuit by your enemies, you must make it through the scary forest.
Go forth, {name}, you wary traveler.""")

#What maze
maze_number = int(input("Pick a number from 0 to 9"))

#Two piece maze
if maze_number == 3:
    location = 1
    def show_progress():
            """Show how you are doing"""
            print(f"""The arrangement of squares is 1 2 3
                              4 5 6
                              7 8 9.
            You may move to any adjacent square, unless the path is blocked.
            You are in square {location}. The exit is in square 8.""")
    while True:

        if location == 1:
            show_progress()
            print("A cobra blocks the path to square 4. You must proceed to square 2.")
            location = 2
        if location == 2:
            show_progress()
            print("""
    You may proceed to square 1, square 3, or square 5. What do you pick?""")
            location = int(input("1, 3 or 5?"))
        if location == 3:
            show_progress()
            print("""
    A gate slams behind you. You may not go back to square 2. You must proceed to square 6""")
            location = 6
        if location == 6:
            print()
