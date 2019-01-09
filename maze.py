#Importing Things


def show_progress():
    """Show how you are doing"""
    print(f"""The arrangement of squares is 1 2 3
                      4 5 6
                      7 8 9.
    You may move to any adjacent square, unless the path is blocked.
    You are in square {location}. The exit is in square 8.""")

#Creating your character
name = input("What shall I call you?")

#Introduction
print(f"""Hello, {name}, and welcome to my scary forest of horrors!
To escape pursuit by your enemies, you must make it through the scary forest.
Go forth, {name}, you wary traveler.""")

location = 1

while location != 8:
    show_progress()
    if location == 1:
        print("A cobra blocks the path to square 4. You must proceed to square 2.")
        location = 2
    elif location == 2:
        print("You may proceed to square 1, square 3, or square 5. What do you pick?")
        location = int(input("1, 3 or 5?"))
    elif location == 3:
        print("A gate slams behind you. You may not go back to square 2. You must proceed to square 6")
        location = 6
    elif location == 6:
        print("You fall into a sewer and float back to square 1")
        location = 1
    elif location == 5:
        print("""
        You are soo close to the exit.
        The only thing now stands between you and the exit is a mighty muscular ogre""")
        ogre_battle = "Undefined"
        while ogre_battle.lower() != "y" and ogre_battle.lower() != "n":
            ogre_battle = input("Do you battle the ogre? Type y or n")
            if ogre_battle.lower() == "y":
                print("""The hulking ogre gives you a massive beating. You fall asleep and fly through the skies above the forest.

                You wake up on a cloud, seemingly above square 2.""")
                location = "2S"
            elif ogre_battle.lower() == "n":
                location = int(input("You may proceed to squares 2, 4, or 6. Which will it be?"))
    elif location == "2S":
        print("""
        Welcome chosen one. We have been awaiting you.
        Take a seat, have some tea.""")
        fly_with_the_birds = "Undefined"
        while fly_with_the_birds.lower() != "y" and fly_with_the_birds.lower() != "n":
            fly_with_the_birds = input("We are going on a trip across the forest in the skies. Do you join us? Type y or n")
            if fly_with_the_birds.lower() == "y":
                print("The birds take you far across the skies. You land in a meadow")
                location = 8
            elif fly_with_the_birds.lower() == "n":
                print("The birds are offended and make you go down a fireman's pole into square 2")
                location = 2
    elif location == 4:
        print("You are at the foot of a tall mountain. You may attempt the climb to square 7 or return to suare 5.")
        while location != 5 and location != 7:
            location = int(input("Climb to 7 or return to 5?"))



print("Congratulations! You have successfully made it out of the maze of horrors!")





