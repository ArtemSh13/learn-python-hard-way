from sys import exit


def gold_room():
    print("There's plenty of gold here. How many kg will you carry?")

    choice = input("> ")
    how_much = -1

    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead("Hey, you have to enter a number.")

    if how_much < 50:
        print("Gorgeous! You're not greedy, so you win")
        exit(0)
    else:
        dead("You're greedy!")


def bear_room():
    print("The bear is sitting here.")
    print("The bear has a barrel of honey.")
    print("The bear closed the exit door behind him.")
    print("How do you move the bear? Take away the honey or tease the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice.lower() == "take away the honey":
            dead("The bear looked at you and hit you in the face with his paw.")
        elif choice.lower() == "tease the bear" and not bear_moved:
            print("The bear moved away from the door.")
            print("You can enter this. Tease the bear ot enter the door?")
            bear_moved = True
        elif choice.lower() == "tease the bear" and bear_moved:
            dead("The bear got angry and bit off your leg.")
        elif choice.lower() == "enter the door" and bear_moved:
            gold_room()
        else:
            print("Enter one of the suggested actions.")


def cthulhu_room():
    print("The great and terrible Cthulhu is looking at you.")
    print("He looks at you and you start to go crazy.")
    print("Run away or start fighting?")

    choice = input("> ")

    if "run away" in choice.lower():
        start()
    elif "start fighting" in choice.lower():
        dead("Hm, it may even be possible to win!")
    else:
        cthulhu_room()


def dead(why: str):
    print(why, "Excellent!")
    exit(0)


def start():
    print("You're in a dark room.")
    print("There are two doors leading from here, to the left and to the right.")
    print("Where will you turn?")

    choice = input("> ")

    if choice.lower() == "left":
        bear_room()
    elif choice.lower() == "right":
        cthulhu_room()
    else:
        dead("You go from room to room until you're starving.")


start()
