from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from the '{from_file}' file to the '{to_file}' file.")

in_file = open(from_file)
in_data = in_file.read()

print(f"The source file is {len(in_data)} bytes in size.")

print(f"Does the target file exist? {exists(to_file)}")
print("It's done, press Enter to continue or CTRL+C to cancel")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Excellent, it's done.")

in_file.close()
out_file.close()
