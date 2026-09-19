# it looks like a script with argv
def print_two(*argv):
    argv1, argv2 = argv
    print(f"argv1: {argv1}, argv2: {argv2}")


# ok, here we're doing this instead *argv
def print_two_again(argv1, argv2):
    print(f"argv1: {argv1}, argv2: {argv2}")


# it takes only one argument
def print_one(argv1):
    print(f"argv1: {argv1}")


# it takes no arguments
def print_none():
    print("I take nothing.")


print_two("Michael", "Ann")
print_two_again("Michael", "Ann")
print_one("First!")
print_none()
