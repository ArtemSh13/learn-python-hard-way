people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not too many cats! The world is saved!")

if people < dogs:
    print("The world drowned in saliva!")

if people > dogs:
    print("It's not that bad!")


dogs += 5

if people >= dogs:
    print("There are more people or as many as dogs.")

if people <= dogs:
    print("There are less people or as many as dogs.")


if people == dogs:
    print("There are people as many as dogs.")
