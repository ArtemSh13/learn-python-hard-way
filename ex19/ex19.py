def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"We have {cheese_count} pieces of cheese!")
    print(f"We have {boxes_of_crackers} boxes of crackers!")
    print(f"It's enough for a party!")
    print("Let's go!\n")


print("We can give numbers directly to a function:")
cheese_and_crackers(20, 30)


print("OR we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We even can perform calculations inside a function:")
cheese_and_crackers(10 + 20, 5 + 6)


print("and combine variables with calculations:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("You won't believe, we can ask arguments from a user right in the function:")
cheese_and_crackers(int(input("How much cheese do tou want? > ")),
                    int(input("How many crackers do you want? > ")))
