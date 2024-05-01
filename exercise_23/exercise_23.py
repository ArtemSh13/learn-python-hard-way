import sys

script, encoding, error = sys.argv


# A recursive function to read lines of the file
def main(language_file, encoding, errors):
    line = language_file.readline()
    # Call the function until there are lines in the file
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# A function to print encoded and decoded strings
def print_line(line, encoding, errors):
    # Removing spaces at the beginning and at the end of the line
    next_lang = line.strip()
    # Encode the string to bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Decode the bytes to characters
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


languages = open("exercise_23/languages.txt", encoding="utf-8")

main(languages, encoding, error)