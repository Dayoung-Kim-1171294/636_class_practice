list_of_numbers = [10, 25, 3, 47, 15]

for i in range(len(list_of_numbers)):
    if i + 1 < len(list_of_numbers):
        if list_of_numbers[i] > list_of_numbers[i+1]:
            print(f"{list_of_numbers[i]} is greater than {list_of_numbers[i+1]}")
        elif list_of_numbers[i] < list_of_numbers[i+1]:
            print(f"{list_of_numbers[i]} is less than {list_of_numbers[i+1]}")
        else:
            print(f"{list_of_numbers[i]} is equal to {list_of_numbers[i+1]}")