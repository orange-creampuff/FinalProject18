#Importing Things
import random

def show_progress():
    """Show how you are doing"""
    print(f"""

The arrangement of squares is 1 2 3
                              4 5 6
                              7 8 9.
    You may move to any adjacent square, unless the path is blocked.
    You are in square {location}. The exit is in square 8.

    """)

#Creating your character
name = input("What shall I call you? ")

#Introduction
print(f"""Hello, {name}, and welcome to my scary forest of horrors!
To escape pursuit by your enemies, you must make it through the scary forest.
Go forth, {name}, you wary traveler.""")

location = "1"
numberoftheday = random.randint(1,3)
snake_charmer = False
ogre_sleeping = True

while location != "8":
    if location == "1":
        yes_or_no = "Undefined"
        if snake_charmer:
            while yes_or_no != "y" and yes_or_no != "n":
                yes_or_no = input("A cobra block the path to square 4. You may charm the snake. Do you? Type y or n ")
        elif not snake_charmer:
            yes_or_no = "n"
        if yes_or_no == "y":
            print("The snake gives way and you proceed on the path.")
            location = "4"
        elif yes_or_no == "n":
            print("A cobra blocks the path to square 4. You must proceed to square 2.")
            location = "2"
    elif location == "2":
        show_progress()
        print("You may proceed to square 1, square 3, or square 5. What do you pick?")
        while location != "1" and location != "3" and location != "5":
            location = input("Type 1, 3 or 5. ")
    elif location == "3":
        print("A gate slams behind you. You may not go back to square 2. You must proceed to square 6")
        location = "6"
    elif location == "6":
        print("A wizard gives you the snake charmer. Then you fall into a sewer and float back to square 1")
        snake_charmer = True
        location = "1"
    elif location == "5":
        show_progress()
        print("""
        You are soo close to the exit.
        The only thing now stands between you and the exit is a mighty muscular ogre""")
        if not ogre_sleeping:
            ogre_battle = "Undefined"
            while ogre_battle.lower() != "y" and ogre_battle.lower() != "n":
                ogre_battle = input("Do you battle the ogre? Type y or n ")
                if ogre_battle.lower() == "y":
                    print("""The hulking ogre gives you a massive beating. You fall asleep and fly through the skies above the forest.

                    You wake up on a cloud, seemingly above square 2.""")
                    location = "2S"
                elif ogre_battle.lower() == "n":
                    while location != "2" and location != "4" and location != "6":
                        location = input("You may proceed to squares 2, 4, or 6. Which will it be? ")
        else:
            print("The ogre is sleeping and will not fight you this time.")
            while location != "2" and location != "4" and location != "6":
                location = input("You may proceed to squares 2, 4, or 6. Which will it be? ")
            ogre_sleeping = False
    elif location == "2S":
        print("""
        Welcome chosen one. We have been awaiting you.
        Take a seat, have some tea.""")
        fly_with_the_birds = "Undefined"
        while fly_with_the_birds.lower() != "y" and fly_with_the_birds.lower() != "n":
            fly_with_the_birds = input("We are going on a trip across the forest in the skies. Do you join us? Type y or n ")
            if fly_with_the_birds.lower() == "y":
                print("The birds take you far across the skies. You land in a meadow")
                location = "8"
            elif fly_with_the_birds.lower() == "n":
                print("The birds are offended and make you go down a fireman's pole into square 2")
                location = "2"
    elif location == "4":
        show_progress()
        print("You are at the foot of a tall mountain. You may attempt the climb to square 7 or return to suare 5.")
        while location != "5" and location != "7":
            location = input("Climb to 7 or return to 5? ")
    elif location == "7":
        show_progress()
        print("""You are getting close and things are getting interesting.
        You are at the summit. Unfortunately, attempting the descent into the meadow is not possible right now.""")
        sleep_eagle = "Undefined"
        while sleep_eagle.lower() != "y" and sleep_eagle.lower()!= "n":
            sleep_eagle = input("Do you lie down to rest in the eagle's nest? Type y or n ")
        if sleep_eagle.lower() == "y":
            print("""You wake up in the firm claws of mama eagle.
            She does not hurt you, even though she did not ask to be fed worms.
            Together, you fly through the skies""")
            location = "2S"
        elif sleep_eagle.lower() == "n":
            print("You are forced to descend the mountain to 4 or swim across the mountain lake to square 9.")
            while location != "4" and location != "9":
                location = input("Descend to 4 or brave the risky waters to 9? Type 4 or 9 ")
    elif location == "9":
        print("A programmer controls access to the gate to the meadow. He does not like you.")
        your_choice = "undefined"
        while your_choice != "1" and your_choice != "2" and your_choice != "3":
            your_choice = input("If you guess the number I am thinking of, I will program this gate to open. Type an integer from 1 to 3. ")
        your_choice = int(your_choice)
        if your_choice == numberoftheday:
            print("Curses, should have chosen a different number today. Well, here you go.")
            location = "8"
        else:
            print("""HAHAHAHAHA! Come back another time!
            The programmer pushes you down the mountain to square 6.""")
            location = "6"




print(f"Congratulations, {name}! You have successfully made it out of my maze of horrors!")





