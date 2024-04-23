from sys import argv

script, filename = argv

txt = open(filename)

print(f"The content of the {filename} file:")
print(txt.read())
txt.close()

print("Enter the file name again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
