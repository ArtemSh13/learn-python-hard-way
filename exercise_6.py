# Why 10? There are only two types...
types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "Python"
do_not = "don't"
y = f"Those who understand {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"Also I said: '{y}'")

# "hilarious" is a synonym of the word "funny"
hilarious = False
joke_evaluation = "Is it funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This part of the line is on the left..."
e = "and this one is on the right"

# This operation is called "concatenation"
print(w + e)
