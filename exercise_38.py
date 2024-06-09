ten_things = "Apples Oranges Crows Phones Light Sugar"

print("Wait, there are less than 10 objects. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Bear",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Appending: ", next_one)
    stuff.append(next_one)
    print(f"Now we have {len(stuff)} objects.")

print("So: ", stuff)

print("Let's do something with our objects.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
