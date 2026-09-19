the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "peach", "apricot"]
change = [1, "ten", 2, "fifty", 3, "hundred"]

# the first type of "for" cycle process a list
for number in the_count:
    print(f"Count {number}")

# the same as above
for fruit in fruits:
    print(f"Fruit: {fruit}")

# it's also possible to process combined lists
# pay your attention characters {} are used, because the type of the value
# isn't known
for i in change:
    print(f"I get {i}")

# also we can create lists, let's start with empty
elements = []

# then the range() function is used to limit the range
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append - a function to add an element to the list
    elements.append(i)

# now we print them
for i in elements:
    print(f"Element number: {i}")
