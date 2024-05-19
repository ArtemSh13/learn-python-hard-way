def just_numbers(end_value: int, step: int) -> list[int]:
    i = 0
    numbers = []
    while i < end_value:
        print(f"At the beginning, the value of i is {i}")
        numbers.append(i)

        i = i + step
        print("Current values: ", numbers)
        print(f"At the end, the value of i is {i}")
    return numbers


print("Values: ")

for num in just_numbers(6, 1):
    print(num)
