from sys import argv

script, filename = argv

print(f"I'm erase the {filename} file")
print("If you wouldn't like to erase it, press the CTRL+C (^C) hotkey")
print("If you would like to erase the file, press Enter")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Erasing the file. Goodbye!")
target.truncate()

print("Now I'm asking you three lines")

line1 = input("")
line2 = input("")
line3 = input("")

print("I'll write it to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"These lines were written to the {filename} file:\n{line1}\n{line2}\n{line3}")
print("And finally I'll close the file")
target.close()

print(f"Let's check that the lines were written correctly\nOpening and reading the {filename} file...")
target = open(filename)
content = target.read()
print(f"This is the {filename} file content:\n{content}")
print("All right!")
