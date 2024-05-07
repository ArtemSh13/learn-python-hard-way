people = 30
cars = 40
trucks= 15


if cars > people:
    print("We'll go by car")
elif cars < people:
    print("We won't go by car")
else:
    print("We can't choose")

if trucks > cars:
    print("Too many trucks.")
elif trucks < cars:
    print("Maybe we should take the truck?")
else:
    print("We still can't choose.")

if people > trucks:
    print("OK, let's go by truck.")
else:
    print("Great, let's stay at home.")
