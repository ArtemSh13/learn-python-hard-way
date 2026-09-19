print("Let's practice!")
print("You have to know about escape sequences with the \\ character, which:")
print("\n manage line breaks and \t indentations.")

poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\tи никогда не отпускать!
"""

print("---------------------------------")
print(poem)
print("---------------------------------")


five = 10 - 2 + 3 - 6
print(f"Five should be here: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1_000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10_000
beans, jars, crates = secret_formula(start_point)

# Remember that it's yet another way to format a string
print("Starting from: {}".format(start_point))
# like f-string
print(f"We have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("Also we can do it this way:")
formula = secret_formula(start_point)
# An easy way to apply a list to creating string
print("We have {} beans, {} jars and {} crates.".format(*formula))
