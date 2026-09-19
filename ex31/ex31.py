print("""You're in a dark room with two doors.
Which door will you enter - 1 or 2?
""")

door = input("> ")

if door == "1":
    print("There is a giant bear eating the \"Druzhba\" cheese in this room.")
    print("What will you do?")
    print("1. To take away the cheese.")
    print("2. To yell in the bear's ear.")

    bear = input("> ")

    if bear == "1":
        print("The bear grabbed your face. Just fine!")
    elif bear == "2":
        print("The bear bit your leg. Just fine!")
    else:
        print(f"Fine, the {bear} action was the only right one.")
        print("The bear ran away.")

elif door == "2":
    print("You're looking into the endless abyss of Cthulhu's eyes. What will you do?")
    print("1. To talk about swamps in Siberia.")
    print("2. To pull the yellow buttons on my jacket.")
    print("3. To try whistle the \"Black raven\" song.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("You're saved because Cthulhu turned into jelly.")
        print("Just fine!")
    else:
        print("Madness seized you and you fell into a pool of rot.")
        print("Just fine!")

else:
    print("Madness seized you and you tore your face up. Good job!")
