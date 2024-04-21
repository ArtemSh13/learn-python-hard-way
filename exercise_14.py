from sys import argv

script, firstname, lastname = argv
prompt = '> '

print(f"Hello, {firstname} {lastname}, I'm the {script} script.")
print("I'd like to ask you some questions.")
print(f"Do you like me, {firstname} {lastname}?")
likes = input(prompt)

print(f"Where do you live, {firstname} {lastname}?")
lives = input(prompt)

print("What computer do you work on?")
computer = input(prompt)

print(f"""
So, you answered \"{likes}\" to the question of whether you like me.
You live in {lives}. I have no idea where it is.
And you have the {computer} computer. Excellent!
""")
